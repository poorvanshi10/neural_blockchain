from core.block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        # Difficulty of 4 means the hash MUST start with four zeros. 
        # This is what makes the CPU do the hard work.
        self.difficulty = 4 

    def create_genesis_block(self):
        return Block(0, {"message": "Neural Network Initialized"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        
        # Force the computer to solve the math puzzle BEFORE adding the block
        new_block.mine_block(self.difficulty) 
        
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
