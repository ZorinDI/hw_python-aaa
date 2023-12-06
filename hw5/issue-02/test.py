from morse import decode
import pytest


@pytest.mark.parametrize(
    "from_morse_to_string,morse",
    [
        ('.-', 'A'),
        ('... --- ...', "SOS"),
        ('.-   -...   -....-', "AB-"),
        ('.... . .-.. .-.. --- .-- --- .-. .-.. -.. ..--..', 'HELLOWORLD?'),
        ('', ''),
    ]
)
def test_from_morse(from_morse_to_string, morse):
    assert decode(from_morse_to_string) == morse


if __name__ == "__main__":
    """"""
    pass
