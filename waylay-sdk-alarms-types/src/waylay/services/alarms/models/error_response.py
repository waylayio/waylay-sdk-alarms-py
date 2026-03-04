"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ErrorResponse(WaylayBaseModel):
    """ErrorResponse."""

    status_code: StrictInt = Field(alias="statusCode")
    error: StrictStr

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
