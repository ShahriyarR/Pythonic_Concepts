from typing import Optional
from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def persist(self, data: str):
        ...


class MySQLDatabase(Database):
    """
    MySQL database implementation class
    """

    # Imagine that here we have some kind of openning the actual real database connection

    def __init__(self) -> None:
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        print("Connected to MySQL")

    def persist(self, data: str) -> Optional[str]:
        if self.is_connected:
            print(f"MySQL has persisted: {data}")
            return f"MySQL has persisted: {data}"


class PGDatabase(Database):
    """
    MySQL database implementation class
    """

    # Imagine that here we have some kind of openning the actual real database connection

    def __init__(self) -> None:
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        print("Connected to PG")

    def persist(self, data: str) -> Optional[str]:
        if self.is_connected:
            print(f"PG has persisted: {data}")
            return f"PG has persisted: {data}"


class User:
    """
    User class
    """

    def __init__(self, database: Database) -> None:
        self.database = database


    def add(self, data: str) -> Optional[str]:
        return self.database.persist(data)


def builder(db_type: str) -> Database:
    _map = {
        "MYSQL": MySQLDatabase(),
        "PG": PGDatabase()
    }
    database = _map[db_type]
    database.connect()
    return database


def factory(db_type: str):
    database = builder(db_type=db_type)
    user = User(database=database)
    user.add("awesome data")


if __name__ == "__main__":
    factory("PG")