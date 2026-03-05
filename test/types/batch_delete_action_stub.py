"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.batch_delete_action import BatchDeleteAction

    BatchDeleteActionAdapter = TypeAdapter(BatchDeleteAction)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_delete_action_model_schema = json.loads(
    r"""{
  "title" : "BatchDeleteAction",
  "type" : "string",
  "enum" : [ "delete" ]
}
""",
    object_hook=with_example_provider,
)
batch_delete_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_delete_action_faker = JSF(
    batch_delete_action_model_schema, allow_none_optionals=1
)


class BatchDeleteActionStub:
    """BatchDeleteAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_delete_action_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "BatchDeleteAction":
        """Create BatchDeleteAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchDeleteActionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchDeleteActionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
