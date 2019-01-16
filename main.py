# Main.py
# Initializes and creates the running loop of the blockchain.
# Taken directly from https://blockgeeks.com/guides/python-blockchain-2/

from Chainblock import *

from mining import *

from MerkleTree import *

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

def process_Merkle(tree, transactions):

    print(transactions)
    for i in range(0, len(transactions)):
        path = tree.get_branch(transactions[i])
        if not tree.audit(transactions[i], path):
            print "Invalid transaction"
            break

while True:

   print("Choose an option")

   print('Choose 1 for adding a new transaction')

   print('Choose 2 for mining the blockchain')

   print('Choose 3 for printing the blockchain')

   print('Choose 4 to make a Merkle Tree out of the current Transaction List')

   print('Choose anything else if you want to quit')




   user_choice = get_user_choice()



   if user_choice == 1:

       tx_data = get_transaction_value()

       recipient, amount = tx_data

       add_value(open_transactions, recipient, amount=amount)

       print(open_transactions)



   elif user_choice == 2:

       mine_block(blockchain, open_transactions, owner, reward)


   elif user_choice == 3:

       print_block(blockchain)

   elif user_choice == 4:
       Merkle = MerkleTree(get_last_value(blockchain)["transaction"])
       print(Merkle)
       process_Merkle(Merkle, get_last_value(blockchain)["transaction"])

   else:

       break



   if not verify_chain(blockchain):

       print('Blockchain manipulated')

       break

