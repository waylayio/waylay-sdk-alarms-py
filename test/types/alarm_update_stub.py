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
    from waylay.services.alarms.models.alarm_update import AlarmUpdate

    AlarmUpdateAdapter = TypeAdapter(AlarmUpdate)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_update_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "assignee" : {
      "allOf" : [ {
        "$ref" : "#/components/schemas/AlarmAssignee"
      }, {
        "nullable" : true
      } ]
    }
  },
  "description" : "At least one field must be specified."
}
""",
    object_hook=with_example_provider,
)
alarm_update_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_update_faker = JSF(alarm_update_model_schema, allow_none_optionals=1)


class AlarmUpdateStub:
    """AlarmUpdate unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_update_faker.generate()

    @classmethod
    def create_instance(cls) -> "AlarmUpdate":
        """Create AlarmUpdate stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AlarmUpdateAdapter.validate_python(cls.create_json())
