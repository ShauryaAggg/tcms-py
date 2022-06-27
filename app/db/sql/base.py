from typing import Any

from sqlalchemy import Column, Integer, MetaData, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import session

from app.models.core.index import IndexModel


class SqlBaseMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['_model'] = getattr(
            attrs.get("Meta", object), "model", None)
        attrs['_table'] = getattr(
            attrs.get("Meta", object), "table", None)
        return super().__new__(cls, name, bases, attrs)


class SqlBaseRepository():
    def __new__(cls, db, *args, **kwargs):
        """
        Initialize the class
        """
        cls._db: session.Session = db

        metadata = MetaData(bind=cls._db.get_bind())
        cls._table: Table = Table(
            cls._table, metadata, autoload_with=cls._db.get_bind())

        config = getattr(cls._model, "Config", None)
        if config:
            cls._indexes = getattr(config, "indexes", IndexModel([]))

        return super().__new__(cls, *args, **kwargs)

    def __init_subclass__(cls) -> None:
        if not getattr(cls, "Meta", None):
            raise AttributeError("Must define Meta class")

        if not getattr(cls.Meta, "model", None):
            raise AttributeError("Must define Model")

        if not isinstance(cls.Meta.table, str):
            raise TypeError("table name must be a string")

    @classmethod
    def find_by_id(cls, id: Any) -> Any:
        result = cls._table.select().where(cls._table.c.id == id).execute().fetchone()
        return cls._model(**result)

    @classmethod
    def find(cls, filter: Any) -> Any:
        result = cls._table.select().where(**filter).execute().fetchall()
        return [cls._model(**item) for item in result]

    @classmethod
    def find_one(cls, filter: Any) -> Any:
        result = cls._table.select().where(**filter).execute().fetchone()
        return cls._model(**result)

    @classmethod
    def create(cls, item: Any) -> Any:
        result = cls._table.insert().values(**item).execute()
        item.update({"_id": result.inserted_id})
        return cls._model(**item)

    @ classmethod
    def update(cls, id: Any, item: Any) -> Any:
        result = cls._table.update().where(cls._table.c.id == id).values(**item).execute()
        return cls._model(**(result.raw_result))

    @ classmethod
    def delete(cls, id: Any) -> Any:
        result = cls._table.delete().where(cls._table.c.id == id).execute()
        return cls._model(**(result.raw_result))

    @classmethod
    def _migrate_model(cls):
        """
        Migrate the model
        """
