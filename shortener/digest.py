"""
PicCollage_Problem2.shortener.digest is responsible for digsting payloads
within user requests.
"""


import re
import string
import random

import uuid

from shortener import database
from shortener.config import UNIT_TEST_FLAG, TAG_LENGTH_MINIMUM, TAG_LENGTH_MAXIMUM


def validate_tag(tag: str) -> bool:
    """
    validate_flag will check whether the tag is validate.

    Args:
        tag (str): tag to be validated.

    Returns:
        bool: Token is valid or not.
    """
    pattern = re.compile(
        r"^[A-Za-z0-9-]{"
        + str(TAG_LENGTH_MINIMUM)
        + r","
        + str(TAG_LENGTH_MAXIMUM)
        + r"}$"
    )
    return pattern.match(tag) is not None


def generate_flag(payload: object, /) -> str:
    """
    generate_flag will generate flag depends on payload. If 'tag' key
    exist, a prefix will be attached, otherwise a random string will
    be used.

    Args:
        payload (object): json object that contains payloads.

    Returns:
        str: generate flag.
    """
    flag = ""
    while (
        database.get_document(flag) is not None or flag == "" or flag == UNIT_TEST_FLAG
    ):
        letters = random.sample(string.ascii_letters, k=2)
        prefix = "".join(letters) + "-"
        flag = prefix + str(uuid.uuid4())[:8]
        if "tag" in payload:
            flag = prefix + payload["tag"]
    return flag
