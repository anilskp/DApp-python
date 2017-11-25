#from web3 import Web3
import web3
from web3 import Web3, HTTPProvider, KeepAliveRPCProvider, IPCProvider
web3.__version__
import json


web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

print('Connected')
fromAddress=web3.personal.listAccounts[0]
toAddress=web3.personal.listAccounts[1]

bl=web3.fromWei(web3.eth.getBalance(fromAddress), "ether")

tobal=web3.fromWei(web3.eth.getBalance(toAddress), "ether")

ac = web3.eth.accounts

print('Etherbase:',bl,"Ether")
print('Account2:', tobal," Ether")

