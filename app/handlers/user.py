from app.db import repositories
from app.handlers.base import Handler

from app.services.user.validators.payload import CreateUserPayload, UpdateUserPayload


class UserHandler(Handler):
    class Meta:
        repository = repositories['user']
