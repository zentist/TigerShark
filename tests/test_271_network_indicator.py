import unittest
import logging
import sys

from tigershark.facade import f271
from tigershark.parsers import M271_5010_X279_A1


class TestParsed271(unittest.TestCase):
    def setUp(self):
        m = M271_5010_X279_A1.parsed_271
        with open('tests/271-example-in-out-network.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        self.f = f271.F271_5010(parsed)

    def test_number_of_facades(self):
        self.assertEqual(len(self.f.facades), 1)

    def test_no_network_info(self):
        subscriber = self.f.facades[0].subscribers[0]
        benefit = subscriber.eligibility_or_benefit_information[2]
        cov_info = benefit.coverage_information

        self.assertEqual(cov_info.in_plan_network_type, None)
        self.assertEqual(cov_info.in_plan_network, False)
        self.assertEqual(cov_info.both_in_out_network, False)
        self.assertEqual(cov_info.out_of_plan_network, False)

    def test_both_network_info(self):
        subscriber = self.f.facades[0].subscribers[0]
        benefit = subscriber.eligibility_or_benefit_information[17]
        cov_info = benefit.coverage_information

        self.assertEqual(cov_info.in_plan_network_type[0], "W")
        self.assertEqual(cov_info.in_plan_network, False)
        self.assertEqual(cov_info.both_in_out_network, True)
        self.assertEqual(cov_info.out_of_plan_network, False)

    def test_out_of_network_info(self):
        subscriber = self.f.facades[0].subscribers[0]
        benefit = subscriber.eligibility_or_benefit_information[16]
        cov_info = benefit.coverage_information

        self.assertEqual(cov_info.in_plan_network_type[0], "N")
        self.assertEqual(cov_info.in_plan_network, False)
        self.assertEqual(cov_info.both_in_out_network, False)
        self.assertEqual(cov_info.out_of_plan_network, True)

    def test_in_network_info(self):
        subscriber = self.f.facades[0].subscribers[0]
        benefit = subscriber.eligibility_or_benefit_information[15]
        cov_info = benefit.coverage_information

        self.assertEqual(cov_info.in_plan_network_type[0], "Y")
        self.assertEqual(cov_info.in_plan_network, True)
        self.assertEqual(cov_info.both_in_out_network, False)
        self.assertEqual(cov_info.out_of_plan_network, False)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
