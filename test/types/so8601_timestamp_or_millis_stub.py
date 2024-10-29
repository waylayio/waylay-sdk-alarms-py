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
    from waylay.services.alarms.models.so8601_timestamp_or_millis import (
        SO8601TimestampOrMillis,
    )

    SO8601TimestampOrMillisAdapter = TypeAdapter(SO8601TimestampOrMillis)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

so8601_timestamp_or_millis_model_schema = json.loads(
    r"""{
  "title" : "SO8601TimestampOrMillis",
  "description" : "ISO8601 timestamp or unix epoch milliseconds.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/SO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
so8601_timestamp_or_millis_model_schema.update({"definitions": MODEL_DEFINITIONS})

so8601_timestamp_or_millis_faker = JSF(
    so8601_timestamp_or_millis_model_schema, allow_none_optionals=1
)


class SO8601TimestampOrMillisStub:
    """SO8601TimestampOrMillis unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return so8601_timestamp_or_millis_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SO8601TimestampOrMillis":
        """Create SO8601TimestampOrMillis stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SO8601TimestampOrMillisAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SO8601TimestampOrMillisAdapter.validate_python(
            json, context={"skip_validation": True}
        )
