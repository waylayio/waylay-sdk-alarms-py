"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AlarmSeverity(str, Enum):
    """AlarmSeverity."""

    CRITICAL = "CRITICAL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
