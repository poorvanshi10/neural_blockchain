from core.ledger import Blockchain
from core.block import Block

# ==========================================
# SYSTEM TEST: WATCH THE MINING IN ACTION
# ==========================================
if __name__ == "__main__":
    print("🧠 Booting Neural Ledger Core...\n")
    ai_ledger = Blockchain()

    print("⛏️  Mining Block 1 (Processing Node A's AI weights)...")
    # You will notice a slight delay here as your CPU grinds through the math!
    ai_ledger.add_block(Block(1, {"node": "Node_A", "accuracy": 0.85}, ""))

    print("\n⛏️  Mining Block 2 (Processing Node B's AI weights)...")
    ai_ledger.add_block(Block(2, {"node": "Node_B", "accuracy": 0.89}, ""))

    print("\n--- Network Consensus Status ---")
    print(f"Total Blocks Secured: {len(ai_ledger.chain)}")
    print(f"Cryptographic Integrity Valid: {ai_ledger.is_chain_valid()}")
