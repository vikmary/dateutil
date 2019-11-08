"""Test for the "import *" functionality.

As import * can be only done at module level, it has been added in a separate file
"""
import pytest

prev_locals = list(locals())
from dateutil2 import *
new_locals = {name:value for name,value in locals().items()
              if name not in prev_locals}
new_locals.pop('prev_locals')


@pytest.mark.import_star
def test_imported_modules():
    """ Test that `from dateutil2 import *` adds modules in __all__ locally """
    import dateutil2.easter
    import dateutil2.parser
    import dateutil2.relativedelta
    import dateutil2.rrule
    import dateutil2.tz
    import dateutil2.utils
    import dateutil2.zoneinfo

    assert dateutil2.easter == new_locals.pop("easter")
    assert dateutil2.parser == new_locals.pop("parser")
    assert dateutil2.relativedelta == new_locals.pop("relativedelta")
    assert dateutil2.rrule == new_locals.pop("rrule")
    assert dateutil2.tz == new_locals.pop("tz")
    assert dateutil2.utils == new_locals.pop("utils")
    assert dateutil2.zoneinfo == new_locals.pop("zoneinfo")

    assert not new_locals
