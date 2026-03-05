"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlarmUpdatedEventType(str, Enum):
    """An alarm was updated.."""

    IO_DOT_WAYLAY_DOT_ALARM_DOT_ALARM_UPDATED = "io.waylay.alarm.AlarmUpdated"

    def __str__(self) -> str:
        return str(self.value)
