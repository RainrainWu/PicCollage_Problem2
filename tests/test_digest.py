"""
PicCollage_Problem2.shortener.test_digest is responsible for unittesting
the module PicCollage_Problem2.shortener.digest.
"""

import re

import pytest

from shortener import digest


@pytest.mark.parametrize(
    "tag, expected",
    [
        pytest.param("", False),
        pytest.param("a", True),
        pytest.param("%", False),
        pytest.param("12n-c4k", True),
        pytest.param("12n?c4k", False),
        pytest.param("-------------------------------------", True),
        pytest.param("                                     ", False),
    ],
)
def test_validate_tag(*, tag: str, expected: bool):
    """
    test_validate_tag was used to test validate_tag function.

    Args:
        tag (str): tag to be validated.
        expected (bool): expected validate result.
    """
    assert digest.validate_tag(tag) == expected


@pytest.mark.parametrize(
    "payload",
    [
        pytest.param({"source": "domain"}),
        pytest.param({"tag": "rain", "source": "domain"}),
        pytest.param({"tag": "pic-collage", "source": "domain"}),
        pytest.param({"tag": "-python-is-the-best-", "source": "domain"}),
    ],
)
def test_generate_flag(*, payload: object):
    """
    test_validate_tag was used to test generate_flag function.

    Args:
        payload (object): mock user submit payload.
    """
    if "tag" in payload:
        pattern = re.compile(r"^[A-Za-z]{2}-" + payload["tag"] + r"$")
    else:
        pattern = re.compile(r"^[A-Za-z]{2}-[A-Za-z0-9]{8}$")
    assert pattern.match(digest.generate_flag(payload)) is not None
