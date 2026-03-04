"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, TypeAlias

ISO8601TimestampOrMillis: TypeAlias = Annotated[int, "Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds."] | datetime
"""ISO8601 timestamp or unix epoch milliseconds.."""
