from one_hot_encoder import fit_transform
import pytest


def test_capitals():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_number():
    actual = fit_transform([2, 3, 1])
    expected = [
        (2, [0, 0, 1]),
        (3, [0, 1, 0]),
        (1, [1, 0, 0])
    ]
    assert actual == expected


def test_with_nothing():
    with pytest.raises(TypeError):
        fit_transform()


def test_wrong_types():
    with pytest.raises(TypeError):
        fit_transform([['A']])


def test_range_to_list():
    assert isinstance(fit_transform(range(5)), list)


if __name__ == "__main__":
    pytest.main()
