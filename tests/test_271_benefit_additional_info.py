import unittest
import logging
import sys


from tigershark.facade import f271
from tigershark.parsers import M271_5010_X279_A1


class TestBenefitAdditionalInfo(unittest.TestCase):
    def test_benefit_additional_info(self):
        m = M271_5010_X279_A1.parsed_271
        with open('tests/271-example-3.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        f = f271.F271_5010(parsed)

        subscriber = f.facades[0].subscribers[0]
        benefit_row = subscriber.eligibility_or_benefit_information[11]
        additional_information = benefit_row.additional_information[0]
        self.assertEqual(additional_information, ('11', 'Office'))
        self.assertEqual(len(benefit_row.messages), 4)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
