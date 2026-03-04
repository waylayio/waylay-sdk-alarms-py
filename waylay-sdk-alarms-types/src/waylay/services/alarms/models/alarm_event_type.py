"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.alarm_raised_event_type import AlarmRaisedEventType
from ..models.alarm_updated_event_type import AlarmUpdatedEventType
from ..models.event_occurred_again_event_type import EventOccurredAgainEventType

AlarmEventType: TypeAlias = AlarmRaisedEventType | EventOccurredAgainEventType | AlarmUpdatedEventType
"""AlarmEventType."""
