from app.routes.core.blueprint import Blueprint
from app.handlers.user import UserHandler

handler = UserHandler()

blueprint = Blueprint("users", url_prefix="/user")
blueprint.register_handler(handler)
