"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.get_batch_operation_response import (
        GetBatchOperationResponse,
    )

    GetBatchOperationResponseAdapter = TypeAdapter(GetBatchOperationResponse)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

get_batch_operation_response_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/BatchOperationResult"
  }, {
    "$ref" : "#/components/schemas/BatchOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
get_batch_operation_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_batch_operation_response_faker = JSF(
    get_batch_operation_response_model_schema, allow_none_optionals=1
)


class GetBatchOperationResponseStub:
    """GetBatchOperationResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_batch_operation_response_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetBatchOperationResponse":
        """Create GetBatchOperationResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetBatchOperationResponseAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetBatchOperationResponseAdapter.validate_python(
            json, context={"skip_validation": True}
        )
