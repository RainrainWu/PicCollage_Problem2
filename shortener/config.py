"""
PicCollage_Problem2.shortener.config store the configurations of the service.
"""

LOG_DIRECTORY = "logs/"
LOG_ROTATION = "500 MB"
LOG_RETENTION = "10 days"

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DATABASE = "shortener"
MONGO_COLLECTION = "mapping"

UNIT_TEST_FLAG = "xC-ttf-"
FVT_SOURCE_1 = "https://www.python.org/"
FVT_SOURCE_2 = "https://golang.org/"
FVT_SOURCE_3 = "https://www.rust-lang.org/"
FVT_VALID_TAG = "go-lang"
FVT_INVALID_TAG = "rust!"
