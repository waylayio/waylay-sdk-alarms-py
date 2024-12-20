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
    from waylay.services.alarms.models.list_order_parameter_any_of import (
        ListOrderParameterAnyOf,
    )

    ListOrderParameterAnyOfAdapter = TypeAdapter(ListOrderParameterAnyOf)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

list_order_parameter_any_of_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "descending",
  "enum" : [ "ascending", "descending" ]
}
""",
    object_hook=with_example_provider,
)
list_order_parameter_any_of_model_schema.update({"definitions": MODEL_DEFINITIONS})

list_order_parameter_any_of_faker = JSF(
    list_order_parameter_any_of_model_schema, allow_none_optionals=1
)


class ListOrderParameterAnyOfStub:
    """ListOrderParameterAnyOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_order_parameter_any_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ListOrderParameterAnyOf":
        """Create ListOrderParameterAnyOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ListOrderParameterAnyOfAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ListOrderParameterAnyOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
