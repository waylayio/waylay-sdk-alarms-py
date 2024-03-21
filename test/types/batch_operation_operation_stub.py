# coding: utf-8
"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.batch_operation_operation import (
        BatchOperationOperation,
    )

    BatchOperationOperationAdapter = TypeAdapter(BatchOperationOperation)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchOperation_operation",
  "required" : [ "action", "description", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchAlarmEntity"
    },
    "action" : {
      "title" : "action",
      "type" : "string",
      "enum" : [ "delete", "update" ]
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Description of the operation",
      "example" : "deleting 3 alarms"
    }
  },
  "description" : "Summary of the batch operation"
}
""",
    object_hook=with_example_provider,
)
batch_operation_operation_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_operation_faker = JSF(
    batch_operation_operation_model_schema, allow_none_optionals=1
)


class BatchOperationOperationStub:
    """BatchOperationOperation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_operation_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchOperationOperation":
        """Create BatchOperationOperation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchOperationOperationAdapter.validate_python(cls.create_json())
