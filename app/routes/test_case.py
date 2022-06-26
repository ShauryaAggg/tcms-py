from app.routes.core.blueprint import Blueprint
from app.db import repositories

from app.handlers.test_case import TestCaseHandler
from app.utils.function import as_func

handler = TestCaseHandler(repositories["test_case"])

blueprint = Blueprint("test_case", url_prefix="/test_case")

blueprint.add_class_route(handler)
