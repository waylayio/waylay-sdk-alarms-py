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
    from waylay.services.alarms.models.alarm_severity_filter import AlarmSeverityFilter

    AlarmSeverityFilterAdapter = TypeAdapter(AlarmSeverityFilter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_severity_filter_model_schema = json.loads(
    r"""{
  "title" : "Alarm Severity Filter",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmSeverity"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
alarm_severity_filter_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_severity_filter_faker = JSF(
    alarm_severity_filter_model_schema, allow_none_optionals=1
)


class AlarmSeverityFilterStub:
    """AlarmSeverityFilter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_severity_filter_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AlarmSeverityFilter":
        """Create AlarmSeverityFilter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlarmSeverityFilterAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlarmSeverityFilterAdapter.validate_python(
            json, context={"skip_validation": True}
        )
