#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional
from dataclasses import dataclass
import datetime

import dateutil2.relativedelta as relativedelta


@dataclass
class Date:
    """
      Class for representing a date with day/month/year.
      Values of day/month/year can equal None, that means, that
      the field is undefined.
    """
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]

    def __init__(self,
                 year: Optional[int] = None,
                 month: Optional[int] = None,
                 day: Optional[int] = None) -> None:
        """
        Create new instance of Date(year, month, day)
        """
        try:
            # Checking that year/month/day is in valid ranges
            datetime.date(year or 1, month or 1, day or 1)
        except ValueError as msg:
            raise ValueError(msg)
        self.year = year
        self.month = month
        self.day = day

    def __add__(self, other: relativedelta.relativedelta) -> object:
        if isinstance(other, (relativedelta.relativedelta, Date)):
            res = other + relativedelta.relativedelta(years=self.year or 0,
                                                      months=self.month or 0,
                                                      days=self.day or 0)
            res_norm = res.normalized()
            return tuple.__new__(type(self), (res_norm.years or None,
                                              res_norm.months or None,
                                              res_norm.days or None))
        else:
            raise ValueError(f'add operation not supported for the type'
                             f'{type(other)}.')

    @classmethod
    def from_json(cls, s: str) -> object:
        values = []
        for f in s[5: -1].split(','):
            value = f.split('=')[-1]
            if value.strip() == 'None':
                values.append(None)
            else:
                values.append(int(value))
        return cls(*values)

    @classmethod
    def from_date(cls, date: datetime.date) -> object:
        """
          Return a new Date object with the same year/month/day.
        """
        return cls.__new__(cls, year=date.year, month=date.month, day=date.day)

    def to_date(self) -> datetime.date:
        """
          Return a new datetime.date with the same year/month/day.
          Zero values are replaced with 1.
        """
        return datetime.date(self.year or 1, self.month or 1, self.day or 1)
