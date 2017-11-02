# -*- coding: utf-8 -*-

"""Console script for mypackage."""

import click


@click.command()
def main(args=None):
    """Console script for mypackage."""
    click.echo("Replace this message by putting your code into "
               "mypackage.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
