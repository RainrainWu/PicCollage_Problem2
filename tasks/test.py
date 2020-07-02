"""
tasks.test contains test tasks description.
"""

from invoke import task

from shortener.config import POETRY_PREFIX


@task
def unit(ctx):
    """
    run unit test through pytest.
    """
    ctx.run("{PREFIX} pytest -m \"unit\"".format(
        PREFIX=POETRY_PREFIX
    ))


@task
def fvt(ctx):
    """
    run fvt through pytest.
    """
    ctx.run("{PREFIX} pytest -m \"fvt\"".format(
        PREFIX=POETRY_PREFIX
    ))
