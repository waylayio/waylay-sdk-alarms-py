# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_alarm_entity import BatchAlarmEntity
from ..models.batch_delete_alarm_all_of_action import BatchDeleteAlarmAllOfAction
from ..models.batch_delete_alarm_all_of_query import BatchDeleteAlarmAllOfQuery


class BatchDeleteAlarm(WaylayBaseModel):
    """BatchDeleteAlarm."""

    entity: BatchAlarmEntity
    action: BatchDeleteAlarmAllOfAction
    query: BatchDeleteAlarmAllOfQuery

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
