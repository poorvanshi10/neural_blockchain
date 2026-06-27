from fastapi import FastAPI
from api.routes import router

# Initialize the web server
app = FastAPI(
    title="Neural Blockchain Node",
    description="Decentralized infrastructure for Federated Learning.",
    version="1.0.0"
)

# Connect our modular routing engine (brings in /mine, /chain, /nodes)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    print("🧠 Booting Neural Ledger API Node...")
    # Runs the server on port 8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
