from Chainblock import *

import hashlib

import json

import time

from MerkleTree import MerkleTree

def hash_block(block):

   return hashlib.sha256(json.dumps(block).encode()).hexdigest()


def valid_proof(transactions, last_hash, nonce):

   guess = (str(transactions) + str(last_hash) + str(nonce)).encode()

   guess_hash = hashlib.sha256(guess).hexdigest()

   print(guess_hash)

   return guess_hash[0:2] == '00'


def pow(blockchain, open_transactions):

   last_block = blockchain[-1]

   last_hash = hash_block(last_block)

   nonce = 0

   while not valid_proof(open_transactions, last_hash, nonce):

       nonce += 1

   return nonce

def mine_block(blockchain, open_transactions, historical_transactions, owner, reward):

    last_block = blockchain[-1]

    hashed_block = hash_block(last_block)

    nonce = pow(blockchain, open_transactions)

    reward_transaction = {

           'sender': 'MINING',

           'recipient': owner,

           'amount': reward,

           'time': int(time.time()),

           'index': last_block["index"] + 1
       }

    open_transactions.append(reward_transaction)

    for transaction in open_transactions:
        historical_transactions.append(transaction)

    block = {

       'previous_hash': hashed_block,

       'index': len(blockchain),

       'transaction': MerkleTree(open_transactions),

       'nonce': nonce

    }

    blockchain.append(block)

