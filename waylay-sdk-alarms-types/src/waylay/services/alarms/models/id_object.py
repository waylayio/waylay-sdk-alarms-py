"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class IdObject(WaylayBaseModel):
    """A JSON object with an id field indicating the resource.."""

    id: StrictStr

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
