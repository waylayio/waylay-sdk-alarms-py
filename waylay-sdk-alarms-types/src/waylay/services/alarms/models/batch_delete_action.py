"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class BatchDeleteAction(str, Enum):
    """BatchDeleteAction."""

    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)
