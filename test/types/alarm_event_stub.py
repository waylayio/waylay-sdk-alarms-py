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
    from waylay.services.alarms.models.alarm_event import AlarmEvent

    AlarmEventAdapter = TypeAdapter(AlarmEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_event_model_schema = json.loads(
    r"""{
  "required" : [ "alarm", "eventtime", "eventtype" ],
  "type" : "object",
  "properties" : {
    "eventtype" : {
      "$ref" : "#/components/schemas/AlarmEventType"
    },
    "eventtime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "alarm" : {
      "$ref" : "#/components/schemas/AlarmEventAlarm"
    },
    "changes" : {
      "type" : "array",
      "description" : "Describes the changes that where done\n\nWill only be there if `eventtype` is `io.waylay.alarm.AlarmUpdated`",
      "items" : {
        "$ref" : "#/components/schemas/AlarmEvent_changes_inner"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
alarm_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_event_faker = JSF(alarm_event_model_schema, allow_none_optionals=1)


class AlarmEventStub:
    """AlarmEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_event_faker.generate()

    @classmethod
    def create_instance(cls) -> "AlarmEvent":
        """Create AlarmEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AlarmEventAdapter.validate_python(cls.create_json())
