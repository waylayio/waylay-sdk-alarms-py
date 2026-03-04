"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.additional_query_param_value import (
        AdditionalQueryParamValue,
    )

    AdditionalQueryParamValueAdapter = TypeAdapter(AdditionalQueryParamValue)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

additional_query_param_value_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "type" : "number"
  }, {
    "type" : "string"
  }, {
    "type" : "boolean"
  } ]
}
""",
    object_hook=with_example_provider,
)
additional_query_param_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

additional_query_param_value_faker = JSF(
    additional_query_param_value_model_schema, allow_none_optionals=1
)


class AdditionalQueryParamValueStub:
    """AdditionalQueryParamValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return additional_query_param_value_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AdditionalQueryParamValue":
        """Create AdditionalQueryParamValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AdditionalQueryParamValueAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AdditionalQueryParamValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
