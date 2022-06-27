from app.db.core.repository import Repository


class Handler:

    def __init__(self, repository: Repository) -> None:
        self._repository = repository
