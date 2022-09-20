from app.db import repositories
from app.handlers.base import Handler
from app.services.test_case.validators.payload import CreateTestCasePayload, UpdateTestCasePayload
from app.utils.route import route


class TestCaseHandler(Handler):
    """
    TestCase Handler class.
    """

    class Meta:
        repository = repositories["test_case"]
        create_payload = CreateTestCasePayload
        update_payload = UpdateTestCasePayload

    @route('/', methods=["DELETE"])
    def another_netho(self, request):
        pass
