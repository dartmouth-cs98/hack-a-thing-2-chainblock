# Main.py
# Initializes and creates the running loop of the blockchain.
# Taken directly from https://blockgeeks.com/guides/python-blockchain-2/

from Chainblock import *

from mining import *

reward = 10.0

genesis_block = {

   'previous_hash': '',

   'index': 0,

   'transaction': [],

   'nonce': 23

}

blockchain = [genesis_block]

open_transactions = []

owner = 'Blockgeeks'

while True:

   print("Choose an option")

   print('Choose 1 for adding a new transaction')

   print('Choose 2 for mining the blockchain')

   print('Choose 3 for printing the blockchain')

   print('Choose anything else if you want to quit')



   user_choice = get_user_choice()



   if user_choice == 1:

       tx_data = get_transaction_value()

       recipient, amount = tx_data

       add_value(blockchain, recipient, amount=amount)

       print(open_transactions)



   elif user_choice == 2:

       mine_block(blockchain, open_transactions, owner, reward)



   elif user_choice == 3:

       print_block(blockchain)



   else:

       break



   if not verify_chain(blockchain):

       print('Blockchain manipulated')

       break