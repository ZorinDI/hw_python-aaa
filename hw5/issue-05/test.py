from what_is_year_now import what_is_year_now
from unittest.mock import patch
import urllib.request
from io import StringIO
import pytest


def test_ymd():
    date = StringIO('{"currentDateTime": "2023-12-05T2:28Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
    expected = 2023
    assert actual == expected


def test_dmy():
    date = StringIO('{"currentDateTime": "05.12.2023T21:29Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual = what_is_year_now()
    expected = 2023
    assert actual == expected


def test_wrong_date():
    date = StringIO('{"currentDateTime": "05/12/2023"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()