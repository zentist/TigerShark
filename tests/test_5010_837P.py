import datetime
from decimal import Decimal
import unittest

from tigershark.parsers.M837_5010_X222_A1 import parsed_837


class TestParserX222A1(unittest.TestCase):
    def test_financial_information(self):
        with open('tests/5010-837-professional-example.txt') as f:
            parsed = parsed_837.unmarshall(f.read().strip())

        segments = parsed.segs()

        self.assertEqual(len(segments), 45)
        self.assertEqual(
            [str(x) for x in segments[1].elements],
            [
                "GS",
                "HC",
                "XXXXXXX",
                "XXXXX",
                "20170617",
                "1741",
                "101",
                "X",
                "005010X222A1"
            ]
        )
        segment_first_nm1 = parsed.descendant("segment", "NM1")[0]
        self.assertEqual(
            [str(x) for x in segment_first_nm1.elements],
            [
                "NM1",
                "41",
                "2",
                "SUBMITTER",
                "",
                "",
                "",
                "",
                "46",
                "ABC123"
            ]
        )