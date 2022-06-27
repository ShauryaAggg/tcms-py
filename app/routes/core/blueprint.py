from sanic import Blueprint

from app.utils.function import as_func


class Blueprint(Blueprint):
    """
    Blueprint class that registers all handlers in the handler class.
    """

    def register_handler(self, handler, *args, **kwargs):
        """
        Register handler methods in the blueprint.
        """

        methods = [
            method for method in dir(handler)
            if not method.startswith('__') and
            callable(getattr(handler, method)) and
            getattr(getattr(handler, method), "route", False)
        ]

        for method in methods:
            method = getattr(handler, method)
            self.add_route(
                as_func(method),
                uri=getattr(method, "uri", "/"),
                methods=getattr(method, "methods", ["GET"]),
            )
