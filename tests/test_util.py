import os
import unittest

from tigershark.X12.parse import ParseError
from tigershark.util import identify_simple_x12

from tests import TEST_FILE_MAP


class TestUtil(unittest.TestCase):

    def test_all_identifiable(self):
        all_tests = sorted(TEST_FILE_MAP.iteritems())
        for expected, name in all_tests:
            with open(os.path.join('tests', name)) as f:
                x12_contents = f.read()
            self.assertEqual(expected, identify_simple_x12(x12_contents))

    def test_parse_error(self):
        with self.assertRaises(ParseError):
            identify_simple_x12('not x12')
