*Slogan of the project*: [Reggae Mix for Harmony](https://music.youtube.com/watch?v=1CNmsjP4BZo&si=l_TrXJEGDGmqOqi9)

# Coexistence Board Chain - Telegram Chess Bot with AI

## Overview

**Coexistence Board Chain** is an interactive chess bot built for Telegram that promotes the idea of human-AI cooperation. Typically, the game is played in a 2x2 setting, where one human and one AI team up against another pair. The goal is not just to win, but to enhance collaboration and understand the balance between human skills and AI assistance. The core idea is to explore how humans and AI can coexist and cooperate effectively.

The project leverages a range of modern technologies to provide an engaging and dynamic chess-playing experience.

---

## Tech Stack

- **Python 3.9.1**: Backend logic and integration.
- **FastAPI**: API framework for backend services.
- **Firebase (Firestore & Firebase Authentication)**: User authentication and game state management.
- **Google Vertex AI**: AI-powered chess move suggestions.
- **Telethon**: Integration with Telegram API Gaming Platform uses HTML5 to manage a game.
- **Redis**: Session management and caching.
- **Docker & Kubernetes**: Containerization and deployment on Google Kubernetes Engine (GKE).
- **Cloudflare**: DNS and SSL for secure connections.
- **HTML5 & JavaScript (Frontend)**: WebView and WebSocket integration for the chessboard UI.

---

## Project Structure

The project structure was refined and updated during recent work. Below is an overview of the key components:

```
CoexistenceBoardChain/
│
├── backend/
│   ├── ai/
│   │   └── ai_integration.py           # Integration with Google Vertex AI
│   ├── firebase/
│   │   ├── firebase_auth.py            # Firebase Authentication setup
│   │   └── firebase_db.py              # Firestore database management
│   ├── game/
│   │   └── endpoints.py                # Game logic for handling moves
│   ├── middleware/
│   │   └── auth_middleware.py          # Middleware for Google OAuth verification
│   └── main.py                         # FastAPI entry point
│
├── config/
│   ├── settings.py                     # Centralized configuration
│   └── secrets.env                     # Sensitive environment variables
│
├── docker-compose.yml                  # Local Docker configuration
├── Dockerfile                           # Container image setup for FastAPI
├── frontend/
│   └── app.js                          # JavaScript for WebSocket communication
├── telegram_bot/
│   └── bot.py                          # Telegram bot logic using Telethon
├── tests/
│   ├── test_auth.py                    # Unit tests for Firebase authentication
│   ├── test_game_logic.py              # Unit tests for chess game logic
│   ├── test_websockets.py              # Tests for WebSocket communication
│
└── README.md                           # Project overview and setup instructions
```

---

## Running the Project

### 1. Prerequisites

- Python 3.9.1
- Poetry
- Docker & Docker Compose
- Google Cloud SDK (gcloud)

### 2. Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sz0gun/learn-2-learn.git
   cd learn-2-learn
   ```

2. **Install Dependencies**:
   Using Poetry, install the required dependencies:
   ```bash
   poetry install
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the `config` directory, containing:
   ```bash
   TELEGRAM_API_ID="your_api_id"
   TELEGRAM_API_HASH="your_api_hash"
   TELEGRAM_BOT_TOKEN="your_bot_token"
   FIREBASE_KEY_PATH="/path/to/firebase/credentials.json"
   GOOGLE_APPLICATION_CREDENTIALS="/path/to/gcp/service/account.json"
   ```

4. **Run Locally**:
   To start the backend API using FastAPI:
   ```bash
   poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```

5. **Run Tests**:
   Execute all tests using `pytest`:
   ```bash
   poetry run pytest tests/
   ```

---

## Deployment

To deploy the application, you need to set up Google Kubernetes Engine (GKE) and use Docker images for containerization.

### 1. Build Docker Image
```bash
docker build -t coexistenceboardchain .
```

### 2. Push Image to Google Container Registry
```bash
gcloud auth configure-docker
docker tag coexistenceboardchain gcr.io/c-b-chain/coexistenceboardchain:latest
docker push gcr.io/c-b-chain/coexistenceboardchain:latest
```

### 3. Deploy on GKE
Use Kubernetes manifests to deploy the services, or use Helm charts for more flexibility and easier upgrades.

---

## Testing

### **1. Unit and Integration Tests**
- **Unit tests** were implemented to verify individual functionalities, such as Firebase authentication and move validation in chess logic.
- **Integration tests** included checking the full cycle of game state persistence in Firebase Firestore.

### **2. WebSocket Tests**
- Verified the WebSocket communication flow between the client and the server.
- Debugging issues with asynchronous `websocket_connect` involved ensuring compatibility with the current async test frameworks and updating the implementation to work with `pytest-asyncio`.

### **3. End-to-End Testing (Coming Up)**
- Using **Cypress** to ensure a complete and integrated flow is functional, from user interaction with the Telegram bot through the WebView to AI-generated move suggestions.

---

## Future Improvements

- **Enhanced AI Collaboration**: Improve the AI-human interaction to better support users during the game, offering suggestions and insights into moves.
- **Extend to Multiplayer**: Add features to support full multiplayer modes, integrating more complex AI behavior for simultaneous player management.
- **Deploy Monitoring Tools**: Set up **Prometheus** and **Sentry** to monitor API performance and errors in real time.
- **Game Secrets**: After achieving stable API and communication functionality, add "secrets" to the game such as quizzes, non-standard super moves, traps, and other surprises to make the game more engaging and unpredictable.

---

## Conclusion
The game's concept of fostering human-AI collaboration is at the core of this project, encouraging players to strategize together as a team with AI, making it a unique and educational experience.
