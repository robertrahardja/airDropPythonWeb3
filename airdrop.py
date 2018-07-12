import sys
import csv
from web3 import Web3, HTTPProvider, IPCProvider
#change to ipc for mainnet
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
from solc import compile_source
from web3.contract import ConciseContract

myAddress = Web3.toChecksumAddress('3a20ca9b5cb5336325313442d5c10b2d4ae3229b')
contractAddress = Web3.toChecksumAddress('314635509ec21a4369bb91eeb096a611649536ef')
keyStore = '/Users/robertrahardja/Documents/Programming/gethTestnetTest/keystore/UTC--2018-07-12T06-36-52.531756834Z--3a20ca9b5cb5336325313442d5c10b2d4ae3229b'

toAddress = Web3.toChecksumAddress('096c9164def69f4f9e9fdf24be4b205c3a8f3d45')

#get abi text
f = open('abi.txt', 'r')
abiText = f.read()
f.close
#instantiate contract
contract = w3.eth.contract(address = contractAddress, abi = abiText)

#Test call of balance
ownerBalance = contract.call().balanceOf(myAddress)
print("To test testnet call: \nThe token balance of the sender is " + str(ownerBalance))


#get private key
with open(keyStore) as keyfile:
    encrypted_key = keyfile.read()
    pk = w3.eth.account.decrypt(encrypted_key, 'password')
    privateKey = pk.hex()
    # tip: do not save the key or password anywhere, especially into a shared source file
print("Owner private key is " + str(privateKey))


 #get nonce
nonce = w3.eth.getTransactionCount(myAddress)
print("Owner's nonce is "  + str(nonce))

 #make transaction instance
txn_dict = contract.functions.transfer(toAddress,1).buildTransaction({
    'from': myAddress,
    'chainId': 15,
    'gas': 140000,
    'gasPrice': w3.toWei('40', 'gwei'),
    'nonce': nonce,
})

#sign transaction
signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=privateKey)

#send transaction
result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
print("result is " + str(result.hex()))
#get transaction receipt
tx_receipt = w3.eth.getTransactionReceipt(result)

print("The transaction receipt is " + str(tx_receipt))
myNowBalance = contract.call().balanceOf(myAddress)
print("Now the balance of " + str(myAddress) + " is " + str(myNowBalance))
toNowBalance = contract.call().balanceOf(toAddress)
print("Now the balance of " + str(toAddress) + " is " + str(toNowBalance))
