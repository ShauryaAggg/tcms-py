from http.client import HTTPResponse

from sanic import Request, json
from app.db.core.repository import Repository
from app.services.test_case.validators.payload import CreateTestCasePayload

from app.utils.route import route


class TestCaseHandler:

    def __init__(self, repository: Repository) -> None:
        self._repository: Repository = repository

    @route("/", methods=["POST"])
    def create_test_case(self, request: Request) -> HTTPResponse:
        payload = CreateTestCasePayload(**(request.json or {}))
        test_case = self._repository.create(payload.dict())

        return json(test_case.dict())

    @route("/<layer_id:str>", methods=["GET"])
    def get_test_case(self, request: Request, layer_id: str) -> HTTPResponse:
        test_case = self._repository.find_by_id(layer_id)
        return json(test_case.dict())
