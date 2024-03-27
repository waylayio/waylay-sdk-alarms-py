# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.alarm_event_type_one_of import AlarmEventTypeOneOf
from ..models.alarm_event_type_one_of1 import AlarmEventTypeOneOf1
from ..models.alarm_event_type_one_of2 import AlarmEventTypeOneOf2

AlarmEventType = Union[
    Annotated[AlarmEventTypeOneOf, ""],
    Annotated[AlarmEventTypeOneOf1, ""],
    Annotated[AlarmEventTypeOneOf2, ""],
]
"""AlarmEventType."""
