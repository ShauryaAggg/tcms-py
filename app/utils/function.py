from typing import List


def as_func(func):
    """
    Convert a bounded method to a function object.

    :param func: A bounded method.

    :return: A function object.
    """

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
