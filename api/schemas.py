from pydantic import BaseModel
from typing import List

# Enforces the structure of an incoming AI model update
class ModelUpdate(BaseModel):
    node_id: str
    model_accuracy: float

# Enforces the structure when adding new peer IPs to the network
class PeerNodes(BaseModel):
    nodes: List[str]
