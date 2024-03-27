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
    from waylay.services.alarms.models.alarm_event_type_one_of1 import (
        AlarmEventTypeOneOf1,
    )

    AlarmEventTypeOneOf1Adapter = TypeAdapter(AlarmEventTypeOneOf1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_event_type_one_of_1_model_schema = json.loads(
    r"""{
  "title" : "AlarmEventType_oneOf_1",
  "type" : "string",
  "description" : "An alarm happened again.",
  "enum" : [ "io.waylay.alarm.EventOccuredAgain" ]
}
""",
    object_hook=with_example_provider,
)
alarm_event_type_one_of_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_event_type_one_of_1_faker = JSF(
    alarm_event_type_one_of_1_model_schema, allow_none_optionals=1
)


class AlarmEventTypeOneOf1Stub:
    """AlarmEventTypeOneOf1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_event_type_one_of_1_faker.generate()

    @classmethod
    def create_instance(cls) -> "AlarmEventTypeOneOf1":
        """Create AlarmEventTypeOneOf1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AlarmEventTypeOneOf1Adapter.validate_python(cls.create_json())