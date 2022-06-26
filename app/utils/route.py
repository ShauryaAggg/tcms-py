from typing import List


def route(uri: str, methods: List[str]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        wrapper.uri = uri
        wrapper.methods = methods
        return wrapper
    return decorator
