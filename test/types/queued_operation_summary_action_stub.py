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
    from waylay.services.alarms.models.queued_operation_summary_action import (
        QueuedOperationSummaryAction,
    )

    QueuedOperationSummaryActionAdapter = TypeAdapter(QueuedOperationSummaryAction)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

queued_operation_summary_action_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "update", "delete" ]
}
""",
    object_hook=with_example_provider,
)
queued_operation_summary_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

queued_operation_summary_action_faker = JSF(
    queued_operation_summary_action_model_schema, allow_none_optionals=1
)


class QueuedOperationSummaryActionStub:
    """QueuedOperationSummaryAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return queued_operation_summary_action_faker.generate()

    @classmethod
    def create_instance(cls) -> "QueuedOperationSummaryAction":
        """Create QueuedOperationSummaryAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return QueuedOperationSummaryActionAdapter.validate_python(cls.create_json())