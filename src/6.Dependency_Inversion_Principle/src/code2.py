from typing import Optional

class DIP:
    """
    Dependency Inversion Principle
    """

    def __init__(self) -> None:
        self.user = User()
        

    def main(self) -> None:
        self.user.add("awesome data")


class User:
    """
    User class
    """

    def __init__(self) -> None:
        # Connecting to the database
        self.database = MySQLDatabase()
        self.database.connect()


    def add(self, data: str) -> Optional[str]:
        return self.database.persist(data)


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


if __name__ == "__main__":
    obj = DIP()
    obj.main()