"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.cloud_alarm_event_type import CloudAlarmEventType

    CloudAlarmEventTypeAdapter = TypeAdapter(CloudAlarmEventType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

cloud_alarm_event_type_model_schema = json.loads(
    r"""{
  "title" : "CloudAlarmEventType",
  "type" : "string",
  "enum" : [ "io.waylay.alarms.v1.AlarmRaised", "io.waylay.alarms.v1.EventOccurredAgain", "io.waylay.alarms.v1.AlarmUpdated" ]
}
""",
    object_hook=with_example_provider,
)
cloud_alarm_event_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

cloud_alarm_event_type_faker = JSF(
    cloud_alarm_event_type_model_schema, allow_none_optionals=1
)


class CloudAlarmEventTypeStub:
    """CloudAlarmEventType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cloud_alarm_event_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "CloudAlarmEventType":
        """Create CloudAlarmEventType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                CloudAlarmEventTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return CloudAlarmEventTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
