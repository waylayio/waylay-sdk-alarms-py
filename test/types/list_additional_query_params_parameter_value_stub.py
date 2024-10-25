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
    from waylay.services.alarms.models.list_additional_query_params_parameter_value import (
        ListAdditionalQueryParamsParameterValue,
    )

    ListAdditionalQueryParamsParameterValueAdapter = TypeAdapter(
        ListAdditionalQueryParamsParameterValue
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

list_additional_query_params_parameter_value_model_schema = json.loads(
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
list_additional_query_params_parameter_value_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

list_additional_query_params_parameter_value_faker = JSF(
    list_additional_query_params_parameter_value_model_schema, allow_none_optionals=1
)


class ListAdditionalQueryParamsParameterValueStub:
    """ListAdditionalQueryParamsParameterValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_additional_query_params_parameter_value_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ListAdditionalQueryParamsParameterValue":
        """Create ListAdditionalQueryParamsParameterValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ListAdditionalQueryParamsParameterValueAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ListAdditionalQueryParamsParameterValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
