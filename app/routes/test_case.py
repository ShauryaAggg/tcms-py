from app.routes.core.blueprint import Blueprint
from app.handlers.test_case import TestCaseHandler

handler = TestCaseHandler()

blueprint = Blueprint("test_case", url_prefix="/test_case")
blueprint.register_handler(handler)
