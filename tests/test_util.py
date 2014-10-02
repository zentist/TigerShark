import os
import unittest

from tigershark.X12.parse import ParseError
from tigershark.facade import FACADE_MAP
from tigershark.util import apply_facade_to_simple_x12
from tigershark.util import identify_simple_x12

from tests import TEST_FILE_MAP


class TestUtil(unittest.TestCase):

    def test_all_identifiable(self):
        all_tests = sorted(TEST_FILE_MAP.iteritems())

        for expected, name in all_tests:
            with open(os.path.join('tests', name)) as f:
                x12_contents = f.read().replace('\n', '')
            self.assertEqual(expected, identify_simple_x12(x12_contents))

    def test_parse_error(self):
        with self.assertRaises(ParseError):
            identify_simple_x12('not x12')

    def test_apply_facade(self):
        all_tests = sorted(TEST_FILE_MAP.iteritems())

        for (transaction_set_id, version_tuple), name in all_tests:
            with open(os.path.join('tests', name)) as f:
                x12_contents = f.read().replace('\n', '')

            facadable = (
                transaction_set_id in FACADE_MAP
                and version_tuple.version in FACADE_MAP[transaction_set_id]
            )

            if facadable:
                facade = apply_facade_to_simple_x12(x12_contents)

                self.assertEqual(facade.x12_version_string,
                                 version_tuple.short_string)
                self.assertEqual(facade.transaction_set_identifier_code,
                                 transaction_set_id)
            else:
                with self.assertRaises(ValueError):
                    apply_facade_to_simple_x12(x12_contents)
