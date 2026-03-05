"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class EventStreamFormat(str, Enum):
    """EventStreamFormat."""

    APPLICATION_SLASH_CLOUDEVENTS_PLUS_JSON = "application/cloudevents+json"

    def __str__(self) -> str:
        return str(self.value)
