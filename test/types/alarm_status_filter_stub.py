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
    from waylay.services.alarms.models.alarm_status_filter import AlarmStatusFilter

    AlarmStatusFilterAdapter = TypeAdapter(AlarmStatusFilter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_status_filter_model_schema = json.loads(
    r"""{
  "title" : "Alarm Status Filter",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmStatus"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
alarm_status_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_status_filter_faker = JSF(
    alarm_status_filter_model_schema, allow_none_optionals=1
)


class AlarmStatusFilterStub:
    """AlarmStatusFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_status_filter_faker.generate()

    @classmethod
    def create_instance(cls) -> "AlarmStatusFilter":
        """Create AlarmStatusFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return AlarmStatusFilterAdapter.validate_python(cls.create_json())
