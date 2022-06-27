from sanic import Blueprint

from app.routes.test_case import blueprint as test_case_router
from app.routes.test_step import blueprint as test_step_router

group = [test_case_router, test_step_router]

bp_group = Blueprint.group(*group, url_prefix="/api/v1")
