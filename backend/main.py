from fastapi import FastAPI, WebSocket, Depends
from backend.game.endpoints import process_move
from backend.middleware.auth_middleware import AuthMiddleware
from backend.firebase.firebase_auth import verify_google_token
from config.settings import settings

app = FastAPI()

# Add Middleware for Google Token Verification
app.add_middleware(AuthMiddleware)

@app.post("/api/move")
async def move(source: str, target: str, token: str = Depends(verify_google_token)):
    result = process_move(source, target, token)
    return {"result": result}

@app.websocket("/ws/game")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)  # Broadcast back for real-time updates