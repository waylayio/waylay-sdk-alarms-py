"""Waylay Alarms model tests.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.alarms.models.iso8601_timestamp_or_millis import (
        ISO8601TimestampOrMillis,
    )

    ISO8601TimestampOrMillisAdapter = TypeAdapter(ISO8601TimestampOrMillis)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

iso8601_timestamp_or_millis_model_schema = json.loads(
    r"""{
  "title" : "ISO8601TimestampOrMillis",
  "description" : "ISO8601 timestamp or unix epoch milliseconds.",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/UnixEpochMillis"
  }, {
    "$ref" : "#/components/schemas/ISO8601Timestamp"
  } ]
}
""",
    object_hook=with_example_provider,
)
iso8601_timestamp_or_millis_model_schema.update({"definitions": MODEL_DEFINITIONS})

iso8601_timestamp_or_millis_faker = JSF(
    iso8601_timestamp_or_millis_model_schema, allow_none_optionals=1
)


class ISO8601TimestampOrMillisStub:
    """ISO8601TimestampOrMillis unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return iso8601_timestamp_or_millis_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ISO8601TimestampOrMillis":
        """Create ISO8601TimestampOrMillis stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ISO8601TimestampOrMillisAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ISO8601TimestampOrMillisAdapter.validate_python(
            json, context={"skip_validation": True}
        )
