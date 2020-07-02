"""
tasks is the namespace manager for invoke tasks.
"""

from invoke import Collection

from tasks import (
    env,
    style,
    test
)


namespace = Collection()
namespace.add_collection(env)
namespace.add_collection(style)
namespace.add_collection(test)
