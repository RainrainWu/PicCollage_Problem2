"""
PicCollage_Problem2.shortener.database provides methods for operating data
storage system.
"""

from bson.objectid import ObjectId

from loguru import logger
from pymongo import MongoClient
from pymongo.errors import (
    ConnectionFailure,
    PyMongoError,
)

from shortener.config import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_DATABASE,
    MONGO_COLLECTION,
)


try:
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    records = client[MONGO_DATABASE][MONGO_COLLECTION]
except ConnectionFailure as err:
    logger.error("Could not connect to mongodb: ", err)


def get_document(flag: str, /) -> bool:
    """
    get_document will get the document with specified flag.

    Args:
        flag (str): flag to be checked.

    Returns:
        bool: True if the flag already existed, else False.
    """
    try:
        document = records.find_one({"flag": flag})
    except PyMongoError as err:
        logger.error("Failed to obtain document: ", err)

    return document


def register_flag(flag: str, source: str, /) -> str:
    """
    register_flag register new flag information into database.

    Args:
        flag (str): flag to be registered.
        source (str): source url for the flag.

    Returns:
        bool: True if register successfully, else False.
    """
    if get_document(flag) is not None:
        return False
    post = {
        "flag": flag,
        "source": source,
        "metrix": {
            "visited_times": 0,
        },
    }
    try:
        post_id = records.insert_one(post).inserted_id
        return str(post_id)
    except PyMongoError as err:
        logger.error("Failed to insert data: ", err)
        return ""


def get_source(flag: str, /) -> str:
    """
    get_source obtain the source url for the flag.

    Args:
        flag (str): target flag.

    Returns:
        str: source url for the flag.
    """
    content = get_document(flag)
    if content is None:
        return ""
    return content["source"]


def get_metrix(flag: str, /) -> dict:
    """
    get_metrix obtain the metrix for the flag.

    Args:
        flag (str): target flag.

    Returns:
        dict: json metrix for the flag.
    """
    document = get_document(flag)
    if document is None:
        return {}
    return document["metrix"]


def get_mapping(size: int = 10) -> dict:
    """
    get_mapping obtains all mapping between flag and source url.

    Returns:
        dict: mapping relations.
    """
    mapping = {}
    for document in records.find()[:size]:
        mapping[document["flag"]] = document["source"]
    return mapping


def add_visited_times(flag: str, count: int = 1, /) -> bool:
    """
    add_visited_time increase the visited times of the flag.

    Args:
        flag (str): flag that visited by users.
        count (int): visited times increase count.

    Returns:
        bool: whether operation is successful.
    """
    document = get_document(flag)
    if document is None:
        return False

    try:
        records.update_one(
            {"flag": flag},
            {"$inc": {"metrix.visited_times": count}}
        )
    except PyMongoError as err:
        print("Failed to update metrix: ", err)

    return True


# print(get_mapping())
# register_flag("TX-rain", "github.com/RainrainWu")
# print(get_mapping())
# print(get_document("TX-rain"))
# add_visited_times("TX-rain")
# print(get_document("TX-rain"))
# records.delete_one({"flag": "TX-rain"})
# print(get_mapping())
