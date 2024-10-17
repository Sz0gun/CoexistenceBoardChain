### **`backend/firebase/firebase_db.py`** - Firebase Firestore Database

from firebase_admin import firestore
import asyncio

db = firestore.client()

async def store_game_state(game_id: str, state: dict):
    await asyncio.to_thread(db.collection('games').document(game_id).set, state)

async def get_game_state(game_id: str):
    doc = await asyncio.to_thread(db.collection('games').document(game_id).get)
    return doc.to_dict() if doc.exists else None
