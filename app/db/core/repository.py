from typing import Any


class Repository:
    def find_by_id(self, id: Any) -> Any: ...
    def find(self, filter: Any) -> Any: ...
    def find_one(self, filter: Any) -> Any: ...
    def create(self, item: Any) -> Any: ...
    def update(self, id: Any, item: Any) -> Any: ...
    def delete(self, id: Any) -> Any: ...
