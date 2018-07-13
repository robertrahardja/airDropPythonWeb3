import sys
import csv
import time
from web3 import Web3, HTTPProvider, IPCProvider
#change to ipc for mainnet
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
from solc import compile_source
from web3.contract import ConciseContract

fromAddress = Web3.toChecksumAddress('3a20ca9b5cb5336325313442d5c10b2d4ae3229b')
contractAddress = Web3.toChecksumAddress('314635509ec21a4369bb91eeb096a611649536ef')
keyStore = '/Users/robertrahardja/Documents/Programming/gethTestnetTest/keystore/UTC--2018-07-12T06-36-52.531756834Z--3a20ca9b5cb5336325313442d5c10b2d4ae3229b'

#get abi text
f = open('abi.txt', 'r')
abiText = f.read()
f.close

#instantiate contract
contract = w3.eth.contract(address = contractAddress, abi = abiText)

#loop to get balance
while True:
    #print sender balance
    senderBalance = contract.call().balanceOf(fromAddress)
    print ("\nSender:\n" + fromAddress + " has " + str(senderBalance) + " tokens\n")

    with open('csvTest') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #loop through and show balance of each account in csv
        for row in reader:
            ownerBalance = contract.call().balanceOf(Web3.toChecksumAddress(row[0]))
            print ( row[0] + " has " + str(ownerBalance) + " tokens\n")
            #print("To test testnet call: \nThe token balance of the sender is " + str(ownerBalance))

    print ("------------------------------------------------")        
    time.sleep(5)  
