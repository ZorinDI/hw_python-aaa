from morse import encode
from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string,result", "from_morse_to_string,morse",
    [
        ("A", '.-'),
        ("SOS", '... --- ...'),
        ("A B -", '.-   -...   -....-'),
        ("", ''),
    ],
    [
        ('.-', 'A'),
        ('... --- ...', "SOS"),
        ('.-   -...   -....-', "A B -"),
        ('', ''),
    ]
)
def from_sting(source_string, result):
    assert encode(source_string) == result


def from_morse(from_morse_to_string, morse):
    assert decode(from_morse_to_string) == morse
