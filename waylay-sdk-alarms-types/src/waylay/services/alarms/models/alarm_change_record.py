"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_change_type import AlarmChangeType


class AlarmChangeRecord(WaylayBaseModel):
    """AlarmChangeRecord."""

    attribute: StrictStr | None = None
    type: AlarmChangeType | None = None
    old_value: StrictStr | None = Field(default=None, alias="oldValue")
    new_value: StrictStr | None = Field(default=None, alias="newValue")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
