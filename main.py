# Main.py
# Initializes and creates the running loop of the blockchain.
# Taken directly from https://blockgeeks.com/guides/python-blockchain-2/

from Chainblock import *

user_input = input("Give the first element of the Blockchain")

blockchain = [user_input]

print("hello")

while True:

   print("Choose an option")

   print('Choose 1 for adding a new transaction')

   print('Choose 2 for printing the blockchain')

   print('Choose 3 if you want to manipulate the data')

   print('Choose anything else if you want to quit')



   user_choice = get_user_choice()



   if user_choice == 1:

       tx_amount = get_transaction_value()

       add_value(blockchain, tx_amount, get_last_value(blockchain))



   elif user_choice == 2:

       print_block(blockchain)



   elif user_choice == 3:

       if len(blockchain) >= 1:

           blockchain[0] = 2



   else:

       break



   if not verify_chain(blockchain):

       print('Blockchain manipulated')

       break