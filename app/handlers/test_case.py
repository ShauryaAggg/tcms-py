from http.client import HTTPResponse

from sanic import Request, json
from app.handlers.base import Handler
from app.services.test_case.validators.payload import CreateTestCasePayload

from app.utils.route import route


class TestCaseHandler(Handler):
    @route("/", methods=["POST"])
    def create_test_case(self, request: Request) -> HTTPResponse:
        payload = CreateTestCasePayload(**(request.json or {}))
        test_case = self._repository.create(payload.dict())

        return json(test_case.serialize())

    @route("/<id:str>", methods=["GET"])
    def get_test_case(self, request: Request, id: str) -> HTTPResponse:
        test_case = self._repository.find_by_id(id)
        return json(test_case.serialize())
