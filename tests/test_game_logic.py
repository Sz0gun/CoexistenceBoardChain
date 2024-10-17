import pytest
from backend.game.endpoints import process_move

def test_valid_move():
    result = process_move("e2", "e4", "test_user")
    assert result == "Move accepted"

def test_invalid_move():
    result = process_move("e2", "e5", "test_user")
    assert result == "Illegal move"
