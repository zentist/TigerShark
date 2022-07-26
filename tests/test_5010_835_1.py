import datetime
from decimal import Decimal
import unittest

from tigershark.facade import f835
from tigershark.parsers.M835_5010_X221_A1 import parsed_835


class TestParsed835(unittest.TestCase):
    def setUp(self):
        with open('tests/5010-835-example-1.txt') as f:
            parsed = parsed_835.unmarshall(f.read().strip())
        self.facade = f835.F835_5010(parsed).facades[0]

    def test_root_information(self):
        fi = self.facade
        self.assertEqual(
            fi.transaction_set_control_number, '0001'
        )

    def test_financial_information(self):
        fi = self.facade.header.financial_information
        self.assertEqual(
            fi.transaction_type,
            ('I', 'Remittance Information Only'))
        self.assertEqual(fi.amount, Decimal('1790.00'))
        self.assertEqual(fi.credit_or_debit, ('C', 'Credit'))
        self.assertEqual(fi.payment_method, ('CHK', 'Check'))
        self.assertIsNone(fi.payment_format)
        self.assertIsNone(fi.sender_aba_transit_routing_number)
        self.assertIsNone(
            fi.sender_canadian_bank_branch_and_institution_number)
        self.assertIsNone(fi.sender_account_type)
        self.assertEqual(fi.sender_bank_account_number, '')
        self.assertEqual(fi.sender_id, '')
        self.assertEqual(fi.sender_supplemental_id, '')
        self.assertIsNone(fi.receiver_aba_transit_routing_number)
        self.assertIsNone(
            fi.receiver_canadian_bank_branch_and_institution_number)
        self.assertIsNone(fi.receiver_account_type)
        self.assertEqual(fi.receiver_bank_account_number, '')
        self.assertEqual(fi.issue_date, datetime.date(2011, 9, 30))

    def test_reassociation_trace_number(self):
        rtn = self.facade.header.reassociation_trace_number
        self.assertEqual(rtn.trace_type,
                         ('1', 'Current Transaction Trace Numbers'))
        self.assertEqual(rtn.check_or_eft_trace_number, '123456789')
        self.assertEqual(rtn.payer_id, '1123456789')
        self.assertEqual(rtn.originating_company_supplemental_code, '')

    def test_currency_information(self):
        ci = self.facade.header.currency_information
        self.assertIsNone(ci.currency_code)
        self.assertIsNone(ci.exchange_rate)

    def test_receiver(self):
        receiver = self.facade.header.receiver
        self.assertEqual(receiver.id, '5010835EXAMPLE')
        self.assertEqual(receiver.description, '')
        self.assertEqual(receiver.reference_id, '')

    def test_version(self):
        version = self.facade.header.version
        self.assertIsNone(version.version_number)
        self.assertIsNone(version.description)
        self.assertIsNone(version.reference_id)

    def test_production_date(self):
        self.assertEqual(self.facade.header.production_date.date,
                         datetime.date(2011, 9, 30))

    def test_payer(self):
        payer = self.facade.payer
        self.assertIsNone(payer.payer_id)
        self.assertIsNone(payer.submitter_id)
        self.assertIsNone(payer.hin)
        self.assertIsNone(payer.naic_code)

        cd = payer.contact_details
        self.assertEqual(cd.name, 'DENTAL PAYER NAME')

    def test_payee(self):
        payee = self.facade.payee
        self.assertIsNone(payee.state_license)
        self.assertEqual(payee.tax_id, '123456789')

    def test_claims_overview(self):
        co = self.facade.claims_overview
        self.assertEqual(co.number, '1')

    def test_claims(self):
        self.assertEqual(len(self.facade.claims), 3)

    def test_claim_1(self):
        claim = self.facade.claims[0]
        self.assertEqual(claim.date_received, datetime.date(2011, 9, 8))
        self.assertEqual(
            claim.date_statement_period_start,
            datetime.date(1900, 1, 1))
        self.assertEqual(
            claim.claim_adjustments.patient_responsibility.amount_1,
            Decimal('0.0'))
        self.assertEqual(
            claim.claim_adjustments.contractual_obligation.amount_1,
            Decimal('0.0'))

        self.assertEqual(
            claim.payment_info.patient_control_number,
            'PRECERTIFICATION')
        self.assertEqual(claim.patient.first_name, 'PATIENT')
        self.assertEqual(claim.group_or_policy_number, '11223344')
        self.assertEqual(claim.contract_class, 'CONTRACTING')

        self.assertEqual(len(claim.line_items), 7)

        line_item = claim.line_items[0]
        self.assertEqual(line_item.charge, Decimal('90'))
        self.assertEqual(line_item.payment, Decimal('80'))
        self.assertEqual(line_item.quantity, '1')
        self.assertEqual(line_item.provider_control_number, '00010')
        self.assertEqual(line_item.allowed_amount, Decimal('80'))
        self.assertEqual(
            line_item.claim_adjustments.patient_responsibility.amount_1,
            Decimal('0.0'))
        self.assertEqual(
            line_item.claim_adjustments.contractual_obligation.amount_1,
            Decimal('10.0'))

    def test_footer(self):
        footer = self.facade.footer
        self.assertIsNone(footer)

if __name__ == "__main__":
    unittest.main()
