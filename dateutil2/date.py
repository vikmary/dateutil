#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional
import dataclasses
import datetime

import dateutil2.relativedelta as relativedelta


@dataclasses.dataclass(eq=True, unsafe_hash=True)
class Date:
    """
      Class for representing a date with day/month/year.
      Values of day/month/year can equal None, that means, that
      the field is undefined.
    """
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None

    def __post_init__(self) -> None:
        """
        Checks whether year, month and day are valid
        """
        try:
            # Checking that year/month/day is in valid ranges
            datetime.date(self.year or 1, self.month or 1, self.day or 1)
        except ValueError as msg:
            raise ValueError(msg)

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

    def replace(self, **changes):
        return dataclasses.replace(self, **changes)

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
        return cls(year=date.year, month=date.month, day=date.day)

    def to_date(self) -> datetime.date:
        """
          Return a new datetime.date with the same year/month/day.
          Zero values are replaced with 1.
        """
        return datetime.date(self.year or 1, self.month or 1, self.day or 1)
