from http.client import HTTPResponse

from sanic import Request, json

from app.handlers.base import Handler
from app.services.test_step.validators.payload import CreateTestStepPayload
from app.utils.route import route


class TestStepHandler(Handler):

    @route("/", methods=["POST"])
    def create_test_step(self, request: Request) -> HTTPResponse:
        payload = CreateTestStepPayload(**(request.json or {}))
        test_step = self._repository.create(payload.dict())

        return json(test_step.serialize())

    @route("/<id:str>", methods=["GET"])
    def get_test_step(self, request: Request, id: str) -> HTTPResponse:
        test_step = self._repository.find_by_id(id)
        return json(test_step.serialize())
