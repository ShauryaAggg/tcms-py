from app.db.core.repository import Repository


class Handler:
    """
    Base handler for all handlers.
    """

    def __init__(self, repository: Repository) -> None:
        """
        Initialize handler with repository.

        :param repository: Repository instance.
        """
        self._repository = repository
