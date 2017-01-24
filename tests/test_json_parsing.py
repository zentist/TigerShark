import unittest
import logging
import sys


from tigershark.facade import f835, f271
from tigershark.parsers import M835_4010_X091_A1, M271_4010_X092_A1, M835_5010_X221_A1, M271_5010_X279_A1


class TestJSONFunction(unittest.TestCase):
    def test_json_835(self):
        m = M835_4010_X091_A1.parsed_835
        with open('tests/835-example.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        f = f835.F835_4010(parsed)
        try:
            f.to_json()
        except TypeError:
            self.fail(".to_json() raised TypeError")

    def test_json_271(self):
        m = M271_4010_X092_A1.parsed_271
        with open('tests/271-example.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        f = f271.F271_4010(parsed)
        try:
            f.to_json()
        except TypeError:
            self.fail(".to_json() raised TypeError")

    def test_json_835_5010(self):
        m = M835_5010_X221_A1.parsed_835
        with open('tests/5010-835-example-1.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        f = f835.F835_5010(parsed)
        try:
            f.to_json()
        except TypeError:
            self.fail(".to_json() raised TypeError")

    def test_json_271_5010(self):
        m = M271_5010_X279_A1.parsed_271
        with open('tests/5010-271-example-1.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        f = f271.F271_5010(parsed)
        try:
            f.to_json()
        except TypeError:
            self.fail(".to_json() raised TypeError")

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
