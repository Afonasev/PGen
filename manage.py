#! /usr/bin/env python3
import os

import click

import pgen


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.secho('Running server for PGen', fg='green')
    pgen.app.run()


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
        secret_key=pgen.app.secret_key,
        length=length,
    )
    click.secho('Your new password: %s' % new_pass)


@cli.command()
def test():
    os.system(
        'nosetests --cover-package=pgen '
        '--cover-erase --with-coverage --with-doctest'
    )


if __name__ == '__main__':
    cli()
