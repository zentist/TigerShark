import datetime
import os
import unittest

from tigershark.facade.common import IdentifyingHeaders
from tigershark.parsers import IdentifyingParser


class TestIdentifyingHeaders(unittest.TestCase):

    def parse_file(self, name):
        with open(os.path.join('tests', name)) as f:
            parsed = IdentifyingParser.unmarshall(
                f.read().strip(), ignoreExtra=True)
        return IdentifyingHeaders(parsed)

    def test_5010_details(self):
        facade = self.parse_file('5010-835-example-1.txt')

        control = facade.interchange_controls[0]

        self.assertEqual(control.authorization_information_qualifier, '00')
        self.assertEqual(control.authorization_information, '          ')

        self.assertEqual(control.security_information_qualifier, '00')
        self.assertEqual(control.security_information, '          ')

        self.assertEqual(control.interchange_sender_id_qualifier, 'ZZ')
        self.assertEqual(control.interchange_sender_id, '5010TEST       ')

        self.assertEqual(control.interchange_receiver_id_qualifier, 'ZZ')
        self.assertEqual(control.interchange_receiver_id, '835RECVR       ')

        self.assertEqual(control.interchange_date, datetime.date(2011, 9, 30))
        self.assertEqual(control.interchange_time, datetime.time(11, 5))

        self.assertEqual(control.interchange_control_standards_id, '^')
        self.assertEqual(control.interchange_control_version_number, '00501')
        self.assertEqual(control.interchange_control_number, '000004592')

        self.assertEqual(control.acknowledgement_requested, '0')
        self.assertEqual(control.test_indicator, 'T')
        self.assertEqual(control.subelement_separator, '|')

        group = control.functional_groups[0]

        self.assertEqual(group.functional_id_code, 'HP')

        self.assertEqual(group.application_sender_code, '5010TEST')
        self.assertEqual(group.application_receiver_code, '835RECVR')

        self.assertEqual(group.date, datetime.date(2011, 9, 30))
        self.assertEqual(group.time, datetime.time(10, 7, 18))

        self.assertEqual(group.group_control_number, '45920001')

        self.assertEqual(group.responsible_agency_code, 'X')

        self.assertEqual(group.version_indicator_code, '005010X221A1')

        self.assertEqual(group.version_tuple, (5, 1, 0))

    def test_4010_details(self):
        facade = self.parse_file('271-example.txt')

        control = facade.interchange_controls[0]

        self.assertEqual(control.authorization_information_qualifier, '00')
        self.assertEqual(control.authorization_information, '          ')

        self.assertEqual(control.security_information_qualifier, '00')
        self.assertEqual(control.security_information, '          ')

        self.assertEqual(control.interchange_sender_id_qualifier, 'ZZ')
        self.assertEqual(control.interchange_sender_id, 'ZIRMED         ')

        self.assertEqual(control.interchange_receiver_id_qualifier, 'ZZ')
        self.assertEqual(control.interchange_receiver_id, '12345          ')

        self.assertEqual(control.interchange_date, datetime.date(2012, 6, 5))
        self.assertEqual(control.interchange_time, datetime.time(23, 24))

        self.assertEqual(control.interchange_control_standards_id, 'U')
        self.assertEqual(control.interchange_control_version_number, '00401')
        self.assertEqual(control.interchange_control_number, '000050033')

        self.assertEqual(control.acknowledgement_requested, '1')
        self.assertEqual(control.test_indicator, 'P')
        self.assertEqual(control.subelement_separator, '^')

        group = control.functional_groups[0]

        self.assertEqual(group.functional_id_code, 'HB')

        self.assertEqual(group.application_sender_code, 'ZIRMED')
        self.assertEqual(group.application_receiver_code, '12345')

        self.assertEqual(group.date, datetime.date(2012, 6, 5))
        self.assertEqual(group.time, datetime.time(23, 24))

        self.assertEqual(group.group_control_number, '50025')

        self.assertEqual(group.responsible_agency_code, 'X')

        self.assertEqual(group.version_indicator_code, '004010X092A1')

        self.assertEqual(group.version_tuple, (4, 1, 0))
