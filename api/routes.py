from fastapi import APIRouter, HTTPException
from core.ledger import Blockchain
from core.block import Block
from api.schemas import ModelUpdate, PeerNodes

router = APIRouter()
ai_ledger = Blockchain()

@router.get("/chain")
def get_chain():
    return {"length": len(ai_ledger.chain), "chain": ai_ledger.chain}

@router.post("/mine")
def mine_block(data: ModelUpdate):
    # Convert Pydantic model to dict
    new_block = Block(len(ai_ledger.chain), data.model_dump(), ai_ledger.get_latest_block().hash)
    ai_ledger.add_block(new_block)
    
    return {
        "message": "Model update verified and block mined!",
        "block": new_block.__dict__
    }

@router.post("/nodes/register")
def register_nodes(payload: PeerNodes):
    for node in payload.nodes:
        ai_ledger.register_node(node)
    return {"message": "New peer nodes registered", "total_nodes": list(ai_ledger.nodes)}

@router.get("/nodes/resolve")
def consensus():
    replaced = ai_ledger.resolve_conflicts()
    if replaced:
        return {"message": "Chain outdated. Replaced with network consensus.", "chain": ai_ledger.chain}
    return {"message": "Chain is authoritative.", "chain": ai_ledger.chain}
