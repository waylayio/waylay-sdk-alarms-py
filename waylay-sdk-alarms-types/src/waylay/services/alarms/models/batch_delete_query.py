"""Waylay Alarms models.

This code was generated from the OpenAPI documentation of 'Waylay Alarms'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.bulk_query_filter import BulkQueryFilter
from ..models.bulk_query_ids import BulkQueryIds

BatchDeleteQuery: TypeAlias = BulkQueryIds | BulkQueryFilter
"""BatchDeleteQuery."""
