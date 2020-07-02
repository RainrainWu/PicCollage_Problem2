"""
tasks.env contains environment setup tasks description.
"""

from invoke import task


@task
def prod(ctx):
    """
    Setup environment with production dependencies.
    """
    ctx.run("poetry install --no-dev")


@task
def dev(ctx):
    """
    Setup environment with developing dependencies.
    """
    ctx.run("poetry install")
