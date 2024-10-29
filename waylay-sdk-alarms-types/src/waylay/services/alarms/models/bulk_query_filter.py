# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.alarm_severity_filter import AlarmSeverityFilter
from ..models.alarm_source_filter import AlarmSourceFilter
from ..models.alarm_status_filter import AlarmStatusFilter
from ..models.alarm_type_filter import AlarmTypeFilter


class BulkQueryFilter(WaylayBaseModel):
    """Object specifying filters on the alarm to which the operation will be applied. At least one of the filters must be set.."""

    type: AlarmTypeFilter | None = None
    status: AlarmStatusFilter | None = None
    severity: AlarmSeverityFilter | None = None
    source: AlarmSourceFilter | None = None
    date_from: Any | None = Field(default=None, alias="dateFrom")
    date_to: Any | None = Field(default=None, alias="dateTo")
    assignee: StrictStr | None = Field(
        default=None, description="String field to indicate an assignee for the alarm."
    )
    creation_time_from: Any | None = Field(default=None, alias="creationTimeFrom")
    creation_time_to: Any | None = Field(default=None, alias="creationTimeTo")
    last_updated_from: Any | None = Field(default=None, alias="lastUpdatedFrom")
    last_updated_to: Any | None = Field(default=None, alias="lastUpdatedTo")
    last_triggered_from: Any | None = Field(default=None, alias="lastTriggeredFrom")
    last_triggered_to: Any | None = Field(default=None, alias="lastTriggeredTo")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
