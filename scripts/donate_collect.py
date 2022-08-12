from brownie import Earthquake_Relief_Donation, Wei
from scripts.common import get_account,get_donor_account,Web3

def donate(donation_amt):
    donation = Earthquake_Relief_Donation[-1]
    donor_acc = get_donor_account()
    donation_amt_in_wei =  Web3.toWei(donation_amt, 'ether'); 

    #https://stackoverflow.com/questions/71227362/how-to-deal-when-testing-with-eth-brownie-for-a-sender-with-not-enough-balance
    print(f"The donation amount is {donation_amt_in_wei}")
    donation.donate({"from": donor_acc, "value": donation_amt_in_wei})

    #print('Donated ', Wei(donation_amt_in_wei).to('ether'))
    #print('Balance of donor in Eth ', Wei(donor_acc.balance()).to('ether'))


def collect_donated_amount():
    donation = Earthquake_Relief_Donation[-1]
    owner_account = get_account()
    
    initial_balance = owner_account.balance()
    #print('initial balance of owner in Eth ', Wei(initial_balance).to('ether'))

    donation.collect_donated_amount({"from": owner_account})

    final_balance = owner_account.balance()
    #print('final  balance of owner in Eth ', Wei(final_balance).to('ether'))

    print("Amount collected minus gas used :: ",Wei(final_balance- initial_balance).to('ether'))


def main(): 
    donation_amt = 1
    donate(donation_amt)
    collect_donated_amount()