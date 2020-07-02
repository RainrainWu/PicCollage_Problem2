"""
tasks.env contains environment setup tasks description.
"""

from invoke import task


@task
def init_prod(ctx):
    """
    Setup environment with production dependencies.
    """
    ctx.run("poetry install --no-dev")


@task
def init_dev(ctx):
    """
    Setup environment with developing dependencies.
    """
    ctx.run("pipenv install")
