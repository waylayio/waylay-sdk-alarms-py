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
    from waylay.services.alarms.models.batch_alarm import BatchAlarm

    BatchAlarmAdapter = TypeAdapter(BatchAlarm)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_alarm_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchAlarmEntity"
    },
    "action" : {
      "type" : "string"
    },
    "query" : {
      "type" : "object"
    }
  }
}
""",
    object_hook=with_example_provider,
)
batch_alarm_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_alarm_faker = JSF(batch_alarm_model_schema, allow_none_optionals=1)


class BatchAlarmStub:
    """BatchAlarm unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_alarm_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchAlarm":
        """Create BatchAlarm stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchAlarmAdapter.validate_python(cls.create_json())
