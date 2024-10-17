### **`backend/firebase/firebase_auth.py`** - Firebase Authentication

import firebase_admin
from firebase_admin import credentials, auth
from config.settings import settings

try:
    cred = credentials.Certificate(settings.firebase_key_path)
    firebase_admin.initialize_app(cred, name='coexistence_app')
except ValueError:
    app = firebase_admin.get_app(name='coexistence_app')
    
def verify_google_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        return None