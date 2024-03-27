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
    from waylay.services.alarms.models.list_order_parameter import ListOrderParameter

    ListOrderParameterAdapter = TypeAdapter(ListOrderParameter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

list_order_parameter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "desc",
  "enum" : [ "asc", "desc" ]
}
""",
    object_hook=with_example_provider,
)
list_order_parameter_model_schema.update({"definitions": MODEL_DEFINITIONS})

list_order_parameter_faker = JSF(
    list_order_parameter_model_schema, allow_none_optionals=1
)


class ListOrderParameterStub:
    """ListOrderParameter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_order_parameter_faker.generate()

    @classmethod
    def create_instance(cls) -> "ListOrderParameter":
        """Create ListOrderParameter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ListOrderParameterAdapter.validate_python(cls.create_json())