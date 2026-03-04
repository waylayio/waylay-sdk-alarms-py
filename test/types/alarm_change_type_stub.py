"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.alarm_change_type import AlarmChangeType

    AlarmChangeTypeAdapter = TypeAdapter(AlarmChangeType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alarm_change_type_model_schema = json.loads(
    r"""{
  "title" : "AlarmChangeType",
  "type" : "string",
  "description" : "Indication of what has changed",
  "enum" : [ "io.waylay.alarm.change.severity", "io.waylay.alarm.change.status", "io.waylay.alarm.change.attribute" ]
}
""",
    object_hook=with_example_provider,
)
alarm_change_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_change_type_faker = JSF(alarm_change_type_model_schema, allow_none_optionals=1)


class AlarmChangeTypeStub:
    """AlarmChangeType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_change_type_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlarmChangeType":
        """Create AlarmChangeType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlarmChangeTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlarmChangeTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
