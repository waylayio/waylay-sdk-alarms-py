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
    from waylay.services.alarms.models.batch_operation import BatchOperation

    BatchOperationAdapter = TypeAdapter(BatchOperation)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_model_schema = json.loads(
    r"""{
  "required" : [ "id", "operation", "queueTime", "user" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/BatchId"
    },
    "user" : {
      "type" : "string",
      "description" : "User id of the user who started the operation",
      "example" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe"
    },
    "operation" : {
      "$ref" : "#/components/schemas/BatchOperation_operation"
    },
    "queueTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
batch_operation_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_faker = JSF(batch_operation_model_schema, allow_none_optionals=1)


class BatchOperationStub:
    """BatchOperation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchOperation":
        """Create BatchOperation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchOperationAdapter.validate_python(cls.create_json())
