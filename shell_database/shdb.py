import click
import logging
from shell_database.store.store import DataStore
from shell_database.store.encryption import EncryptionManager


_data_store = None
_encryption_manager = None


def setup():
    global _data_store, _encryption_manager
    _data_store = DataStore()
    _encryption_manager = EncryptionManager()


@click.group()
@click.option('-v', '--verbose', help='Enable verbose output', default=False, is_flag=True)
@click.option('-d', '--debug', help='Enable debug output', default=False, is_flag=True)
def cli(verbose: bool = False, debug: bool = False):
    if verbose:
        logging.getLogger().setLevel(level='INFO')
    if debug:
        logging.getLogger().setLevel(level='DEBUG')
        logging.debug('debug output enabled')
    setup()


@cli.command(help="Add a new key value pair")
@click.argument('key')
@click.argument('value')
@click.option('-e', '--encrypt', help="Encrypt the value before storing it", is_flag=True, required=False)
def add(key, value, encrypt: bool):
    if encrypt:
        value = _encryption_manager.encrypt(value)
    _data_store.add(key, value)


@cli.command(help="Get the value from a key")
@click.argument('key')
@click.option('-d', '--decrypt', help="Decrypt the value stored", is_flag=True, required=False)
def get(key, decrypt):
    value = _data_store.get(key)
    if decrypt and isinstance(value, bytes):
        value = _encryption_manager.decrypt(value)
    if value:
        print(value)


@cli.command('list', help="List the stored keys")
@click.argument('pattern', required=False)
@click.option('-c', '--count', help="Counts the number of keys found", required=False, is_flag=True)
def list_keys(pattern: str = None, count: bool = False):
    keys = _data_store.list_keys(pattern)
    if count:
        print(len(keys))
    for key in keys:
        print(key)


if __name__ == '__main__':
    cli()
