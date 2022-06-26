from sanic import Blueprint
from app.db import repositories

from app.handlers.test_case import TestCaseHandler
from app.utils.function import as_func

handler = TestCaseHandler(repositories["test_case"])

blueprint = Blueprint("test_case", url_prefix="/test_case")

blueprint.add_route(as_func(handler.create_test_case),
                    handler.create_test_case.uri,
                    methods=handler.create_test_case.methods,
                    name="create")


blueprint.add_route(as_func(handler.get_test_case),
                    handler.get_test_case.uri,
                    methods=handler.get_test_case.methods,
                    name="find_by_id")
