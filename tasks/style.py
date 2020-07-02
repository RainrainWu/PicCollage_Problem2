"""
tasks.style contains coding style checking tasks description.
"""

from invoke import task

from shortener.config import (
    POETRY_PREFIX,
    MODULE_NAME,
)


@task
def pylint(ctx):
    """
    check style through pylint.
    """
    ctx.run('{PREFIX} pylint {MODULE}'.format(
        PREFIX=POETRY_PREFIX,
        MODULE=MODULE_NAME
    ))


@task
def flake8(ctx):
    """
    check style throug flake8.
    """
    ctx.run('{PREFIX} flake8'.format(
        PREFIX=POETRY_PREFIX
    ))


@task
def black(ctx):
    """
    fix style through black.
    """
    ctx.run("{PREFIX} black {MODULE}".format(
        PREFIX=POETRY_PREFIX,
        MODULE=MODULE_NAME
    ))
