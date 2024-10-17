import pytest
from starlette.testclient import TestClient
from backend.main import app
from backend.firebase.firebase_db import store_game_state, get_game_state

client = TestClient(app)

def test_websocket_connection():
    with client.websocket_connect("/ws/game") as websocket:
        websocket.send_text("test move")
        response = websocket.receive_text()
        assert response == "test move"

@pytest.mark.asyncio
async def test_store_game_state():
    game_id = "test_game"
    state = {"board": "initial_state"}
    await store_game_state(game_id, state)
    retrieved_state = await get_game_state(game_id)
    assert retrieved_state == state
