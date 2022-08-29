from unittest import mock
import pytest

from src.code6 import User


def test_user_add_mysql():
    database = mock.Mock()
    database.is_connected = True
    database.persist.return_value = "MySQL has persisted: data"

    user = User(database=database)
    assert user.add("data") == "MySQL has persisted: data"
    database.persist.assert_called()


def test_user_add_pg():
    database = mock.Mock()
    database.is_connected = True
    database.persist.return_value = "PG has persisted: data"

    user = User(database=database)
    assert user.add("data") == "PG has persisted: data"
    database.persist.assert_called()
