import sys
import csv
from web3 import Web3, HTTPProvider, IPCProvider
#change to ipc for mainnet
web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
from solc import compile_source
from web3.contract import ConciseContract

contractAddress = '0x73f46e31f80bbd5fd43cc5c1350c09db3fa98a13'
myAddress = '0xdc9d7f1b0cfd80eb033a3935a1a23687fd36a960'
myPrivateKey = '0x1fc3b872b45db18c5a78ab883dbcc457d14092e064149d6753e9fd2697940424'
mnemonic = 'concert biology gaze electric wife control into unveil tomorrow decade exhibit near'
#toAddress = '0x850d5c22a64d6f835850870fab8bc0d3cafa1036'
#to be iterated from csv

#get abi text
f = open('abi.txt', 'r')
abiText = f.read()
f.close

#create contract
contract = web3.eth.contract(address = contractAddress, abi = abiText)

#loop over csvTest file
with open('csvTest') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        #get nonce
        nonce = web3.eth.getTransactionCount(myAddress)
        #make transaction instance
        txn_dict = contract.functions.transfer(row[0],row[1]).buildTransaction({
            'chainId': 3,
            'gas': 140000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
        })

        #sign transaction
        signed_txn = w3.eth.account.signTransaction(txn_dict, private_key=myPrivateKey)
        #send transaction
        result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        #get transaction receipt
        tx_receipt = w3.eth.getTransactionReceipt(result)
        #print confirmation of transaction sent
        print('transfer from ' + tx_receipt.from + ' to ' + tx_receipt.to + ' with transaction hash of ' + tx_receipt.transactionHash + ' is done.\n')
