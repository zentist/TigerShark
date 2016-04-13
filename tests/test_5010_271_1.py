from decimal import Decimal
import unittest

from tigershark.facade import f271
from tigershark.parsers.M271_5010_X279_A1 import parsed_271


class TestParsed271(unittest.TestCase):
    def setUp(self):
        with open('tests/5010-271-example-1.txt') as f:
            parsed = parsed_271.unmarshall(f.read().strip())
        self.facade = f271.F271_5010(parsed).facades[0]

    def test_financial_information(self):
        eobi = self.facade.subscribers[0].eligibility_or_benefit_information
        self.assertEqual(
            eobi[0].coverage_information.service_type,
            ('30', 'Health Benefit Plan Coverage'))
        self.assertEqual(
            eobi[0].coverage_information.insurance_type,
            ('EP', 'Exclusive Provider Organization'))
        self.assertEqual(eobi[0].coverage_information.description, '')
        self.assertEqual(eobi[1].coverage_information.benefit_amount, Decimal(0))
        self.assertEqual(eobi[1].coverage_information.benefit_percent, Decimal(0))
        self.assertEqual(eobi[1].coverage_information.information_type,
                         ('W', 'Other Source of Data'))

    def test_subscriber_information(self):
        subscriber = self.facade.subscribers[0]
        location = subscriber.personal_information.address_location
        self.assertEqual(location.city, 'KANSAS CITY')
        self.assertEqual(location.state, 'MO')
        self.assertEqual(location.zip, '64108')
        street = subscriber.personal_information.address_street
        self.assertEqual(street.addr1, '4040 VILLAGE AB')
        self.assertEqual(street.addr2, '')
        dates = subscriber.personal_information.dates
        self.assertEqual(dates[0].time.strftime('%Y-%m-%d'), '2016-02-01')
        self.assertEqual(dates[0].type, ('346', 'Plan Begin'))
        self.assertEqual(dates[1].time.strftime('%Y-%m-%d'), '2016-06-01')
        self.assertEqual(dates[1].type, ('472', 'Service'))
        self.assertEqual(dates[2].time.strftime('%Y-%m-%d'), '2014-12-08')
        self.assertEqual(dates[2].type, ('356', 'Eligibility Begin'))
        demographic = subscriber.personal_information.demographic_information
        self.assertEqual(demographic.birth_date.strftime('%Y-%m-%d'), '1943-08-13')
        self.assertEqual(demographic.gender, ('M', 'Male'))
        name = subscriber.personal_information.name
        self.assertEqual(name.entity_identifier, ('IL', 'Insured'))
        self.assertEqual(name.entity_type, ('1', 'Person'))
        self.assertEqual(name.first_name, 'JOHN')
        self.assertEqual(name.id_code, '1234567899')
        self.assertEqual(name.id_code_qual, ('MI', 'Member Identification Number'))
        self.assertEqual(name.last_name, 'SMITH')
        self.assertTrue(name.is_person)
        reference_ids = subscriber.personal_information.reference_ids
        self.assertEqual(reference_ids[0].reference_id, '0404044')
        self.assertEqual(reference_ids[0].reference_id_qualifier, ('18', 'Plan Number'))
        self.assertEqual(reference_ids[1].reference_id, '030030001000120')
        self.assertEqual(reference_ids[1].reference_id_qualifier, ('6P', 'Group Number'))
        self.assertEqual(reference_ids[1].description, 'NEVADA EXCHANGE')
        relationship = subscriber.personal_information.relationship
        self.assertTrue(relationship.is_insured)
        self.assertEqual(relationship.maintenance_reason, ('25', 'Change in Identifying Data Elements'))
        self.assertEqual(relationship.maintenance_type, ('001', 'Change'))
        self.assertEqual(relationship.relationship, ('18', 'Self'))

    def test_receiver(self):
        r_name = self.facade.receivers[0].receiver_information.name
        self.assertEqual(r_name.entity_identifier, ('1P', 'Provider'))
        self.assertEqual(r_name.entity_type, ('1', 'Person'))
        self.assertEqual(r_name.first_name, 'Barraret')
        self.assertEqual(r_name.id_code, '1234567894')
        self.assertEqual(r_name.id_code_qual,
             ('XX', 'Health Care Financing Administration National Provider Identifier'))
        self.assertTrue(r_name.is_person)
        self.assertEqual(r_name.middle_initial, 'J.')
        self.assertEqual(r_name.last_name, 'James')

    def test_version(self):
        self.assertEqual(self.facade.transaction_set_identifier_code, '271')
        self.assertEqual(self.facade.x12_version_string, '5010')

    def test_payer(self):
        eobi = self.facade.subscribers[0].eligibility_or_benefit_information
        benefit_related_entity = eobi[1].benefit_related_entity
        self.assertEqual(benefit_related_entity.address_location.city, 'El Fixato')
        self.assertEqual(benefit_related_entity.address_location.state, 'TX')
        self.assertEqual(benefit_related_entity.address_location.zip, '68887')
        self.assertEqual(benefit_related_entity.address_street.addr1, 'PO Box 983322')
        self.assertEqual(benefit_related_entity.name.entity_identifier, ('PR', 'Payer'))
        self.assertEqual(benefit_related_entity.name.entity_type,
                         ('2', 'Non-Person Entity'))
        self.assertTrue(benefit_related_entity.name.is_organization)
        self.assertEqual(benefit_related_entity.name.org_name, 'Mala Compania')

    def test_header(self):
        header = self.facade.header
        self.assertIsNone(header)

if __name__ == "__main__":
    unittest.main()
