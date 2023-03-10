import numpy as np
from .birashk import add_days as bir_add_days
from .birashk import is_leapyear as bir_is_leapyear
from .birashk import day_of_year as bir_day_of_year
from .birashk import jd_to_persian, persian_to_jd
from .gregorian import add_days as gre_add_days
from .gregorian import greg_leap as gre_is_leapyear
from .gregorian import day_of_year as gre_day_of_year
from .gregorian import jd_to_gregorian, gregorian_to_jd



def persian_from_jd(jd):
    date, time = jd_to_persian(jd)
    y,m,d = date
    H,M,S,MS = time
    return Persian(y,m,d, H,M,S,MS)


class Persian:
    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.datetime = (year, month, day, hour, minute, second, microsecond)
        self.date = (year, month, day)
        self.time = (hour, minute, second, microsecond)

    def __repr__(self):
        return 'Persian'+str(self.datetime)

    def is_leap(self):
        return bir_is_leapyear(self.year)

    def day_of_year(self):
        return bir_day_of_year(self.year, self.month, self.day)

    def to_jd(self):
        return persian_to_jd(self.datetime)

    def to_gregorian(self):
        jd = self.to_jd()
        return gregorian_from_jd(jd)

    def add_days(self, delta):
        self.date = bir_add_days(self.date, delta)
        self.year, self.month, self.day = self.date
        self.datetime = (self.year, self.month, self.day,
                         self.hour, self.minute, self.second,
                         self.microsecond)
        


def gregorian_from_jd(jd):
    date, time = jd_to_gregorian(jd)
    y,m,d = date
    H,M,S,MS = time
    return Gregorian(y,m,d, H,M,S,MS)


class Gregorian:
    def __init__(self, year, month, day, hour=0, minute=0, second=0, microsecond=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.datetime = (year, month, day, hour, minute, second, microsecond)
        self.date = (year, month, day)
        self.time = (hour, minute, second, microsecond)

    def __repr__(self):
        return 'Gregorian'+str(self.datetime)

    def is_leap(self):
        return gre_is_leapyear(self.year)

    def day_of_year(self):
        return gre_day_of_year(self.year, self.month, self.day)

    def to_jd(self):
        return gregorian_to_jd(self.datetime)

    def to_persian(self):
        jd = self.to_jd()
        return persian_from_jd(jd)

    def add_days(self, delta):
        self.date = gre_add_days(self.date, delta)
        self.year, self.month, self.day = self.date
        self.datetime = (self.year, self.month, self.day,
                         self.hour, self.minute, self.second,
                         self.microsecond)

# https://github.com/behrouzz/astrodata/raw/main/equinox/equinox_time.csv
