import unittest
from core.block import Block
from core.ledger import Blockchain

class TestNeuralBlockchain(unittest.TestCase):
    def setUp(self):
        # This runs before every test to boot up a fresh blockchain
        self.ledger = Blockchain()

    def test_genesis_block(self):
        # Proves the network starts correctly
        self.assertEqual(len(self.ledger.chain), 1)
        self.assertEqual(self.ledger.chain[0].previous_hash, "0")

    def test_mining_and_validation(self):
        # Proves a block can be mined and the chain remains valid
        new_block = Block(1, {"node": "Node_X", "accuracy": 0.95}, self.ledger.get_latest_block().hash)
        self.ledger.add_block(new_block)
        self.assertTrue(self.ledger.is_chain_valid())

    def test_tampering_detection(self):
        # SIMULATE A HACK: Proves the network catches altered AI data
        self.ledger.add_block(Block(1, {"accuracy": 0.90}, self.ledger.get_latest_block().hash))
        
        # A hacker sneaks in and changes the model accuracy to 99%
        self.ledger.chain[1].data = {"accuracy": 0.99}
        
        # The auditor should flag this as False (Invalid)
        self.assertFalse(self.ledger.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
