import unittest

from src.utils import Formatter

valid_data = {"foo": "bar", "types": {"status": 1, "code": 2.3}}
expected_formatted_data = {"foo": {"_S": "bar"}, "types": {"status": {"_I": 1}, "code": {"_R": 2.3}}}


class TestFormatter(unittest.TestCase):
    def test_with_valid_data(self) -> None:
        formatted_data = Formatter.format(valid_data)
        self.assertIsInstance(formatted_data, dict)
        self.assertEqual(formatted_data, expected_formatted_data)

    def test_unformat_data(self) -> None:
        unformatted_data = Formatter.unformat(
            {"foo": {"_S": "bar"}, "types": {"status": {"_I": "1"}, "code": {"_R": "2.3"}}}
        )
        self.assertIsInstance(unformatted_data, dict)
        self.assertEqual(unformatted_data, unformatted_data)
