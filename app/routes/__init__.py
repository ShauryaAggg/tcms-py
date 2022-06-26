from sanic import Blueprint

from app.routes.test_case import blueprint as test_case_router

group = [test_case_router]

bp_group = Blueprint.group(*group, url_prefix="/api/v1")
