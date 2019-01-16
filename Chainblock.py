#   ChainBlock.py
#   Defines the Basic Methods of the Blockchain according to the first step of the tutorial:
#   https://blockgeeks.com/guides/python-blockchain-2/

def add_list(blockchain):

    blockchain.append([blockchain[-1], 3.2])
    print(blockchain)

def get_last_value(blockchain):

    return(blockchain[-1])

def add_value(open_transactions, recipient, sender=owner, amount=1.0):
    transaction = {'sender': sender,

                   'recipient': recipient,

                   'amount': amount}

    open_transactions.append(transaction)

def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')

    tx_amount = float(input('Enter your transaction amount '))

    return tx_recipient, tx_amount

def get_user_choice():
    user_input = input("Please give your choice here: ")

    return user_input

def print_block(blockchain):

   for block in blockchain:

       print("Here is your block")

       print(block)

def verify_chain(blockchain):

   index = 0

   valid = True

   for block in blockchain:

       if index == 0:

           index += 1

           continue

       elif block[0] == blockchain[index - 1]:

           valid = True

       else:

           valid = False

           break

       index += 1

   return valid