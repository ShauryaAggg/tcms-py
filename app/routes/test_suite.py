from app.routes.core.blueprint import Blueprint

from app.db import repositories
from app.handlers.test_suite import TestSuiteHandler

handler = TestSuiteHandler(repositories["test_suite"])

blueprint = Blueprint("test_suite", url_prefix="/test_suite")
blueprint.register_handler(handler)
