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
    from waylay.services.alarms.models.id_object import IdObject

    IdObjectAdapter = TypeAdapter(IdObject)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

id_object_model_schema = json.loads(
    r"""{
  "title" : "IdObject",
  "required" : [ "id" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "title" : "Resource Id",
      "type" : "string"
    }
  },
  "description" : "A JSON object with an id field indicating the resource.",
  "example" : {
    "id" : "12345"
  }
}
""",
    object_hook=with_example_provider,
)
id_object_model_schema.update({"definitions": MODEL_DEFINITIONS})

id_object_faker = JSF(id_object_model_schema, allow_none_optionals=1)


class IdObjectStub:
    """IdObject unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return id_object_faker.generate()

    @classmethod
    def create_instance(cls) -> "IdObject":
        """Create IdObject stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return IdObjectAdapter.validate_python(cls.create_json())