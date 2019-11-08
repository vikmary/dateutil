import sys
import unittest

class ImportVersionTest(unittest.TestCase):
    """ Test that dateutil2.__version__ can be imported"""

    def testImportVersionStr(self):
        from dateutil2 import __version__

    def testImportRoot(self):
        import dateutil2

        self.assertTrue(hasattr(dateutil2, '__version__'))


class ImportEasterTest(unittest.TestCase):
    """ Test that dateutil2.easter-related imports work properly """

    def testEasterDirect(self):
        import dateutil2.easter

    def testEasterFrom(self):
        from dateutil2 import easter

    def testEasterStar(self):
        from dateutil2.easter import easter


class ImportParserTest(unittest.TestCase):
    """ Test that dateutil2.parser-related imports work properly """
    def testParserDirect(self):
        import dateutil2.parser

    def testParserFrom(self):
        from dateutil2 import parser

    def testParserAll(self):
        # All interface
        from dateutil2.parser import parse
        from dateutil2.parser import parserinfo

        # Other public classes
        from dateutil2.parser import parser

        for var in (parse, parserinfo, parser):
            self.assertIsNot(var, None)


class ImportRelativeDeltaTest(unittest.TestCase):
    """ Test that dateutil2.relativedelta-related imports work properly """
    def testRelativeDeltaDirect(self):
        import dateutil2.relativedelta

    def testRelativeDeltaFrom(self):
        from dateutil2 import relativedelta

    def testRelativeDeltaAll(self):
        from dateutil2.relativedelta import relativedelta
        from dateutil2.relativedelta import MO, TU, WE, TH, FR, SA, SU

        for var in (relativedelta, MO, TU, WE, TH, FR, SA, SU):
            self.assertIsNot(var, None)

        # In the public interface but not in all
        from dateutil2.relativedelta import weekday
        self.assertIsNot(weekday, None)


class ImportRRuleTest(unittest.TestCase):
    """ Test that dateutil2.rrule related imports work properly """
    def testRRuleDirect(self):
        import dateutil2.rrule

    def testRRuleFrom(self):
        from dateutil2 import rrule

    def testRRuleAll(self):
        from dateutil2.rrule import rrule
        from dateutil2.rrule import rruleset
        from dateutil2.rrule import rrulestr
        from dateutil2.rrule import YEARLY, MONTHLY, WEEKLY, DAILY
        from dateutil2.rrule import HOURLY, MINUTELY, SECONDLY
        from dateutil2.rrule import MO, TU, WE, TH, FR, SA, SU

        rr_all = (rrule, rruleset, rrulestr,
                  YEARLY, MONTHLY, WEEKLY, DAILY,
                  HOURLY, MINUTELY, SECONDLY,
                  MO, TU, WE, TH, FR, SA, SU)

        for var in rr_all:
            self.assertIsNot(var, None)

        # In the public interface but not in all
        from dateutil2.rrule import weekday
        self.assertIsNot(weekday, None)


class ImportTZTest(unittest.TestCase):
    """ Test that dateutil2.tz related imports work properly """
    def testTzDirect(self):
        import dateutil2.tz

    def testTzFrom(self):
        from dateutil2 import tz

    def testTzAll(self):
        from dateutil2.tz import tzutc
        from dateutil2.tz import tzoffset
        from dateutil2.tz import tzlocal
        from dateutil2.tz import tzfile
        from dateutil2.tz import tzrange
        from dateutil2.tz import tzstr
        from dateutil2.tz import tzical
        from dateutil2.tz import gettz
        from dateutil2.tz import tzwin
        from dateutil2.tz import tzwinlocal
        from dateutil2.tz import UTC
        from dateutil2.tz import datetime_ambiguous
        from dateutil2.tz import datetime_exists
        from dateutil2.tz import resolve_imaginary

        tz_all = ["tzutc", "tzoffset", "tzlocal", "tzfile", "tzrange",
                  "tzstr", "tzical", "gettz", "datetime_ambiguous",
                  "datetime_exists", "resolve_imaginary", "UTC"]

        tz_all += ["tzwin", "tzwinlocal"] if sys.platform.startswith("win") else []
        lvars = locals()

        for var in tz_all:
            self.assertIsNot(lvars[var], None)

@unittest.skipUnless(sys.platform.startswith('win'), "Requires Windows")
class ImportTZWinTest(unittest.TestCase):
    """ Test that dateutil2.tzwin related imports work properly """
    def testTzwinDirect(self):
        import dateutil2.tzwin

    def testTzwinFrom(self):
        from dateutil2 import tzwin

    def testTzwinStar(self):
        from dateutil2.tzwin import tzwin
        from dateutil2.tzwin import tzwinlocal

        tzwin_all = [tzwin, tzwinlocal]

        for var in tzwin_all:
            self.assertIsNot(var, None)


class ImportZoneInfoTest(unittest.TestCase):
    def testZoneinfoDirect(self):
        import dateutil2.zoneinfo

    def testZoneinfoFrom(self):
        from dateutil2 import zoneinfo

    def testZoneinfoStar(self):
        from dateutil2.zoneinfo import gettz
        from dateutil2.zoneinfo import gettz_db_metadata
        from dateutil2.zoneinfo import rebuild

        zi_all = (gettz, gettz_db_metadata, rebuild)

        for var in zi_all:
            self.assertIsNot(var, None)
