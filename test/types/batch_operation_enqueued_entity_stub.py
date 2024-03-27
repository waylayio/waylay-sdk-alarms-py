# coding: utf-8
"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.batch_operation_enqueued_entity import (
        BatchOperationEnqueuedEntity,
    )

    BatchOperationEnqueuedEntityAdapter = TypeAdapter(BatchOperationEnqueuedEntity)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_enqueued_entity_model_schema = json.loads(
    r"""{
  "required" : [ "id", "operation", "queueTime" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/BatchId"
    },
    "queueTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "operation" : {
      "$ref" : "#/components/schemas/Queued_operation_summary"
    }
  }
}
""",
    object_hook=with_example_provider,
)
batch_operation_enqueued_entity_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_enqueued_entity_faker = JSF(
    batch_operation_enqueued_entity_model_schema, allow_none_optionals=1
)


class BatchOperationEnqueuedEntityStub:
    """BatchOperationEnqueuedEntity unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_enqueued_entity_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchOperationEnqueuedEntity":
        """Create BatchOperationEnqueuedEntity stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchOperationEnqueuedEntityAdapter.validate_python(cls.create_json())
