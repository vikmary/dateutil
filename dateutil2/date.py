#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
import datetime

import dateutil2.relativedelta as relativedelta


class Date(namedtuple('Date', ['year', 'month', 'day'])):
    """
      Class for representing a date with day/month/year.
      Values of day/month/year can equal None, that means, that
      the field is undefined.
    """
    __slots__ = ()

    def __new__(_cls, year, month, day):
        'Create new instance of Date(year, month, day)'
        try:
            # Checking that year/month/day is in valid ranges
            datetime.date(year or 1, month or 1, day or 1)
        except ValueError as msg:
            raise ValueError(msg)
        return tuple.__new__(_cls, (year, month, day))

    def __add__(self, other: relativedelta.relativedelta) -> namedtuple:
        if isinstance(other, (relativedelta.relativedelta, namedtuple)):
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

    def replace(self, **kwargs):
        """
          Return a new instance of Date with new year/month/day.
        """
        return self._replace(**kwargs)

    @classmethod
    def from_date(cls, date: datetime.date) -> namedtuple:
        """
          Return a new Date object with the same year/month/day.
        """
        return cls.__new__(date.year, date.month, date.day)
        
    def to_date(self) -> datetime.date:
        """
          Return a new datetime.date with the same year/month/day.
          Zero values are replaced with 1.
        """
        return datetime.date(self.year or 1, self.month or 1, self.day or 1)
