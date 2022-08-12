from scripts.common import get_account,get_donor_account, LOCAL_BC_ENVS, Web3
from scripts.deploy import deploy_donation
from brownie import network, accounts, exceptions,Wei
import pytest

#Test cases to test smart contract
def test_donate_and_collect():

    owner_account = get_account()
    donor_acc = get_donor_account()

    donation = deploy_donation(owner_account)
    donation_amt = Web3.toWei(1, 'ether'); 
    
    #Test donate
    tx1 = donation.donate({"from": donor_acc, "value": donation_amt})
    tx1.wait(1)
    assert donation.s_addrToAmt(donor_acc.address) == donation_amt

    #Test donation amount collection
    tx2 = donation.collect_donated_amount({"from": owner_account})
    tx2.wait(1)
    
    assert donation.s_addrToAmt(donor_acc.address) == 0


def test_only_owner_can_collect():
    if network.show_active() not in LOCAL_BC_ENVS:
        pytest.skip("only meant local testing")
    
    owner_account = get_account()
    not_owner = accounts.add()

    donation = deploy_donation(owner_account)
    
    #Trying to collect from account other than owner should raise error
    with pytest.raises(exceptions.VirtualMachineError):
        donation.collect_donated_amount({"from": not_owner})


def test_only_non_owner_can_donate():
    owner_account = get_account()
    not_owner = accounts.add()

    donation = deploy_donation(owner_account)

    #Trying to donate from owner account should raise error
    with pytest.raises(exceptions.VirtualMachineError):
        donation.donate({"from": owner_account})
