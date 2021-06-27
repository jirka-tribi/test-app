from .database import Database


class App:
    def __init__(
        self,
        test_db: Database,
    ):
        self.test_db = test_db

    def test_status(self):
        return 200
