import pytest

from src.code2 import User

def test_user_add():
    # You can't open connection to live database at each test run
    user = User()
    # Now we have untestable code!!!!
    assert user.add("data") == "MySQL has persisted: data"