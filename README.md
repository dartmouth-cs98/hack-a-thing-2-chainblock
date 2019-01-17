# hack-a-thing-2-chainblock
hack-a-thing-2-chainblock created by GitHub Classroom

(ReadMe written by Ryan Hall, collaborated with Dev Jahveri)

We attempted to build a blockchain for the second hack-a-thing assignment.
We did this by using a tutorial found here: 
https://blockgeeks.com/guides/python-blockchain-2/
This blockchain was essentially a list which contained a record of previous
transactions and a block for the current transactions.

In general I worked on the features within mining.py while Dev worked on the 
features in Chainblock.py. Certain features in main were installed by me, including , while 
Dev worked on other features in main.

However, the tutorial itself had a number of errors. It did not adjust parts
of the code to account for the fact that transactions were implemented as a 
dictionary. Dev and I both spent a significant period of time adjusting code to 
account for this fact.

On top of the tutorial we added features to make our blockchain more 
sophisticated. In particular we stored our record of transactions in a Merkle tree
and used the validation features of a Merkle tree to verify that previous transactions 
were secure. We collaborated together in order to integrate these trees into our 
blockchain. At the same time, we needed to adjust 

Dev and I both learned about how blockchains work. Before this project, 
the actual implementation of a blockchain was somewhat abstract to us. We really
benefited from being able to see this object come alive in code. Additionally, we spent 
a lot of time learning how to construct and implement a Merkle Tree.

This project has very clear applications in cryptocurrencies which we both think would
be interesting to pursue. On top of this, blockchain can add security to a
variety of projects outside of crypto.

We attempted to build the Merkle Tree data type ourselves but were less than 
successful there. Instead, we ported code from here: 
https://hackernoon.com/merkle-tree-introduction-4c44250e2da7
in order to define the Merkle Trees and focused instead on how to integrate them
with our blockchain.  We also struggled with hashing the Merkle Tree inside of our blockchain
since the implementation of the hash in our tutorial used .json and our implementation of a 
Merkle tree was not .json serializable. This limited the number of Merkle Trees we could create. 
At the same time, we attempted to store the blockchain object for demonstration 
later but had difficulty using the python .pkl library.
