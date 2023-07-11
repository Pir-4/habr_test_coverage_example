import logging

import click
import uvicorn

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
def start_test_app():
    uvicorn.run(
        app='main:app',
        loop='uvloop',
        host='0.0.0.0'
    )


if __name__ == '__main__':
    logger.info('Run app')
    cli()
