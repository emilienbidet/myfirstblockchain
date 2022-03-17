from block import Block


class BlockChain:
    def __init__(self):
        self.chain = [Block(0, "Genesis Block")]

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block: Block):
        block.previous_hash = self.get_last_block().hash
        block.hash = block.get_hash()
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.get_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def __str__(self):
        return ("\n" + "-" * 30 + "\n").join([str(block) for block in self.chain])
