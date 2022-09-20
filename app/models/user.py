from app.models.base import Base


class User(Base):
    """
    Basic User model
    """
    name: str
    age: int
    email: str
