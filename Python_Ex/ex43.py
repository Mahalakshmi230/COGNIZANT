import configparser

class Config:
    def __init__(self, file_name):
        self.file_name = file_name
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.file_name)
        return self.config


class DatabaseConfig(Config):
    def get_db_settings(self):
        config = self.load()

        if "database" not in config:
            return "Database section missing"

        db = config["database"]

        required_keys = ["host", "user", "password"]

        for key in required_keys:
            if key not in db:
                return f"Missing key: {key}"

        return {
            "host": db["host"],
            "user": db["user"],
            "password": db["password"]
        }


def main():
    obj = DatabaseConfig("db.ini")
    print(obj.get_db_settings())


main()