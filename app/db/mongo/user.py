from app.models.user import User
from app.db.mongo.base import MongoBaseRepository


class UserRepository(MongoBaseRepository):
    class Meta:
        model = User
        collection = "users"
