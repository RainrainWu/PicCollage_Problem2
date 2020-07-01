"""
PicCollage_Problem2.shortener.digest is responsible for digsting payloads
within user requests.
"""


import re, string, random

import uuid

from shortener import database


def validate_tag(tag: str) -> bool:
    """
    validate_flag will check whether the tag is validate.

    Args:
        tag (str): tag to be validated.

    Returns:
        bool: Token is valid or not.
    """
    pattern = re.compile(r"^[A-Za-z0-9-]*$")
    return pattern.match(tag)


def generate_flag(payload: object, /) -> str:
    """
    generate_flag will generate flag depends on payload. If 'tag' key
    exist, a prefix will be attached, or a random string will be used.

    Args:
        payload (object): json object that contains payloads.

    Returns:
        str: generate flag.
    """
    flag = ""
    while database.check_flag(flag) or flag == "":
        letters = random.sample(string.ascii_letters, k=2)
        prefix = "".join(letters) + "-"
        flag = prefix + str(uuid.uuid4())[:8]
        if "tag" in payload:
            flag = prefix + payload["tag"]
    return flag
