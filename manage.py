# !/usr/bin/env python3
import os

import click

from app import app
import pgen


try:
    import config
except ImportError:
    import example_config as config


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.secho('Running server for PGen', fg='green')

    app.secret_key = config.secret_key
    app.config['STATIC_FOLDER'] = config.static_path
    app.config['TEMPLATE_FOLDER'] = config.template_path

    app.run(debug=config.debug)


@cli.command()
@click.option('--login', prompt=True)
@click.password_option()
@click.option('--site', prompt=True)
@click.option('--length', '-l', default=10)
def gen(login, password, site, length):
    new_pass = pgen.gen_pass(
        login=login,
        password=password,
        site=site,
        secret_key=config.secret_key,
        length=length,
    )
    click.secho('Your new password: %s' % new_pass)


@cli.command()
def test():
    os.system(
        'nosetests --cover-package=pgen,app '
        '--cover-erase --with-coverage --with-doctest'
    )


if __name__ == '__main__':
    try:
        cli()
    except Exception as exc:
        if not str(exc):
            raise

        click.secho('ERROR: %s!' % exc, fg='red')
