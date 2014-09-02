# !/usr/bin/env python3
import os

import click

import pgen


@click.group()
def cli():
    pass


@cli.command()
@click.option('--login', prompt=True)
@click.option('--site', prompt=True)
@click.password_option()
@click.option('--length', '-l', default=10)
def gen(login, site, password, length):
    click.echo('Your key: %s' % pgen.gen_pass(password, login, site, length))


@cli.command()
def test():
    os.system(
        'nosetests --cover-package=pgen,app '
        '--cover-erase --with-coverage --with-doctest'
    )


if __name__ == '__main__':
    cli()
