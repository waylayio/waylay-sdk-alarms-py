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
    from waylay.services.alarms.models.alarm_event_type_one_of import (
        AlarmEventTypeOneOf,
    )

    AlarmEventTypeOneOfAdapter = TypeAdapter(AlarmEventTypeOneOf)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_event_type_one_of_model_schema = json.loads(
    r"""{
  "title" : "AlarmEventType_oneOf",
  "type" : "string",
  "description" : "A new alarm was created.",
  "enum" : [ "io.waylay.alarm.AlarmRaised" ]
}
""",
    object_hook=with_example_provider,
)
alarm_event_type_one_of_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_event_type_one_of_faker = JSF(
    alarm_event_type_one_of_model_schema, allow_none_optionals=1
)


class AlarmEventTypeOneOfStub:
    """AlarmEventTypeOneOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_event_type_one_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AlarmEventTypeOneOf":
        """Create AlarmEventTypeOneOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlarmEventTypeOneOfAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlarmEventTypeOneOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
