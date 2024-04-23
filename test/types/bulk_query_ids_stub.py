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
    from waylay.services.alarms.models.bulk_query_ids import BulkQueryIds

    BulkQueryIdsAdapter = TypeAdapter(BulkQueryIds)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

bulk_query_ids_model_schema = json.loads(
    r"""{
  "title" : "BulkQueryIds",
  "required" : [ "ids" ],
  "type" : "object",
  "properties" : {
    "ids" : {
      "title" : "ids",
      "minItems" : 1,
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AlarmId"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
bulk_query_ids_model_schema.update({"definitions": MODEL_DEFINITIONS})

bulk_query_ids_faker = JSF(bulk_query_ids_model_schema, allow_none_optionals=1)


class BulkQueryIdsStub:
    """BulkQueryIds unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return bulk_query_ids_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "BulkQueryIds":
        """Create BulkQueryIds stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BulkQueryIdsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BulkQueryIdsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
