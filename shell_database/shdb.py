import click
import logging
from sqlitedict import SqliteDict


@click.group()
@click.option('-v', '--verbose', help='Enable verbose output', default=False, is_flag=True)
@click.option('-d', '--debug', help='Enable debug output', default=False, is_flag=True)
def cli(verbose: bool = False, debug: bool = False):
    if verbose:
        logging.getLogger().setLevel(level='INFO')
    if debug:
        logging.getLogger().setLevel(level='DEBUG')
        logging.debug('debug output enabled')


@cli.command()
@click.argument('key')
@click.argument('value')
def add(key, value):
    with SqliteDict('./shdb.sqlite', autocommit=True) as db:
        db[key] = value


@cli.command()
@click.argument('key')
def get(key):
    with SqliteDict('./shdb.sqlite', autocommit=True) as db:
        print(db[key])


if __name__ == '__main__':
    cli()