"""
PicCollage_Problem2.shortener.test_database is responsible for unittesting
the module PicCollage_Problem2.shortener.database.
"""

import pytest

from shortener import database
from shortener.config import TEST_FLAG


@pytest.mark.parametrize(
    "flag, source, expected",
    [
        pytest.param(TEST_FLAG, "domain", True),
        pytest.param(TEST_FLAG, "domain", False),
    ],
)
def test_register_flag(*, flag: str, source: str, expected: bool):
    """
    test_register_flag was used to test register_flag function.

    Args:
        flag (str): flag to be register.
        source (str): source url mapping with flag.
        expected (bool): result is empty string or not.
    """
    output = database.register_flag(flag, source)
    assert (output != "") == expected


@pytest.mark.parametrize(
    "flag, expected",
    [
        pytest.param(TEST_FLAG, True),
        pytest.param("xc_ttf", False),
    ],
)
def test_get_document(*, flag: str, expected: bool):
    """
    test_get_document was used to test get_document function.

    Args:
        flag (str): flag of target document.
        expected (bool): result is empty dict or not.
    """
    output = database.get_document(flag)
    assert (output is not None) == expected


@pytest.mark.parametrize(
    "flag, expected",
    [
        pytest.param(TEST_FLAG, True),
        pytest.param("xc_ttf", False),
    ],
)
def test_get_source(*, flag: str, expected: bool):
    """
    test_get_source was used to test get_source function.

    Args:
        flag (str): flag of target source.
        expected (bool): result is empty string or not.
    """
    output = database.get_source(flag)
    assert (output != "") == expected


@pytest.mark.parametrize(
    "flag, expected",
    [
        pytest.param(TEST_FLAG, True),
        pytest.param("xc_ttf", False),
    ],
)
def test_get_metrix(*, flag: str, expected: bool):
    """
    test_get_metrix was used to test get_metrix function.

    Args:
        flag (str): flag of target metrix.
        expected (bool): result is empty string or not.
    """
    output = database.get_metrix(flag)
    assert (output != {}) == expected


@pytest.mark.parametrize(
    "flag, expected",
    [
        pytest.param(TEST_FLAG, True),
        pytest.param("xc_ttf", False),
    ],
)
def test_get_mapping(*, flag: str, expected: bool):
    """
    test_get_mapping was used to test get_mapping function.

    Args:
        flag (str): flag to be checked.
        expected (bool): flag is exist in mapping or not.
    """
    mapping = database.get_mapping()
    assert (flag in mapping) == expected


@pytest.mark.parametrize(
    "flag, count, expected",
    [
        pytest.param(TEST_FLAG, 1, 1),
        pytest.param(TEST_FLAG, 2, 3),
        pytest.param("xc_ttf", 1, -1),
    ],
)
def test_add_visited_times(*, flag: str, count: int, expected: int):
    """
    test_add_visited_times was used to test add_visited_times function.

    Args:
        flag (str): flag to be visited.
        count (int): how many times to visit the flag.
        expected (int): result of visited_times after operation.
    """
    result = database.add_visited_times(flag, count)
    assert result == expected


@pytest.mark.parametrize(
    "flag, expected",
    [
        pytest.param(TEST_FLAG, True),
        pytest.param("xc_ttf", False),
    ],
)
def test_delete_document(*, flag: str, expected: bool):
    """
    test_delete_document was used to test delete_document function.

    Args:
        flag (str): flag of target document.
        expected (bool): delete successfully or nott.
    """
    output = database.delete_document(flag)
    assert output == expected
