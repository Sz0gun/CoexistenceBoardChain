### **`backend/middleware/auth_middleware.py`** - Middleware for Google OAuth token verification

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from backend.firebase.firebase_auth import verify_google_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=403, detail="Authorization header missing")
        user = verify_google_token(token)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        request.state.user = user
        response = await call_next(request)
        return response