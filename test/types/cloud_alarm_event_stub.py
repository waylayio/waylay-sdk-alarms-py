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
    from waylay.services.alarms.models.cloud_alarm_event import CloudAlarmEvent

    CloudAlarmEventAdapter = TypeAdapter(CloudAlarmEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

cloud_alarm_event_model_schema = json.loads(
    r"""{
  "example" : {
    "time" : "2011-09-06T12:03:27.845Z",
    "type" : "io.waylay.alarms.v1.AlarmUpdated",
    "subject" : "289dd1a3-35a7-44fa-8596-9aee3ad0b36f/2c49e3bf-547b-42bc-a5e9-9193155ec03d"
  },
  "allOf" : [ {
    "$ref" : "./cloudevents.schema.yaml#/definitions/cloudevent_json"
  }, {
    "$ref" : "#/components/schemas/CloudAlarmEventData"
  }, {
    "required" : [ "subject", "time" ]
  } ]
}
""",
    object_hook=with_example_provider,
)
cloud_alarm_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

cloud_alarm_event_faker = JSF(cloud_alarm_event_model_schema, allow_none_optionals=1)


class CloudAlarmEventStub:
    """CloudAlarmEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cloud_alarm_event_faker.generate()

    @classmethod
    def create_instance(cls) -> "CloudAlarmEvent":
        """Create CloudAlarmEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return CloudAlarmEventAdapter.validate_python(cls.create_json())