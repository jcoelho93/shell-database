from pathlib import Path
from fuzzywuzzy import process
from sqlitedict import SqliteDict


class DataStore:

    DEFAULT_FILE = Path.home() / '.shdb/store.sqlite'

    def __init__(self, filename: Path = None):
        self.store = filename or DataStore.DEFAULT_FILE
        if not self.store.parent.exists():
            self.store.parent.mkdir(parents=True, exist_ok=True)
        self.store = str(self.store)

    def add(self, key, value):
        with SqliteDict(self.store, autocommit=True) as db:
            db[key] = value

    def get(self, key):
        with SqliteDict(self.store, autocommit=True) as db:
            return db[key]

    def list_keys(self, pattern: str = None):
        with SqliteDict(self.store, autocommit=True) as db:
            keys = [k for k,_ in db.items()]
        if pattern:
            keys = process.extract(pattern, keys)
            return [k for k,rating in keys if rating > 50]
        return keys