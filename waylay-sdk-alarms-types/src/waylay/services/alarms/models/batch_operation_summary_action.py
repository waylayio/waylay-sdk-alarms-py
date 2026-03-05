"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class BatchOperationSummaryAction(str, Enum):
    """BatchOperationSummaryAction."""

    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
