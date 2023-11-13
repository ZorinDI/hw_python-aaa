from one_hot_encoder import fit_transform
import unittest


class Testing(unittest.TestCase):
    def test_capitals(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_number(self):
        actual = fit_transform([2, 3, 1])
        expected = [
            (2, [0, 0, 1]),
            (3, [0, 1, 0]),
            (1, [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_wrong_types_ex(self):
        actual = ['Moscow', 'New York', 1, 2]
        expected = [
            'Moscow',
            'New York',
            1,
            2
        ]
        self.assertEqual(actual, expected)

    def test_with_nothing(self):
        self.assertRaises(TypeError, fit_transform)


if __name__ == "__main__":
    unittest.main()
