# coding: utf-8
"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ListOrderParameterAnyOf1(str, Enum):
    """ListOrderParameterAnyOf1."""

    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
