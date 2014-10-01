import datetime
import unittest

from tigershark.facade import D8


class TestD8(unittest.TestCase):

    def test_parse_none(self):
        self.assertEqual(D8.x12_to_python(None), None)

    def test_parse_CCYYMMDD(self):
        self.assertEqual(D8.x12_to_python('19790405'),
                         datetime.date(1979, 4, 5))

    def test_parse_YYMMDD(self):
        self.assertEqual(
            D8.x12_to_python('140405'),
            datetime.date(2014, 4, 5))

    def test_to_x12_none(self):
        self.assertEqual(D8.python_to_x12(None), '')

    def test_to_x12_date(self):
        self.assertEqual(
            D8.python_to_x12(datetime.date(2014, 4, 5)),
            '20140405')
