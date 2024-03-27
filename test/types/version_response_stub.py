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
    from waylay.services.alarms.models.version_response import VersionResponse

    VersionResponseAdapter = TypeAdapter(VersionResponse)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

version_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "version" : {
      "type" : "string",
      "example" : "2.7.0"
    },
    "name" : {
      "type" : "string",
      "example" : "alarm-service"
    }
  }
}
""",
    object_hook=with_example_provider,
)
version_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

version_response_faker = JSF(version_response_model_schema, allow_none_optionals=1)


class VersionResponseStub:
    """VersionResponse unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return version_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "VersionResponse":
        """Create VersionResponse stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VersionResponseAdapter.validate_python(cls.create_json())
