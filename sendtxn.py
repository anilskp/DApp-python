#from web3 import Web3
import web3
from web3 import Web3, HTTPProvider, KeepAliveRPCProvider, IPCProvider
web3.__version__
import json


#from web3.providers.rpc import HTTPProvider
#web3 = Web3(HTTPProvider('"http://localhost:8545"'))

web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

print('Connected')
fromAddress=web3.personal.listAccounts[1]
toAddress=web3.personal.listAccounts[0]
#txn='{from: fromAddress,to: toAddress, value: web3.toWei(2,"ether")}'
bl=web3.fromWei(web3.eth.getBalance(fromAddress), "ether")

from getpass import getpass  
pw = getpass(prompt='Enter the password for the sender: ')

web3.personal.unlockAccount(fromAddress, pw)
params = {}
params['to'] = toAddress
params['from'] = fromAddress 
params['data'] = web3.toHex("testan") 
params['value'] = web3.toWei(2, "ether")
tx_hash = web3.eth.sendTransaction(params)

tobal=web3.fromWei(web3.eth.getBalance(toAddress), "ether")

ac = web3.eth.accounts
print(ac)
print(bl)
print(tobal)
print(tx_hash)
