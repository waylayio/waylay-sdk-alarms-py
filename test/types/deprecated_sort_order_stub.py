"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.deprecated_sort_order import DeprecatedSortOrder

    DeprecatedSortOrderAdapter = TypeAdapter(DeprecatedSortOrder)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

deprecated_sort_order_model_schema = json.loads(
    r"""{
  "type" : "string",
  "deprecated" : true,
  "default" : "desc",
  "enum" : [ "asc", "desc" ]
}
""",
    object_hook=with_example_provider,
)
deprecated_sort_order_model_schema.update({"definitions": MODEL_DEFINITIONS})

deprecated_sort_order_faker = JSF(
    deprecated_sort_order_model_schema, allow_none_optionals=1
)


class DeprecatedSortOrderStub:
    """DeprecatedSortOrder unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return deprecated_sort_order_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DeprecatedSortOrder":
        """Create DeprecatedSortOrder stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DeprecatedSortOrderAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DeprecatedSortOrderAdapter.validate_python(
            json, context={"skip_validation": True}
        )
