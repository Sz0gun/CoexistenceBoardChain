import pytest
from backend.firebase.firebase_auth import verify_google_token

def test_valid_token(mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", return_value={"uid": "test_user"})
    user = verify_google_token("valid_token")
    assert user is not None

def test_invalid_token(mocker):
    mocker.patch("firebase_admin.auth.verify_id_token", side_effect=Exception("Invalid token"))
    user = verify_google_token("invalid_token")
    assert user is None
