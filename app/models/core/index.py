from typing import List, Any


class IndexModel:

    def __init__(self, keys, *args, **kwargs) -> None:
        self._keys: List[tuple] = []
        self._unique = kwargs.get('unique', False)
        self._sparse = kwargs.get('sparse', False)

        for key in keys:
            if not isinstance(key, (str, tuple)):
                raise TypeError("Index key must be a string or a tuple")

            if isinstance(key, str):
                self._keys.append((key, 1))

            if isinstance(key, tuple):
                if (len(key) != 2):
                    raise TypeError(
                        "Index key must be a string or a tuple of shape (key, direction)")

                if key[1] < 0:
                    key = (key[0], -1)
                else:
                    key = (key[0], 1)

                self._keys.append(key)

    @property
    def keys(self) -> List[Any]:
        return self._keys

    @property
    def unique(self) -> bool:
        return self._unique

    @property
    def sparse(self) -> bool:
        return self._sparse
