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
    from waylay.services.alarms.models.error_response_with_details import (
        ErrorResponseWithDetails,
    )

    ErrorResponseWithDetailsAdapter = TypeAdapter(ErrorResponseWithDetails)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

error_response_with_details_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/ErrorResponse"
  }, {
    "type" : "object",
    "properties" : {
      "details" : {
        "minItems" : 1,
        "type" : "array",
        "items" : {
          "type" : "string",
          "description" : "specific error message",
          "example" : "/severity <- Could not parse severity, valid values are: CRITICAL, MAJOR, MINOR, WARNING"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
error_response_with_details_model_schema.update({"definitions": MODEL_DEFINITIONS})

error_response_with_details_faker = JSF(
    error_response_with_details_model_schema, allow_none_optionals=1
)


class ErrorResponseWithDetailsStub:
    """ErrorResponseWithDetails unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return error_response_with_details_faker.generate()

    @classmethod
    def create_instance(cls) -> "ErrorResponseWithDetails":
        """Create ErrorResponseWithDetails stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ErrorResponseWithDetailsAdapter.validate_python(cls.create_json())
