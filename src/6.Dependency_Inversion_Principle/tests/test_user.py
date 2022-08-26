import pytest

from src.code import User

def test_user_add():
    user = User()
    assert user.add("data") == "MySQL has persisted: data"