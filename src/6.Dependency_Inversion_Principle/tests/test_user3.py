from unittest.mock import patch, Mock
import pytest
import src


from src.code3 import User


def test_user_add():
    mock_database = Mock()
    mock_database.persist.return_value = "MySQL has persisted: data"
    
    user = User(database=mock_database)
    assert user.add("data") == "MySQL has persisted: data"
    mock_database.persist.assert_called()