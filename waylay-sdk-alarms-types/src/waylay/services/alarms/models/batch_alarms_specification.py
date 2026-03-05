"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch_delete_alarm import BatchDeleteAlarm
from ..models.batch_update_alarm import BatchUpdateAlarm

BatchAlarmsSpecification: TypeAlias = BatchUpdateAlarm | BatchDeleteAlarm
"""BatchAlarmsSpecification."""
