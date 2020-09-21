from pathlib import Path
from cryptography.fernet import Fernet

class EncryptionManager:

    DEFAULT_KEY_FILE = Path.home() / '.shdb/secret.key'
    ENCODING = "UTF-8"

    def __init__(self, filename: Path = None):
        filename = filename or EncryptionManager.DEFAULT_KEY_FILE
        if not filename.exists():
            self.key = self.__generate_key(filename)
        else:
            self.key = self.__load_key(filename)

    def encrypt(self, value: str) -> bytes:
        encoded = value.encode(EncryptionManager.ENCODING)
        f = Fernet(self.key)
        encrypted = f.encrypt(encoded)
        return encrypted

    def decrypt(self, data: bytes) -> str:
        f = Fernet(self.key)
        decrypted = f.decrypt(data)
        return decrypted.decode(EncryptionManager.ENCODING)


    def __generate_key(self, filename: Path):
        if not filename.exists():
            filename.parent.mkdir(parents=True, exist_ok=True)
            key = Fernet.generate_key()
            with filename.open(mode='wb') as key_file:
                key_file.write(key)
        return key

    def __load_key(self, filename: Path):
        return filename.open(mode='r').read()
