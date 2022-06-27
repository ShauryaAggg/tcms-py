from app.routes.core.blueprint import Blueprint

from app.db import repositories
from app.handlers.test_step import TestStepHandler

handler = TestStepHandler(repositories["test_step"])

blueprint = Blueprint("test_step", url_prefix="/test_step")
blueprint.register_handler(handler)
