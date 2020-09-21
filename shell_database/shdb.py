import click
import logging
from shell_database.store.store import DataStore


_data_store = DataStore()


@click.group()
@click.option('-v', '--verbose', help='Enable verbose output', default=False, is_flag=True)
@click.option('-d', '--debug', help='Enable debug output', default=False, is_flag=True)
def cli(verbose: bool = False, debug: bool = False):
    if verbose:
        logging.getLogger().setLevel(level='INFO')
    if debug:
        logging.getLogger().setLevel(level='DEBUG')
        logging.debug('debug output enabled')


@cli.command(help="Add a new key value pair")
@click.argument('key')
@click.argument('value')
def add(key, value):
    _data_store.add(key, value)


@cli.command(help="Get the value from a key")
@click.argument('key')
def get(key):
    value = _data_store.get(key)
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