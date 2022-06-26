from enum import Enum
from torpedo.common_utils import CONFIG

config = CONFIG.config


class MongoConfigs(Enum):
    MONGO = "MONGO"
    MONGO_TEST = "MONGO_TEST"
