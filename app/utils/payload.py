from typing import Optional
from datetime import datetime

from pydantic.main import ModelMetaclass
from pydantic import root_validator


class AllOptional(ModelMetaclass):
    """
    Metaclass to mark all the fields of a model as Optional
    """

    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(getattr(base, '__annotations__', {}))

        for field in annotations:
            if (not field.startswith('__')):
                annotations[field] = Optional[annotations[field]]

        namespaces['__annotations__'] = annotations

        return super().__new__(self, name, bases, namespaces, **kwargs)


def get_create_payload(model):
    class _CreatePayload(model):
        pass
    return _CreatePayload


def get_upload_payload(model):
    class _UploadPayload(model, metaclass=AllOptional):
        @root_validator(allow_reuse=True)
        def validate_values(cls, values):
            values['updated_at'] = datetime.now()
            values.pop('id', None)  # Disallow sending `id` in `update_payload`
            return values

    return _UploadPayload
