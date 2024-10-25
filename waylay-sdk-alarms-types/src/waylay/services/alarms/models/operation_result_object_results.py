# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Dict

from pydantic import (
    ConfigDict,
    Field,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.failure_operation_result_value import FailureOperationResultValue
from ..models.success_operation_result_value import SuccessOperationResultValue


class OperationResultObjectResults(WaylayBaseModel):
    """OperationResultObjectResults."""

    success: Dict[str, SuccessOperationResultValue] = Field(
        description="Object containing the successful operation results.  The keys will be alarm ids."
    )
    failure: Dict[str, FailureOperationResultValue] = Field(
        description="Object containing the unsuccessful operation results.  The keys will be alarm ids."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
