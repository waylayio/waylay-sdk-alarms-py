"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_operation_summary import BatchOperationSummary


class BatchOperation(WaylayBaseModel):
    """BatchOperation."""

    id: StrictStr
    user: StrictStr = Field(description="User id of the user who started the operation")
    operation: BatchOperationSummary
    queue_time: datetime = Field(alias="queueTime")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
