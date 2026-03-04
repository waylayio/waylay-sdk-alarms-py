"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.batch_delete_query import BatchDeleteQuery

    BatchDeleteQueryAdapter = TypeAdapter(BatchDeleteQuery)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_delete_query_model_schema = json.loads(
    r"""{
  "title" : "BatchDeleteQuery",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BulkQueryIds"
  }, {
    "$ref" : "#/components/schemas/BulkQueryFilter"
  } ]
}
""",
    object_hook=with_example_provider,
)
batch_delete_query_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_delete_query_faker = JSF(batch_delete_query_model_schema, allow_none_optionals=1)


class BatchDeleteQueryStub:
    """BatchDeleteQuery unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_delete_query_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "BatchDeleteQuery":
        """Create BatchDeleteQuery stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchDeleteQueryAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchDeleteQueryAdapter.validate_python(
            json, context={"skip_validation": True}
        )
