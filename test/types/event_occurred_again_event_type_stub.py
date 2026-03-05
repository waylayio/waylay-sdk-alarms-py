"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.event_occurred_again_event_type import (
        EventOccurredAgainEventType,
    )

    EventOccurredAgainEventTypeAdapter = TypeAdapter(EventOccurredAgainEventType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

event_occurred_again_event_type_model_schema = json.loads(
    r"""{
  "title" : "EventOccurredAgainEventType",
  "type" : "string",
  "description" : "An alarm happened again.",
  "enum" : [ "io.waylay.alarm.EventOccuredAgain" ]
}
""",
    object_hook=with_example_provider,
)
event_occurred_again_event_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

event_occurred_again_event_type_faker = JSF(
    event_occurred_again_event_type_model_schema, allow_none_optionals=1
)


class EventOccurredAgainEventTypeStub:
    """EventOccurredAgainEventType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return event_occurred_again_event_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "EventOccurredAgainEventType":
        """Create EventOccurredAgainEventType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                EventOccurredAgainEventTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return EventOccurredAgainEventTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
