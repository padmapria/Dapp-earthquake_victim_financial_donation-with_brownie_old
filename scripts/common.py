from brownie import network, config, accounts
from web3 import Web3
from random import choice

FORKED_LOCAL_ENVS = ["mainnet-fork"]

#development is brownie inbuilt ganache
LOCAL_BC_ENVS = ["development", "ganache-local"]

sequence = [i for i in range(1,10)]

#patrick github reference
#https://github.com/PatrickAlphaC/brownie_fund_me/blob/main/brownie-config.yaml
def get_account():
    if (
        network.show_active() in LOCAL_BC_ENVS
        or network.show_active() in FORKED_LOCAL_ENVS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

#To generate Test donor accounts
def get_donor_account():
    if (
        network.show_active() in LOCAL_BC_ENVS
        or network.show_active() in FORKED_LOCAL_ENVS
    ):
        return accounts[choice(sequence)]
    else:
        return accounts.add(config["wallets"]["from_key"])
