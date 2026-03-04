"""Waylay Alarms query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.
"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.event_stream_format import EventStreamFormat


def _get_query_alias_for(field_name: str) -> str:
    if field_name == "event_format":
        return "eventFormat"
    return field_name


class GetQuery(WaylayBaseModel):
    """Model for `get` query parameters."""

    event_format: Annotated[
        EventStreamFormat | None,
        Field(
            description="The format of events in the stream.   If specified this must be `application/cloudevents+json` (make sure to correctly URL encode the `+` as `%2B`)"
        ),
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_query_alias_for,
        populate_by_name=True,
    )
