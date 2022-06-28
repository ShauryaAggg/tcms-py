import re
from typing import Any

from pymongo import ReturnDocument, collection, database
from bson import ObjectId

from app.models.core.index import IndexModel


class MongoBaseMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        attrs['_model'] = getattr(
            attrs.get("Meta", object), "model", None)
        attrs['_collection'] = getattr(
            attrs.get("Meta", object), "collection", None)

        return super().__new__(cls, name, bases, attrs, **kwargs)


class MongoBaseRepository(metaclass=MongoBaseMeta):
    """
    Base Repository for MongoDB
    """

    def __new__(cls, db, *args, **kwargs):
        """
        Initialize the class

        :param db: MongoDB database
        """
        cls._db: database.Database = db
        cls._collection: collection.Collection = cls._db.get_collection(
            cls._collection)

        config = getattr(cls._model, "Config", None)
        if config:
            cls._indexes = getattr(config, "indexes", [])

        cls._init_collection()

        return super().__new__(cls, *args, **kwargs)

    def __init_subclass__(cls) -> None:
        if not getattr(cls, "Meta", None):
            raise AttributeError("Must define Meta class")

        if not getattr(cls.Meta, "model", None):
            raise AttributeError("Must define Model")

        if not isinstance(cls.Meta.collection, str):
            raise TypeError("collection name must be a string")

    @classmethod
    def find_by_id(cls, id: Any) -> Any:
        result = cls._collection.find_one({"_id": ObjectId(id)})
        if not result:
            raise ValueError("No document found with id: {}".format(id))
        return cls._model(**result)

    @classmethod
    def find(cls, filter: Any) -> Any:
        result = cls._collection.find(filter)
        return [cls._model(**item) for item in result]

    @classmethod
    def find_one(cls, filter: Any) -> Any:
        result = cls._collection.find_one(filter)
        return cls._model(**result)

    @classmethod
    def create(cls, item: Any) -> Any:
        result = cls._collection.insert_one(item)
        item.update({"_id": str(result.inserted_id)})
        return cls._model(**item)

    @ classmethod
    def update(cls, id: Any, item: Any) -> Any:
        result = cls._collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": item}, return_document=ReturnDocument.AFTER)
        if not result:
            raise ValueError("No item found with id: {}".format(id))
        return cls._model(**(result))

    @ classmethod
    def delete(cls, id: Any) -> Any:
        result = cls._collection.find_one_and_delete({"_id": ObjectId(id)})
        if not result:
            raise ValueError("No item found with id: {}".format(id))
        return cls._model(**(result))

    @classmethod
    def _init_collection(cls):
        """
        Initialize the collection and set the indexes for the collection
        """
        for index in cls._indexes:
            cls._collection.create_index(
                index.keys, unique=index.unique, sparse=index.sparse
            )
