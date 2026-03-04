"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ErrorResponseWithDetails(WaylayBaseModel):
    """ErrorResponseWithDetails."""

    status_code: StrictInt = Field(alias="statusCode")
    error: StrictStr
    details: Annotated[list[StrictStr], Field(min_length=1)] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
