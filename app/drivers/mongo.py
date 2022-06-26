from typing import Dict

import uvloop
from sanic import app
from logging import Logger
from app.constants.configs import MongoConfigs
from app.db.mongo.mongo_store import MongoStore
from app.db.mongo import repositories

from app.db import repositories


class MongoDriver:
    logger = Logger(__name__)

    @classmethod
    async def _register(cls, app_: app.Sanic, **config):
        """
        Helper method for initializing the beanie client
        :param app_:
        :param config:
        :return:
        """
        store = cls.get_client(**config)
        cls.logger.info("Connected to database successfully!")
        app_.config["db"] = store.database
        app_.config["repositories"] = store.repositories
        repositories.update(store.repositories)

    @classmethod
    async def register_db(
        cls, app_: app.Sanic, loop: uvloop, config_name=MongoConfigs.MONGO.value
    ):
        """
        Wrapper for main DB registration
        :param app:
        :param loop:
        :return:
        """
        # pylint: disable=unused-argument
        config = cls.get_mongo_config(app_, config_name)
        cls.logger.info("connecting to mongo database..")
        await cls._register(app_, **config)

    @staticmethod
    def get_client(**config) -> MongoStore:
        """
        getting motor client object
        :param config:
        :return:
        """
        connection_uri = (
            f"mongodb://{config['USER']}:{config['PASS']}"
            f"@{''.join(config['HOSTS'])}/{config['DB_NAME']}"
        )
        client = MongoStore(connection_uri, repositories)
        return client

    @staticmethod
    def get_mongo_config(app_: app, config_name) -> Dict:
        """
        picking up mongo config from the config object
        :param app_:
        :param config_name:
        :return:
        """

        assert (
            config_name in app_.config
        ), f"'{config_name}' config not found in the config.json"
        return app_.config[config_name]
