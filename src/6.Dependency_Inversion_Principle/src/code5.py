from typing import Optional

class MySQLDatabase:
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


class PGDatabase:
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

    def __init__(self, database: MySQLDatabase) -> None:
        self.database = database


    def add(self, data: str) -> Optional[str]:
        return self.database.persist(data)


def factory():
    # database = MySQLDatabase()
    # database.connect()
    database = PGDatabase()
    database.connect()
    user = User(database=database)
    user.add("awesome data")


if __name__ == "__main__":
    factory()