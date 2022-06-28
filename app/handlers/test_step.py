from http.client import HTTPResponse

from sanic import Request, json

from app.utils.route import route
from app.handlers.base import Handler
from app.services.test_step.validators.payload import CreateTestStepPayload, UpdateTestStepPayload


class TestStepHandler(Handler):
    """
    TestStep Handler class.
    """

    @route("/", methods=["POST"])
    def create_test_step(self, request: Request) -> HTTPResponse:
        payload = CreateTestStepPayload(**(request.json or {}))
        test_step = self._repository.create(payload.dict())

        return json(test_step.serialize())

    @route("/", methods=["GET"])
    def get_test_cases(self, request: Request) -> HTTPResponse:
        test_steps = self._repository.find({})
        return json([test_step.serialize() for test_step in test_steps])

    @route("/<id:str>", methods=["GET"])
    def get_test_step(self, request: Request, id: str) -> HTTPResponse:
        test_step = self._repository.find_by_id(id)
        return json(test_step.serialize())

    @route("/<id:str>", methods=["PUT"])
    def update_test_step(self, request: Request, id: str) -> HTTPResponse:
        payload = UpdateTestStepPayload(**(request.json or {}))
        test_step = self._repository.update(
            id, payload.dict(exclude_none=True, exclude_unset=True))
        return json(test_step.serialize())

    @route("/<id:str>", methods=["DELETE"])
    def delete_test_step(self, request: Request, id: str) -> HTTPResponse:
        test_step = self._repository.delete(id)
        return json(test_step.serialize())
