"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.batch_operation_summary_action import (
        BatchOperationSummaryAction,
    )

    BatchOperationSummaryActionAdapter = TypeAdapter(BatchOperationSummaryAction)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_operation_summary_action_model_schema = json.loads(
    r"""{
  "title" : "BatchOperationSummary_action",
  "type" : "string",
  "enum" : [ "delete", "update" ]
}
""",
    object_hook=with_example_provider,
)
batch_operation_summary_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_summary_action_faker = JSF(
    batch_operation_summary_action_model_schema, allow_none_optionals=1
)


class BatchOperationSummaryActionStub:
    """BatchOperationSummaryAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_summary_action_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchOperationSummaryAction":
        """Create BatchOperationSummaryAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchOperationSummaryActionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchOperationSummaryActionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
