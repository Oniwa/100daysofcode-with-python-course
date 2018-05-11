from datetime import datetime, timedelta

import pytest

from bite7 import convert_to_datetime, time_between_shutdowns

def test_convert_to_datetime():
    assert convert_to_datetime('INFO 2014-07-03T23:27:51 supybot'
                               ' Shutdown complete.') == datetime(2014, 7, 3,
                                                                  23, 27, 51)

def test_time_between_shutdowns_1():
    assert time_between_shutdowns(['INFO 2014-07-03T23:27:51 supybot '
                                   'Shutdown initiated.', 'INFO 2014-07-03T23:27'
                                                          ':51 supybot Shutdown '
                                                          'complete.']) == timedelta(minutes=0, seconds=0)

def test_time_between_shutdowns_2():
    assert time_between_shutdowns(['INFO 2014-07-03T23:27:51 supybot '
                                   'Shutdown initiated.', 'INFO 2014-07-03T23:31:22 supybot Shutdown complete.']) == timedelta(minutes=3, seconds=31)