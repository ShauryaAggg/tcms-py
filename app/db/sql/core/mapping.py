from typing import Any
import sqlalchemy as sql

from datetime import datetime, timedelta, date, time

"""
Map for pydantic models to SQLAlchemy models.
"""

types = {
    Any: sql.String,
    str: sql.String,
    int: sql.Integer,
    float: sql.Float,
    bool: sql.Boolean,
    datetime: sql.DateTime,
    date: sql.Date,
    time: sql.Time,
    timedelta: sql.Interval,
    list: sql.ARRAY,
    dict: sql.JSON,
    set: sql.ARRAY,
    frozenset: sql.ARRAY,
}
