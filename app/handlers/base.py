from typing import TYPE_CHECKING
from http.client import HTTPResponse

from sanic import Request, json
from sanic.exceptions import SanicException

from app.models.base import Base
from app.db.core.repository import Repository
from app.utils import payload
from app.utils.route import route


class HandlerMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        meta = attrs.get('Meta', object)
        attrs['_repository'] = getattr(meta, 'repository', object)
        model = getattr(
            getattr(attrs['_repository'], 'Meta', object), 'model', Base)

        attrs['_create_payload'] = getattr(meta, 'create_payload',
                                           payload.get_create_payload(model))
        attrs['_update_payload'] = getattr(meta, 'update_payload',
                                           payload.get_upload_payload(model))

        return super().__new__(cls, name, bases, attrs, **kwargs)


class Handler(metaclass=HandlerMeta):
    """
    Base handler for all handlers.
    """
    if TYPE_CHECKING:
        _repository: Repository = None
        _create_payload: Base = None
        _update_payload: Base = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init_subclass__(cls) -> None:
        if not getattr(cls, "Meta", None):
            raise AttributeError("Must define Meta class")

    @route("/", methods=["POST"])
    def create(self, request: Request) -> HTTPResponse:
        payload = self._create_payload(**(request.json or {}))
        object = self._repository.create(payload.dict())

        return json(object.serialize())

    @route("/<id:str>", methods=["GET"])
    def get(self, request: Request, id: str) -> HTTPResponse:
        try:
            object = self._repository.find_by_id(id)
        except Exception as e:
            raise SanicException(e)
        return json(object.serialize())

    @route("/<id:str>", methods=["PATCH"])
    def update(self, request: Request, id: str) -> HTTPResponse:
        payload = self._update_payload(**(request.json or {}))
        print(payload.dict(exclude_unset=True))
        object = self._repository.update(
            id, payload.dict(exclude_none=True, exclude_unset=True))
        return json(object.serialize())

    @ route("/<id:str>", methods=["DELETE"])
    def delete(self, request: Request, id: str) -> HTTPResponse:
        object = self._repository.delete(id)
        return json(object.serialize())
