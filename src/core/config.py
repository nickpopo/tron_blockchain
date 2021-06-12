import os
from logging import config as logging_config

from .logger import LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging_config.dictConfig(LOGGING)

# Swagger settings.
PROJECT_NAME = "Tron Account Info"

# Redis settings
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT") or 6379)

CACHE_EXPIRE_IN_SECONDS = int(os.getenv("CACHE_EXPIRE_IN_SECONDS", 60))

# Tron settings
TRON_CLIENT_API_KEY = os.getenv(
    "TRON_CLIENT_API_KEY",
    "f92221d5-7056-4366-b96f-65d3662ec2d9",
)
TRON_CLIENT_NETWORK = os.getenv("TRON_CLIENT_NETWORK", "mainnet")
TRON_CLIENT_TIMEOUT = int(os.getenv("TRON_CLIENT_TIMEOUT", 20))
