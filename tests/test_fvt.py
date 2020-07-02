"""
PicCollage_Problem2.shortener.test_fvt implement user story for functional
verification tests.

User story outline:
    1. Visit landing page.
    2. Submit payload without tag for shortener service.
    3. Submit payload with valid tag for shortener service.
    4. Submit payload with invalid tag for shortener service.
    5. Visit shorted url to check if redirection is working.
    6. Scrape metrix to check if visited_times increased.
    7. Visit dashboard to check if all mapping are exist.
    8. Delete all registerd shortened source url.
"""

import re

import requests
import pytest

from shortener.config import (
    FVT_SOURCE_1,
    FVT_SOURCE_2,
    FVT_SOURCE_3,
    FVT_VALID_TAG,
    FVT_INVALID_TAG,
    FVT_INVALID_FLAG,
)


def submit_payload(*, tag: str = "", source: str = "https://google.com") -> object:
    """
    submit_payload will submit a payload for registeration.

    Args:
        tag (str): tag for flag generation.
        source (str): source url to redirect.

    Returns:
        object: response object.
    """
    if tag == "":
        resp = requests.post(
            "http://localhost:5000/user/submit", json={"source": source}
        )
    else:
        resp = requests.post(
            "http://localhost:5000/user/submit", json={"tag": tag, "source": source}
        )
    return resp


def delete_flag(*, flag: str) -> object:
    """
    delete_flag will delete the corresponding flag.

    Args:
        flag (str): flag to delete.

    Returns:
        object: response object.
    """
    resp = requests.post("http://localhost:5000/admin/delete", json={"flag": flag})
    return resp


@pytest.mark.fvt
def test_visit_landing_page():
    """
    visit_landing_page will vesit landing page of shortener service.
    """
    resp = requests.get("http://localhost:5000")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World"}


@pytest.mark.fvt
def test_submit_without_tag():
    """
    test_submit_without_tag will submit a payload without tag.
    """
    resp = submit_payload(source=FVT_SOURCE_1)
    assert resp.status_code == 200

    pattern = re.compile(r"^[A-Za-z]{2}-[A-Za-z0-9]{8}$")
    test_submit_without_tag.flag = resp.json()["flag"]
    assert pattern.match(test_submit_without_tag.flag) is not None


@pytest.mark.fvt
def test_submit_with_valid_tag():
    """
    test_submit_with_valid_tag will submit a payload with a valid tag.
    """
    resp = submit_payload(tag=FVT_VALID_TAG, source=FVT_SOURCE_2)
    assert resp.status_code == 200

    pattern = re.compile(r"^[A-Za-z]{2}-" + FVT_VALID_TAG + r"$")
    test_submit_with_valid_tag.flag = resp.json()["flag"]
    assert pattern.match(test_submit_with_valid_tag.flag) is not None


@pytest.mark.fvt
def test_submit_with_invalid_tag():
    """
    test_submit_with_valid_tag will submit a payload with a invalid tag.
    """
    resp = submit_payload(tag=FVT_INVALID_TAG, source=FVT_SOURCE_3)
    assert resp.status_code == 400
    assert resp.json() == {"error": "Invalid tag"}


@pytest.mark.fvt
def test_check_redirection():
    """
    test_check_redirection will test the redirect of shorted url.
    """
    resp = requests.get("http://localhost:5000/" + test_submit_without_tag.flag)
    assert resp.status_code == 200
    assert resp.url == FVT_SOURCE_1

    resp = requests.get("http://localhost:5000/" + test_submit_with_valid_tag.flag)
    assert resp.status_code == 200
    assert resp.url == FVT_SOURCE_2

    resp = requests.get("http://localhost:5000/" + FVT_INVALID_FLAG)
    assert resp.status_code == 400
    assert resp.json() == {"error": "Flag not found"}


@pytest.mark.fvt
def test_check_metrix():
    """
    test_check_metrix will check the metrix changes of flag.
    """
    resp = requests.get(
        "http://localhost:5000/user/metrix/" + test_submit_without_tag.flag
    )
    assert resp.status_code == 200
    assert resp.json()["visited_times"] == 1

    resp = requests.get(
        "http://localhost:5000/user/metrix/" + test_submit_with_valid_tag.flag
    )
    assert resp.status_code == 200
    assert resp.json()["visited_times"] == 1

    resp = requests.get("http://localhost:5000/user/metrix/" + FVT_INVALID_FLAG)
    assert resp.status_code == 400
    assert resp.json() == {"error": "Flag not found"}


@pytest.mark.fvt
def test_check_dashboard():
    """
    test_check_dashboard will check the whether flags are on dashboard.
    """
    resp = requests.get("http://localhost:5000/admin/dashboard")
    assert test_submit_without_tag.flag in resp.json()
    assert test_submit_with_valid_tag.flag in resp.json()
    assert FVT_INVALID_FLAG not in resp.json()


@pytest.mark.fvt
def test_delete_all():
    """
    test_submit_without_tag will submit a payload without tag.
    """
    resp = delete_flag(flag=test_submit_without_tag.flag)
    assert resp.status_code == 200
    assert resp.json() == {"message": "success"}

    resp = delete_flag(flag=test_submit_with_valid_tag.flag)
    assert resp.status_code == 200
    assert resp.json() == {"message": "success"}

    resp = delete_flag(flag=FVT_INVALID_FLAG)
    assert resp.status_code == 400
    assert resp.json() == {"error": "Flag not found"}
