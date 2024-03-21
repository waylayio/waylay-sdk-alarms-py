# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from typing import (
    Union,
    Any,
    List,
    TYPE_CHECKING,
    Optional,
    Dict,
    Literal,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)
from pydantic import StrictStr, Field, ConfigDict


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from ..models.bulk_query_filter import BulkQueryFilter
from ..models.bulk_query_ids import BulkQueryIds

from ..models.bulk_query_ids import BulkQueryIds
from ..models.bulk_query_filter import BulkQueryFilter

BatchDeleteAlarmAllOfQuery = Union[
    Annotated[BulkQueryIds, ""], Annotated[BulkQueryFilter, ""]
]
"""BatchDeleteAlarmAllOfQuery."""
