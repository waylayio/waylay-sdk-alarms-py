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
    from waylay.services.alarms.models.cloud_alarm_event_data_type import (
        CloudAlarmEventDataType,
    )

    CloudAlarmEventDataTypeAdapter = TypeAdapter(CloudAlarmEventDataType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

cloud_alarm_event_data_type_model_schema = json.loads(
    r"""{
  "title" : "CloudAlarmEventData_type",
  "type" : "string",
  "enum" : [ "io.waylay.alarms.v1.AlarmRaised", "io.waylay.alarms.v1.EventOccurredAgain", "io.waylay.alarms.v1.AlarmUpdated" ]
}
""",
    object_hook=with_example_provider,
)
cloud_alarm_event_data_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

cloud_alarm_event_data_type_faker = JSF(
    cloud_alarm_event_data_type_model_schema, allow_none_optionals=1
)


class CloudAlarmEventDataTypeStub:
    """CloudAlarmEventDataType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cloud_alarm_event_data_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "CloudAlarmEventDataType":
        """Create CloudAlarmEventDataType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                CloudAlarmEventDataTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return CloudAlarmEventDataTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
