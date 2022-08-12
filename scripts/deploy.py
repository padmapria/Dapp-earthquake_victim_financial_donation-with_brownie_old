from brownie import Earthquake_Relief_Donation, config,network
from scripts.common import (
    get_account
)
import time

#https://coinsbench.com/how-to-build-and-deploy-an-ethereum-wallet-with-brownie-and-infura-f36427df490f
def deploy_donation(account):

    donation = Earthquake_Relief_Donation.deploy(
        {"from": account},
        publish_source=config['networks'][network.show_active()].get("verify")
    )
    
    # To fix web3 not connected error
    #https://github.com/smartcontractkit/full-blockchain-solidity-course-py/issues/173
    time.sleep(1)

    print(f"Donation Contract Address {donation.address}")
    print(f"Donation owner Address {account}")

    #Write the end point details to a file
    f = open("contract_deployed_endpoint.env", "w")
    f.write("export Donation Contract Address = " +donation.address + "\n")
    f.write("export Donation owner Address = " +str(account))
    f.close()

    return donation


def main():
    account = get_account()
    deploy_donation(account)