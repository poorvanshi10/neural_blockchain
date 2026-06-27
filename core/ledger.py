from core.block import Block
import requests # NEW: For talking to other nodes
from urllib.parse import urlparse

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 
        self.nodes = set() # NEW: Keeps track of neighbor IPs

    def create_genesis_block(self):
        return Block(0, {"message": "Neural Network Initialized"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty) 
        self.chain.append(new_block)

    def is_chain_valid(self, chain=None):
        target_chain = chain if chain else self.chain
        for i in range(1, len(target_chain)):
            current = target_chain[i]
            previous = target_chain[i - 1]

            # Allow validation of dictionary objects coming over HTTP
            current_hash = current.get('hash') if isinstance(current, dict) else current.hash
            prev_hash = previous.get('hash') if isinstance(previous, dict) else previous.hash
            
            if current.get('previous_hash', current.previous_hash) != prev_hash:
                return False
        return True

    # --- NEW P2P METHODS ---
    def register_node(self, address):
        # Parses the URL and adds the neighbor to our set
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def resolve_conflicts(self):
        # The Consensus Algorithm: The Longest Valid Chain Wins
        neighbors = self.nodes
        new_chain = None
        max_length = len(self.chain)

        for node in neighbors:
            try:
                # Ask the neighbor for their chain
                response = requests.get(f"http://{node}/chain", timeout=3)
                if response.status_code == 200:
                    length = response.json()['length']
                    chain = response.json()['chain']

                    # If their chain is longer, we prepare to adopt it
                    if length > max_length and self.is_chain_valid(chain):
                        max_length = length
                        new_chain = chain
            except requests.exceptions.RequestException:
                continue

        # Replace our chain if we found a longer, valid one
        if new_chain:
            self.chain = new_chain
            return True
        return False
