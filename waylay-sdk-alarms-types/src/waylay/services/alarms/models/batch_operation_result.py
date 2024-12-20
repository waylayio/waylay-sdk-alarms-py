# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

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

from ..models.batch_operation_operation import BatchOperationOperation
from ..models.operation_result_object_results import OperationResultObjectResults


class BatchOperationResult(WaylayBaseModel):
    """BatchOperationResult."""

    id: StrictStr
    user: StrictStr = Field(description="User id of the user who started the operation")
    operation: BatchOperationOperation
    queue_time: datetime = Field(alias="queueTime")
    finished_time: datetime = Field(alias="finishedTime")
    results: OperationResultObjectResults

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
