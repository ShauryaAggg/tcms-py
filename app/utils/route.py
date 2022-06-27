from typing import List


def route(uri: str, methods: List[str]):
    """
    Decorator used to define a route path and methods for a handler

    :param uri: The path of the route
    :param methods: The methods of the route
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        wrapper.route = True
        wrapper.uri = uri
        wrapper.methods = methods
        return wrapper
    return decorator
