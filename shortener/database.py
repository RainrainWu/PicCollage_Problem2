"""
PicCollage_Problem2.shortener.database provides methods for operating data
storage system.
"""


records = {
    "rain": {
        "source": "https://github.com/RainrainWu",
        "metrix": {
            "visited_times": 30
        },
    },
}


def check_flag(flag: str, /) -> bool:
    """
    check_flag will check whether the flag already registered.

    Args:
        flag (str): flag to be checked.

    Returns:
        bool: True if the flag already existed, else False.
    """
    return flag in records


def register_flag(flag: str, source: str, /) -> bool:
    """
    register_flag register new flag information into database.

    Args:
        flag (str): flag to be registered.
        source (str): source url for the flag.

    Returns:
        bool: True if register successfully, else False.
    """
    if check_flag(flag):
        return False
    records[flag] = {}
    records[flag]["source"] = source
    return True


def get_source(flag: str, /) -> str:
    """
    get_source obtain the source url for the flag.

    Args:
        flag (str): target flag.

    Returns:
        str: source url for the flag.
    """
    if not check_flag(flag):
        return ""
    return records[flag]["source"]


def get_metrix(flag: str, /) -> dict:
    """
    get_metrix obtain the metrix for the flag.

    Args:
        flag (str): target flag.

    Returns:
        dict: json metrix for the flag.
    """
    if not check_flag(flag):
        return {}
    return records[flag]["metrix"]


def get_mapping() -> dict:
    """
    get_mapping obtains all mapping between flag and source url.

    Returns:
        dict: mapping relations.
    """
    mapping = {}
    for i in records:
        mapping[i] = records[i]["source"]
    return mapping
