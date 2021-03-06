"""
PicCollage_Problem2.shortener.config store the configurations of the service.
"""

# tag configurations
TAG_LENGTH_MINIMUM = 1
TAG_LENGTH_MAXIMUM = 16

# loguru configurations
LOG_DIRECTORY = "logs/"
LOG_ROTATION = "500 MB"
LOG_RETENTION = "10 days"

# mongodb configurations
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DATABASE = "shortener"
MONGO_COLLECTION = "mapping"

# unit test configurations
UNIT_TEST_FLAG = "xC-ttf-"

# functional verification test configurations
FVT_SOURCE_1 = "https://www.python.org/"
FVT_SOURCE_2 = "https://golang.org/"
FVT_SOURCE_3 = "https://www.rust-lang.org/"
FVT_VALID_TAG = "go-lang"
FVT_INVALID_TAG_1 = "rust!"
FVT_INVALID_TAG_2 = "rustrustrustrustrust"
FVT_INVALID_FLAG = "12-abcd"

# invoke tasks configurations
POETRY_PREFIX = "poetry run "
MODULE_NAME = "shortener tests"
