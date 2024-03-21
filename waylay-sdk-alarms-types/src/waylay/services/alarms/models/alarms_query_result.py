# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from pydantic_core import from_json
from typing import Callable, Union
from typing import cast
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from ..models.alarm_entity import AlarmEntity


class AlarmsQueryResult(BaseModel):
    """AlarmsQueryResult."""

    var_self: StrictStr = Field(description="Link to alarm query", alias="self")
    alarms: List[AlarmEntity]
    total: StrictInt = Field(
        description="Total number of alarms that fulfill the criteria"
    )
    next: StrictStr | None = Field(
        default=None,
        description="Link to the next page of results (if more results are available)",
    )
    prev: StrictStr | None = Field(
        default=None,
        description="Link to the previous page of result (if previous page is available)",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    @model_serializer(mode="wrap")
    def serializer(
        self, handler: Callable, info: SerializationInfo
    ) -> Dict[StrictStr, Any]:
        """The default serializer of the model.

        * Excludes `None` fields that were not set at model initialization.
        """
        model_dict = handler(self, info)
        return {
            k: v
            for k, v in model_dict.items()
            if v is not None or k in self.model_fields_set
        }

    def to_dict(self) -> dict[str, Any]:
        """Convert the AlarmsQueryResult instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the AlarmsQueryResult instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a AlarmsQueryResult instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: str | bytes | bytearray) -> Self:
        """Create a AlarmsQueryResult instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)
