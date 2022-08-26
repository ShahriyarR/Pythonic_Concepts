from unittest import mock
import pytest


from src.code3 import User

def test_user_add():
    database = mock.Mock()
    database.is_connected = True
    database.persist.return_value = "MySQL has persisted: data"

    user = User(database=database)
    assert user.add("data") == "MySQL has persisted: data"