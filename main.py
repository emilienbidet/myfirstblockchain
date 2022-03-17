import time

from block import Block
from blockchain import BlockChain

names_block_chain = BlockChain()

names_block_chain.add_block(Block(time.time(), "Alice"))
names_block_chain.add_block(Block(time.time(), "Bob"))
names_block_chain.add_block(Block(time.time(), "Charlie"))

print("Blockchain state:")
print()
print(names_block_chain)
print()
print("Blockchain valid? ", names_block_chain.is_valid())

names_block_chain.chain[1].mine(5)
# names_block_chain.chain[1].data = "Bob Jr."
# print()
# print("Blockchain valid? ", names_block_chain.is_valid())
