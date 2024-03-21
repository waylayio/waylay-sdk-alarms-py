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
    from waylay.services.alarms.models.cloud_alarm_event_data import CloudAlarmEventData

    CloudAlarmEventDataAdapter = TypeAdapter(CloudAlarmEventData)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

cloud_alarm_event_data_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "id" : {
      "example" : "dd59d2d9-9657-4d36-b045-ef97315f2d20"
    },
    "source" : {
      "example" : "/alarms/v1/alarms"
    },
    "subject" : {
      "type" : "string",
      "example" : "289dd1a3-35a7-44fa-8596-9aee3ad0b36f/2c49e3bf-547b-42bc-a5e9-9193155ec03d"
    },
    "type" : {
      "type" : "string",
      "enum" : [ "io.waylay.alarms.v1.AlarmRaised", "io.waylay.alarms.v1.EventOccurredAgain", "io.waylay.alarms.v1.AlarmUpdated" ]
    },
    "data" : {
      "$ref" : "#/components/schemas/AlarmEvent"
    },
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
cloud_alarm_event_data_model_schema.update({"definitions": MODEL_DEFINITIONS})

cloud_alarm_event_data_faker = JSF(
    cloud_alarm_event_data_model_schema, allow_none_optionals=1
)


class CloudAlarmEventDataStub:
    """CloudAlarmEventData unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cloud_alarm_event_data_faker.generate()

    @classmethod
    def create_instance(cls) -> "CloudAlarmEventData":
        """Create CloudAlarmEventData stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CloudAlarmEventDataAdapter.validate_python(cls.create_json())
