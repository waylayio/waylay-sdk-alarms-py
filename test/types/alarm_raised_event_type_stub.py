"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.alarm_raised_event_type import (
        AlarmRaisedEventType,
    )

    AlarmRaisedEventTypeAdapter = TypeAdapter(AlarmRaisedEventType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alarm_raised_event_type_model_schema = json.loads(
    r"""{
  "title" : "AlarmRaisedEventType",
  "type" : "string",
  "description" : "A new alarm was created.",
  "enum" : [ "io.waylay.alarm.AlarmRaised" ]
}
""",
    object_hook=with_example_provider,
)
alarm_raised_event_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_raised_event_type_faker = JSF(
    alarm_raised_event_type_model_schema, allow_none_optionals=1
)


class AlarmRaisedEventTypeStub:
    """AlarmRaisedEventType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_raised_event_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AlarmRaisedEventType":
        """Create AlarmRaisedEventType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlarmRaisedEventTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlarmRaisedEventTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
