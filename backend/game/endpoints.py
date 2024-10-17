### **`backend/game/endpoints.py`** - Game logic endpoint for handling moves

import chess

game = chess.Board()

def process_move(source: str, target: str, user):
    move = chess.Move.from_uci(f"{source}{target}")
    if move in game.legal_moves:
        game.push(move)
        return "Move accepted"
    return "Illegal move"