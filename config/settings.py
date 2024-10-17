### **`config/settings.py`** - Centralized configuration file

from pydantic import BaseSettings

class Settings(BaseSettings):
    telegram_api_id: str
    telegram_api_hash: str
    telegram_bot_token: str
    vertex_ai_model_id: str
    firebase_key_path: str
    google_application_credentials: str
    redis_host: str = 'redis-server'
    redis_port: int = 6379
    slogan_link: str = "https://music.youtube.com/watch?v=1CNmsjP4BZo&si=l_TrXJEGDGmqOqi9"

    # MTProto server configuration
    test_server_address: str
    test_public_key: str
    production_server_address: str
    production_public_key: str

    class Config:
        env_file = "config/secrets.env"

settings = Settings()

