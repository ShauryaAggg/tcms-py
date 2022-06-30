from http.client import HTTPResponse

from sanic import Request, json
from sanic.exceptions import SanicException
from app.handlers.base import Handler
from app.services.test_suite.validators.payload import CreateTestSuitePayload, UpdateTestSuitePayload

from app.utils.route import route


class TestSuiteHandler(Handler):
    """
    TestSuite Handler class.
    """

    @route("/", methods=["POST"])
    def create_test_case(self, request: Request) -> HTTPResponse:
        payload = CreateTestSuitePayload(**(request.json or {}))
        test_case = self._repository.create(payload.dict())

        return json(test_case.serialize())

    @route("/", methods=["GET"])
    def get_test_cases(self, request: Request) -> HTTPResponse:
        test_cases = self._repository.find({})
        return json([test_case.serialize() for test_case in test_cases])

    @route("/<id:str>", methods=["GET"])
    def get_test_case(self, request: Request, id: str) -> HTTPResponse:
        try:
            test_case = self._repository.find_by_id(id)
        except Exception as e:
            raise SanicException(e)
        return json(test_case.serialize())

    @route("/<id:str>", methods=["PUT"])
    def update_test_case(self, request: Request, id: str) -> HTTPResponse:
        payload = UpdateTestSuitePayload(**(request.json or {}))
        test_case = self._repository.update(
            id, payload.dict(exclude_none=True, exclude_unset=True))
        return json(test_case.serialize())

    @route("/<id:str>", methods=["DELETE"])
    def delete_test_case(self, request: Request, id: str) -> HTTPResponse:
        test_case = self._repository.delete(id)
        return json(test_case.serialize())
