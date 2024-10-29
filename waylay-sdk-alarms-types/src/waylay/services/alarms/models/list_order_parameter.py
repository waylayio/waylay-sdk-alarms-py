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

from ..models.list_order_parameter_any_of import ListOrderParameterAnyOf
from ..models.list_order_parameter_any_of1 import ListOrderParameterAnyOf1

ListOrderParameter = Union[
    Annotated[ListOrderParameterAnyOf, ""], Annotated[ListOrderParameterAnyOf1, ""]
]
"""ListOrderParameter."""
