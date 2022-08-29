class IoC:
    """
    Inversion of Control class
    # NO container
    # NO dependency injection
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


    def add(self, data: str) -> None:
        return self.database.persist(data)


class MySQLDatabase:
    """
    MySQL database implementation class
    """

    # Imagine that here we have some kind of openning the actual real database connection


    def persist(self, data: str) -> str:
        print(f"MySQL has persisted: {data}")
        return f"MySQL has persisted: {data}"


if __name__ == "__main__":
    obj = IoC()
    obj.main()