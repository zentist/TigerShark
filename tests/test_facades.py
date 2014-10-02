import os
import unittest

from tigershark import X12VersionTuple
from tigershark.facade import FACADE_MAP
from tigershark.facade import get_facade
from tigershark.parsers import SimpleParser

from tests import TEST_FILE_MAP


class TestGenericParsing(unittest.TestCase):

    def test_all_loadable(self):
        for transaction_set_id in FACADE_MAP:
            for version in FACADE_MAP[transaction_set_id]:
                version_tuple = X12VersionTuple(version, 1, 0, '')
                get_facade(transaction_set_id, version_tuple)

    def test_all_facadable(self):
        for (transaction_set_id, version_tuple), name in TEST_FILE_MAP.iteritems():  # nopep8
            if transaction_set_id not in FACADE_MAP:
                continue
            if version_tuple.version not in FACADE_MAP[transaction_set_id]:
                continue

            with open(os.path.join('tests', name)) as f:
                contents = f.read().replace('\n', '')

            parser = SimpleParser(transaction_set_id, version_tuple)
            x12 = parser.unmarshall(contents)
            facade = get_facade(transaction_set_id, version_tuple)(x12)

            self.assertEqual(facade.x12_version_string,
                             version_tuple.version_string)
            self.assertEqual(facade.transaction_set_identifier_code,
                             transaction_set_id)
