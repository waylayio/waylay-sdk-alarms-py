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
    from waylay.services.alarms.models.create_alarm import CreateAlarm

    CreateAlarmAdapter = TypeAdapter(CreateAlarm)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

create_alarm_model_schema = json.loads(
    r"""{
  "required" : [ "severity", "source", "text", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/AlarmType"
    },
    "text" : {
      "$ref" : "#/components/schemas/AlarmText"
    },
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "source" : {
      "$ref" : "#/components/schemas/IdObject"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601TimestampOrMillis"
    },
    "assignee" : {
      "$ref" : "#/components/schemas/AlarmAssignee"
    }
  },
  "additionalProperties" : {
    "title" : "Additional properties",
    "description" : "Any additional properties provided upon creation will be stored in the `additionalProperties` field\nof the created alarm."
  },
  "description" : "To create an alarm, you need to provide the following mandatory inputs.",
  "example" : {
    "type" : "io.waylay.alarm.test",
    "text" : "Valve test failed",
    "severity" : "CRITICAL",
    "source" : {
      "id" : "733c06ed-7919-416a-9d19-8996821be70d"
    },
    "task" : "1e294c8b-8a7d-4770-997e-2d57fc5ad6ea",
    "myRef" : "902d4191-d1ab-47ae-8405-c33bb237f1d5"
  }
}
""",
    object_hook=with_example_provider,
)
create_alarm_model_schema.update({"definitions": MODEL_DEFINITIONS})

create_alarm_faker = JSF(create_alarm_model_schema, allow_none_optionals=1)


class CreateAlarmStub:
    """CreateAlarm unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return create_alarm_faker.generate()

    @classmethod
    def create_instance(cls) -> "CreateAlarm":
        """Create CreateAlarm stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CreateAlarmAdapter.validate_python(cls.create_json())