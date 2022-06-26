from sanic import Blueprint

from app.utils.function import as_func


class Blueprint(Blueprint):
    def add_class_route(self, handler, *args, **kwargs):
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
                method.uri,
                methods=method.methods,
            )
