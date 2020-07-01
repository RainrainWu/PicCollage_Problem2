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