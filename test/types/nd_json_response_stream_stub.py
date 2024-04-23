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
    from waylay.services.alarms.models.nd_json_response_stream import (
        NdJsonResponseStream,
    )

    NdJsonResponseStreamAdapter = TypeAdapter(NdJsonResponseStream)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

nd_json_response_stream_model_schema = json.loads(
    r"""{
  "title" : "NdJsonResponseStream",
  "example" : {
    "time" : "2011-09-06T12:03:27.845Z",
    "type" : "io.waylay.alarms.v1.AlarmUpdated",
    "subject" : "289dd1a3-35a7-44fa-8596-9aee3ad0b36f/2c49e3bf-547b-42bc-a5e9-9193155ec03d"
  },
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AlarmEvent"
  }, {
    "$ref" : "#/components/schemas/CloudAlarmEvent"
  } ]
}
""",
    object_hook=with_example_provider,
)
nd_json_response_stream_model_schema.update({"definitions": MODEL_DEFINITIONS})

nd_json_response_stream_faker = JSF(
    nd_json_response_stream_model_schema, allow_none_optionals=1
)


class NdJsonResponseStreamStub:
    """NdJsonResponseStream unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return nd_json_response_stream_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "NdJsonResponseStream":
        """Create NdJsonResponseStream stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                NdJsonResponseStreamAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return NdJsonResponseStreamAdapter.validate_python(
            json, context={"skip_validation": True}
        )
