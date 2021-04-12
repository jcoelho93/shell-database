from pathlib import Path
from fuzzywuzzy import process
from sqlitedict import SqliteDict


class DataStore:

    DEFAULT_FILE = Path.home() / '.shdb/store.sqlite'

    def __init__(self, filename: Path = None):
        self.store = filename or DataStore.DEFAULT_FILE
        if not self.store.parent.exists():
            self.store.parent.mkdir(parents=True, exist_ok=True)
        sqlite = SqliteDict(self.store)
        sqlite.close()
        self.store.chmod(0o600)

    def add(self, key, value):
        with SqliteDict(str(self.store), autocommit=True) as db:
            db[key] = value

    def remove(self, key):
        with SqliteDict(str(self.store), autocommit=True) as db:
            try:
                del db[key]
            except KeyError:
                pass

    def get(self, key) -> str:
        with SqliteDict(str(self.store), flag='r', autocommit=True) as db:
            try:
                return db[key]
            except KeyError:
                return None

    def list_keys(self, pattern: str = None):
        with SqliteDict(str(self.store), flag='r', autocommit=True) as db:
            keys = [k for k, _ in db.items()]
        if pattern:
            keys = process.extract(pattern, keys)
            return [k for k, rating in keys if rating > 50]
        return keys
