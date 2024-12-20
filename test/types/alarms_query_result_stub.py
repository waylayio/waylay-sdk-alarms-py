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
    from waylay.services.alarms.models.alarms_query_result import AlarmsQueryResult

    AlarmsQueryResultAdapter = TypeAdapter(AlarmsQueryResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alarms_query_result_model_schema = json.loads(
    r"""{
  "required" : [ "alarms", "self", "total" ],
  "type" : "object",
  "properties" : {
    "self" : {
      "type" : "string",
      "description" : "Link to alarm query",
      "format" : "uri",
      "example" : "/alarms/v1/alarms?page=3"
    },
    "alarms" : {
      "title" : "List of alarms",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AlarmEntity"
      }
    },
    "total" : {
      "type" : "integer",
      "description" : "Total number of alarms that fulfill the criteria",
      "example" : 248
    },
    "next" : {
      "type" : "string",
      "description" : "Link to the next page of results (if more results are available)",
      "format" : "uri",
      "example" : "/alarms/v1/alarms?page=4"
    },
    "prev" : {
      "type" : "string",
      "description" : "Link to the previous page of result (if previous page is available)",
      "format" : "uri",
      "example" : "/alarms/v1/alarms?page=2"
    }
  }
}
""",
    object_hook=with_example_provider,
)
alarms_query_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

alarms_query_result_faker = JSF(
    alarms_query_result_model_schema, allow_none_optionals=1
)


class AlarmsQueryResultStub:
    """AlarmsQueryResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alarms_query_result_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlarmsQueryResult":
        """Create AlarmsQueryResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlarmsQueryResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlarmsQueryResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
