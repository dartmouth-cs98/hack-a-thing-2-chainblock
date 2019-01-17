# Main.py
# Initializes and creates the running loop of the blockchain.
# Taken directly from https://blockgeeks.com/guides/python-blockchain-2/

from Chainblock import *

from mining import *

from MerkleTree import *

import pickle

reward = 10.0

genesis_block = {

   'previous_hash': '',

   'index': 0,

   'transaction': [],

   'nonce': 23

}

blockchain = [genesis_block]

open_transactions = []

historical_transactions = []

owner = 'Blockgeeks'

def process_Merkle(tree, transactions):

    print(transactions)
    for i in range(0, len(transactions)):
        path = tree.get_branch(transactions[i])
        print(path)
        if not tree.audit(transactions[i], path):
            print "Invalid transaction"
            break

while True:

   print("Choose an option")

   print('Choose 1 for adding a new transaction')

   print('Choose 2 for mining the blockchain')

   print('Choose 3 for printing the blockchain')

   print('Choose 4 to confirm that a transaction in the history is in the blockchain')

   print('Choose anything else if you want to quit')

   user_choice = get_user_choice()

   if user_choice == 1:

       if len(open_transactions) >= 7:
           print("Too many transactions. Please mine a block to create a full merkel tree")

       else:
           tx_data = get_transaction_value()

           recipient, amount = tx_data

           add_value(blockchain, open_transactions, recipient, amount=amount)

           print(open_transactions)


   elif user_choice == 2:

       if len(open_transactions) < 7:

           print(" Please add more transactions until a Merkel Tree is ready to be created")

           print(" You need " + str(7-len(open_transactions)) + " more")

       if len(open_transactions) == 7:
           mine_block(blockchain, open_transactions, historical_transactions, owner, reward)
           open_transactions = []


   elif user_choice == 3:
       print_block(blockchain)


   elif user_choice == 4:

       print ("Please choose a transaction stored in history by typing in it's number")

       if len(historical_transactions) == 0:

           print("There are no historical transactions. Please make 7 and then mine a block")

       else:

           for x in range(0, len(historical_transactions)):

               print(str(x+1) + ". " + str(historical_transactions[x]))

           index = get_user_choice()

           if index < 1:

               print("Index too low. Please Try Again")

           elif index > len(historical_transactions):

               print("Index too high. Please Try Again")

           else:

               print(historical_transactions[index - 1])

               transaction_to_validate = historical_transactions[index - 1]

               block_index = transaction_to_validate["index"]

               block = blockchain[block_index]

               tree = block["transaction"]

               path = tree.get_branch(transaction_to_validate)

               if tree.audit(transaction_to_validate, path):
                   print ('Transaction valid and in BlockChain!')
               else:
                   print ('Transaction Failed - that is weird.')
   else:
       break



   if not verify_chain(blockchain):

       print('Blockchain manipulated')

       break