"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.failure_operation_result_value import FailureOperationResultValue
from ..models.success_operation_result_value import SuccessOperationResultValue


class BatchOperationResults(WaylayBaseModel):
    """BatchOperationResults."""

    success: dict[str, SuccessOperationResultValue] = Field(
        description="Object containing the successful operation results. The keys will be alarm ids."
    )
    failure: dict[str, FailureOperationResultValue] = Field(
        description="Object containing the unsuccessful operation results. The keys will be alarm ids."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
