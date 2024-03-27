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
    from waylay.services.alarms.models.ss_event_stream import SSEventStream

    SSEventStreamAdapter = TypeAdapter(SSEventStream)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

ss_event_stream_model_schema = json.loads(
    r"""{
  "title" : "SSEventStream",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmEvent"
  }, {
    "$ref" : "#/components/schemas/CloudAlarmEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
ss_event_stream_model_schema.update({"definitions": MODEL_DEFINITIONS})

ss_event_stream_faker = JSF(ss_event_stream_model_schema, allow_none_optionals=1)


class SSEventStreamStub:
    """SSEventStream unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return ss_event_stream_faker.generate()

    @classmethod
    def create_instance(cls) -> "SSEventStream":
        """Create SSEventStream stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SSEventStreamAdapter.validate_python(cls.create_json())
