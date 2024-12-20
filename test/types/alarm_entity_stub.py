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
    from waylay.services.alarms.models.alarm_entity import AlarmEntity

    AlarmEntityAdapter = TypeAdapter(AlarmEntity)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarm_entity_model_schema = json.loads(
    r"""{
  "required" : [ "count", "creationTime", "id", "lastTriggeredTime", "lastUpdateTime", "severity", "source", "status", "text", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/AlarmId"
    },
    "creationTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "lastUpdateTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "lastTriggeredTime" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "type" : {
      "$ref" : "#/components/schemas/AlarmType"
    },
    "text" : {
      "$ref" : "#/components/schemas/AlarmText"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "source" : {
      "$ref" : "#/components/schemas/IdObject"
    },
    "severity" : {
      "$ref" : "#/components/schemas/AlarmSeverity"
    },
    "status" : {
      "$ref" : "#/components/schemas/AlarmStatus"
    },
    "count" : {
      "title" : "Event count",
      "minimum" : 1,
      "type" : "integer",
      "description" : "The number of times this alarm has been sent"
    },
    "assignee" : {
      "$ref" : "#/components/schemas/AlarmAssignee"
    },
    "history" : {
      "title" : "History of modifications",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AlarmAuditRecord"
      }
    },
    "self" : {
      "$ref" : "#/components/schemas/AlarmSelfLink"
    },
    "additionalProperties" : {
      "type" : "object",
      "description" : "Additional properties that were present in the creation payload",
      "example" : {
        "task" : "1e294c8b-8a7d-4770-997e-2d57fc5ad6ea",
        "myRef" : "902d4191-d1ab-47ae-8405-c33bb237f1d5"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
alarm_entity_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarm_entity_faker = JSF(alarm_entity_model_schema, allow_none_optionals=1)


class AlarmEntityStub:
    """AlarmEntity unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarm_entity_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlarmEntity":
        """Create AlarmEntity stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AlarmEntityAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlarmEntityAdapter.validate_python(
            json, context={"skip_validation": True}
        )
