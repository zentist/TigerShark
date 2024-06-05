from __future__ import print_function

from build.lib.tigershark.facade import Money
from tigershark.facade import DR, TM, SegmentAccess, X12LoopBridge
from tigershark.facade import X12SegmentBridge
from tigershark.facade import ElementAccess
from tigershark.facade import SegmentSequenceAccess
from tigershark.facade import SegmentConversion
from tigershark.facade import ElementSequenceAccess
from tigershark.facade import D8
from tigershark.facade import Facade
from tigershark.facade import enum, boolean
from tigershark.facade.common import ClaimAdjustment
from tigershark.facade.utils import first
from tigershark.facade.enums.common import id_code_qualifier, reference_id_qualifier, date_or_time_qualifier


class F837d(Facade, X12LoopBridge):

    @staticmethod
    def loops(theClass, anX12Message):
        return [theClass(loop) for loop in anX12Message.descendant("loop", theClass.loopName)]

    def __init__(self, anX12Message):
        self.transaction_set_header = first(self.loops(TransactionSetHeader, anX12Message))
        self.header = first(self.loops(Header, anX12Message))
        self.submitter = self.loops(Submitter, anX12Message)
        self.receiver = self.loops(Receiver, anX12Message)
        self.billing_provider = self.loops(BillingProvider, anX12Message)
        self.subscriber = self.loops(Subscriber, anX12Message)
        self.patient = self.loops(Patient, anX12Message)


class TransactionSetHeader(X12LoopBridge):
    loopName = "ST_LOOP"
    transaction_set_identifier_code = ElementAccess("ST", 1)
    transaction_set_control_number = ElementAccess("ST", 2)
    x12_version_string = ElementAccess("ST", 3)


class NamedEntity(X12SegmentBridge):
    entity_identifier = ElementAccess(
        "NM1",
        1,
        x12type=enum(
            {
                "41": "Submitter",
                "87": "Pay-to Provider",
                "PE": "Payee",
                "DN": "Referring Provider",
                "P3": "Primary Care Provider",
                "82": "Rendering Provider",
                "77": "Service Location",
                "DD": "Assistant Surgeon",
                "DQ": "Supervising Physician",
                "IL": "Insured or Subscriber",
                "PR": "Payer",
            },
            raw_unknowns=True,
        ),
    )
    entity_type = ElementAccess("NM1", 2, x12type=enum({"1": "Person", "2": "Non-Person Entity"}))

    last_name_or_org_name = ElementAccess("NM1", 3)
    first_name = ElementAccess("NM1", 4)
    middle_name = ElementAccess("NM1", 5)

    prefix = ElementAccess("NM1", 6)
    suffix = ElementAccess("NM1", 7)
    id_code_qual = ElementAccess("NM1", 8, x12type=enum(id_code_qualifier))
    id_code = ElementAccess("NM1", 9)

    @property
    def is_person(self):
        return self.entity_type[0] == "1"

    @property
    def is_organization(self):
        return self.entity_type[0] == "2"


class DateOrTimePeriod(X12SegmentBridge):
    date_type = ElementAccess("DTP", 1, x12type=enum(date_or_time_qualifier))
    date_or_time = ElementAccess("DTP", 3, x12type=D8, qualifier=(2, "D8"))
    date_or_time_range = ElementAccess("DTP", 3, x12type=DR, qualifier=(2, "RD8"))


class ReferenceID(X12SegmentBridge):
    reference_id_qualifier = ElementAccess("REF", 1, x12type=enum(reference_id_qualifier))
    reference_id = ElementAccess("REF", 2)
    description = ElementAccess("REF", 3)


class ContactInformation(X12SegmentBridge):
    contact_code = ElementAccess("PER", 1, x12type=enum({"IC": "Information Contact"}, raw_unknowns=True))
    contact_name = ElementAccess("PER", 2)
    contact_edi = ElementAccess("PER", oneOf=("ED", (3, 4), (5, 6), (7, 8)))
    contact_email = ElementAccess("PER", oneOf=("EM", (3, 4), (5, 6), (7, 8)))
    contact_fax = ElementAccess("PER", oneOf=("FX", (3, 4), (5, 6), (7, 8)))
    contact_home_phone = ElementAccess("PER", oneOf=("HP", (3, 4), (5, 6), (7, 8)))
    contact_work_phone = ElementAccess("PER", oneOf=("WP", (3, 4), (5, 6), (7, 8)))
    contact_phone = ElementAccess("PER", oneOf=("TE", (3, 4), (5, 6), (7, 8)))
    contact_phone_ext = ElementAccess("PER", oneOf=("EX", (3, 4), (5, 6), (7, 8)))


class Address(X12SegmentBridge):
    addr1 = ElementAccess("N3", 1)
    addr2 = ElementAccess("N3", 2)


class Location(X12SegmentBridge):
    city = ElementAccess("N4", 1)
    state = ElementAccess("N4", 2)
    zip = ElementAccess("N4", 3)
    country_code = ElementAccess("N4", 4)
    location_type = ElementAccess(
        "N4",
        5,
        x12type=enum(
            {
                "CY": "County/Parish",
                "FI": "Federal Information Processing Standards (FIPS) 55 (Named Populated Places)",
            },
            raw_unknowns=True,
        ),
    )
    location_id = ElementAccess("N4", 6)


class DemographicInformation(X12SegmentBridge):
    birth_date = ElementAccess("DMG", 2, x12type=D8, qualifier=(1, "D8"))
    gender = ElementAccess("DMB", 3, x12type=enum({"F": "Female", "M": "Male", "U": "Unknown"}))


class Hierarchy(X12SegmentBridge):
    id = ElementAccess("HL", 1)
    parent_id = ElementAccess("HL", 2)
    level = ElementAccess(
        "HL",
        3,
        x12type=enum(
            {
                "20": "Information Source",
                "21": "Information Receiver",
                "22": "Subscriber",
                "23": "Dependent",
            }
        ),
    )
    has_children = ElementAccess("HL", 4, x12type=boolean("1"))


class ProviderInformation(X12SegmentBridge):
    provider_code = ElementAccess(
        "PRV",
        1,
        x12type=enum(
            {
                "AD": "Admitting",
                "AT": "Attending",
                "BI": "Billing",
                "CO": "Consulting",
                "CV": "Covering",
                "H": "Hospital",
                "HH": "Home Health Care",
                "LA": "Laboratory",
                "OT": "Other Physician",
                "P1": "Pharmacist",
                "P2": "Pharmacy",
                "PC": "Primary Care Physician",
                "PE": "Performing",
                "R": "Rural Health Clinic",
                "RF": "Referring",
                "SB": "Submitting",
                "SK": "Skilled Nursing Facility",
                "SU": "Supervising",
            }
        ),
    )

    reference_id_qualifier = ElementAccess(
        "PRV",
        2,
        x12type=enum(
            {
                "9K": "Servicer",
                "D3": "National Association of Boards of Pharmacy Number",
                "EI": "Employer's Identification Number",
                "HPI": "Healthcare Financing Administration National Provider ID",
                "SY": "Social Security Number",
                "TJ": "Federal Taxpayer's Identification Number",
                "ZZ": "Mutually Defined",
                "PXC": "Health Care Provider Taxonomy Code",
            },
            raw_unknowns=True,
        ),
    )
    reference_id = ElementAccess("PRV", 3)


class Header(X12LoopBridge):
    loopName = "HEADER"

    class _HierarchicalTransaction(X12SegmentBridge):
        structure = ElementAccess(
            "BHT", 1, x12type=enum({"0019": "Information Source, Subscriber, Dependent"}, raw_unknowns=True)
        )
        purpose = ElementAccess("BHT", 2, x12type=enum({"00": "Original", "18": "Reissue}"}, raw_unknowns=True))
        transaction_id = ElementAccess("BHT", 3)
        creation_date = ElementAccess("BHT", 4, x12type=D8)
        creation_time = ElementAccess("BHT", 5, x12type=TM)
        type = ElementAccess(
            "BHT",
            6,
            x12type=enum({"31": "Subrogation Demand", "CH": "Chargeable", "RP": "Reporting"}, raw_unknowns=True),
        )

    hierarchical_transaction_info = SegmentAccess("BHT", x12type=SegmentConversion(_HierarchicalTransaction))


class Submitter(X12LoopBridge):
    loopName = "1000A"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    contact_information = SegmentSequenceAccess("PER", x12type=SegmentConversion(ContactInformation))


class Receiver(X12LoopBridge):
    loopName = "1000B"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))


class ReferringProvider(X12LoopBridge):
    loopName = "2310A"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    information = SegmentAccess("PRV", x12type=SegmentConversion(ProviderInformation))
    secondary_identification = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class RenderingProvider(X12LoopBridge):
    loopName = "2310B"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    information = SegmentAccess("PRV", x12type=SegmentConversion(ProviderInformation))
    secondary_identification = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class ServiceFacilityLocation(X12LoopBridge):
    loopName = "2310C"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    address = SegmentAccess("N3", x12type=SegmentConversion(Address))
    location = SegmentAccess("N4", x12type=SegmentConversion(Location))
    secondary_identification = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class AssistantSurgeon(X12LoopBridge):
    loopName = "2310D"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    information = SegmentAccess("PRV", x12type=SegmentConversion(ProviderInformation))
    secondary_identification = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class SupervisingProvider(X12LoopBridge):
    loopName = "2310E"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identification = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherSubscriberInformation(Facade, X12LoopBridge):
    loopName = "2320"

    class _OtherSubscriberInformation(X12SegmentBridge):
        code = ElementAccess(
            "SBR",
            1,
            x12type=enum(
                {
                    "A": "Payer Responsibility Four",
                    "B": "Payer Responsibility Five",
                    "C": "Payer Responsibility Six",
                    "D": "Payer Responsibility Seven",
                    "E": "Payer Responsibility Eight",
                    "F": "Payer Responsibility Nine",
                    "G": "Payer Responsibility Ten",
                    "H": "Payer Responsibility Eleven",
                    "P": "Primary",
                    "S": "Secondary",
                    "T": "Tertiary",
                    "U": "Unknown",
                }
            ),
        )
        rel = ElementAccess(
            "SBR",
            2,
            x12type=enum(
                {
                    "01": "Spouse",
                    "18": "Self",
                    "19": "Child",
                    "20": "Employee",
                    "21": "Unknown",
                    "39": "Organ Donor",
                    "40": "Cadaver Donor",
                    "53": "Life Partner",
                    "G8": "Other Relationship",
                }
            ),
        )
        insured_group_or_policy_number = ElementAccess("SBR", 3)
        other_insured_group_name = ElementAccess("SBR", 4)
        type_code = ElementAccess(
            "SBR",
            5,
            x12type=enum(
                {
                    "12": "Medicare Secondary Working Aged Beneficiary or Spouse with Employer Group Health Plan",
                    "13": "Medicare Secondary End-Stage Renal Disease Beneficiary in the Mandated Coordination Period with an Employer’s Group Health Plan",
                    "14": "Medicare Secondary, No-fault Insurance including Auto is Primary",
                    "15": "Medicare Secondary Worker’s Compensation",
                    "16": "Medicare Secondary Public Health Service (PHS)or Other Federal Agency",
                    "41": "Medicare Secondary Black Lung",
                    "42": "Medicare Secondary Veteran’s Administration",
                    "43": "Medicare Secondary Disabled Beneficiary Under Age 65 with Large Group Health Plan (LGHP)",
                    "47": "Medicare Secondary, Other Liability Insurance is Primary",
                }
            ),
        )
        type_code = ElementAccess(
            "SBR",
            6,
            x12type=enum(
                {
                    "11": "Other Non-Federal Programs",
                    "12": "Preferred Provider Organization (PPO)",
                    "13": "Point of Service (POS)",
                    "14": "Exclusive Provider Organization (EPO)",
                    "15": "Indemnity Insurance",
                    "16": "Health Maintenance Organization (HMO) Medicare Risk",
                    "17": "Dental Maintenance Organization",
                    "AM": "Automobile Medical",
                    "BL": "Blue Cross/Blue Shield",
                    "CH": "Champus",
                    "CI": "Commercial Insurance Co.",
                    "DS": "Disability",
                    "FI": "Federal Employees Program",
                    "HM": "Health Maintenance Organization",
                    "LM": "Liability Medical",
                    "MA": "Medicare Part A",
                    "MB": "Medicare Part B",
                    "MC": "Medicaid",
                    "OF": "Other Federal Program",
                    "TV": "Title V",
                    "VA": "Veterans Affairs Plan",
                    "WC": "Workers’ Compensation Health Claim",
                    "ZZ": "Mutually Defined",
                }
            ),
        )

    class _OtherInsuranceCoverageInformation(X12SegmentBridge):
        benefit_assignment_certififcation_indicator = ElementAccess(
            "OI", 3, x12type=enum({"N": "No", "Y": "Yes", "W": "Not Applicable"})
        )
        release_of_information_code = ElementAccess(
            "OI",
            6,
            x12type=enum(
                {
                    "I": "Informed Consent to Release Medical Information for Conditions or Diagnoses Regulated by Federal Statutes",
                    "Y": "Yes, Provider has a Signed Statement Permitting Release of Medical Billing Data Related to a Claim",
                }
            ),
        )

    class _OutpatientAdjudicationInformation(X12SegmentBridge):
        reimbursement_rate = ElementAccess("MOA", 1)
        payable_amount = ElementAccess("MOA", 2, x12type=Money)
        payment_remark_code_1 = ElementAccess("MOA", 3)
        payment_remark_code_2 = ElementAccess("MOA", 4)
        payment_remark_code_3 = ElementAccess("MOA", 5)
        payment_remark_code_4 = ElementAccess("MOA", 6)
        payment_remark_code_5 = ElementAccess("MOA", 7)
        payment_remark_code_6 = ElementAccess("MOA", 8)
        non_payable_amount = ElementAccess("MOA", 9, x12type=Money)

    class _ClaimAdjustments(X12LoopBridge):
        def __init__(self, aLoop, *args, **kwargs):
            super(OtherSubscriberInformation._ClaimAdjustments, self).__init__(aLoop, *args, **kwargs)
            self.contractual_obligation = ClaimAdjustment(aLoop, qualifier=(1, "CO"))
            self.correction_and_reversal = ClaimAdjustment(aLoop, qualifier=(1, "CR"))
            self.other = ClaimAdjustment(aLoop, qualifier=(1, "OA"))
            self.payor_initiated_reductions = ClaimAdjustment(aLoop, qualifier=(1, "PI"))
            self.patient_responsibility = ClaimAdjustment(aLoop, qualifier=(1, "PR"))

    subscriber_information = SegmentAccess("SBR", x12type=SegmentConversion(_OtherSubscriberInformation))
    payor_amount_paid = ElementAccess("AMT", 2, (1, "D"))
    amount_owed = ElementAccess("AMT", 2, (1, "EAF"))
    noncovered_charges_actual = ElementAccess("AMT", 2, (1, "A8"))
    other_insurance_coverage_information = SegmentAccess(
        "OI", x12type=SegmentConversion(_OtherInsuranceCoverageInformation)
    )
    outpatient_adjudication_information = SegmentAccess(
        "MOA", x12type=SegmentConversion(_OutpatientAdjudicationInformation)
    )

    def __init__(self, anX12Message, *args, **kwargs):
        super(OtherSubscriberInformation, self).__init__(anX12Message, *args, **kwargs)
        self.claim_adjustments = self._ClaimAdjustments(anX12Message)
        self.other_subscriber = first(self.loops(OtherSubscriber, anX12Message))
        self.other_payer = first(self.loops(OtherPayer, anX12Message))
        self.other_payer_referring_provider = self.loops(OtherPayerReferringProvider, anX12Message)
        self.other_payer_rendering_provider = first(self.loops(OtherPayerRenderingProvider, anX12Message))
        self.other_payer_supervising_provider = first(self.loops(OtherPayerSupervisingProvider, anX12Message))
        self.other_payer_billing_provider = first(self.loops(OtherPayerBillingProvider, anX12Message))
        self.other_payer_service_facility_location = first(self.loops(OtherPayerServiceFacilityLocation, anX12Message))
        self.other_payer_assistant_surgeon = first(self.loops(OtherPayerAssistantSurgeon, anX12Message))


class OtherSubscriber(X12LoopBridge):
    loopName = "2330A"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    address = SegmentAccess("N3", x12type=SegmentConversion(Address))
    location = SegmentAccess("N4", x12type=SegmentConversion(Location))
    social_security_number = SegmentSequenceAccess("REF", qualifier=(1, "SY"), x12type=SegmentConversion(ReferenceID))


class OtherPayer(X12LoopBridge):
    loopName = "2330B"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    address = SegmentAccess("N3", x12type=SegmentConversion(Address))
    location = SegmentAccess("N4", x12type=SegmentConversion(Location))
    remittance_date = SegmentAccess("DTP", (1, "573"), x12type=SegmentConversion(DateOrTimePeriod))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherPayerReferringProvider(X12LoopBridge):
    loopName = "2330C"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherPayerRenderingProvider(X12LoopBridge):
    loopName = "2330D"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherPayerSupervisingProvider(X12LoopBridge):
    loopName = "2330E"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherPayerBillingProvider(X12LoopBridge):
    loopName = "2330F"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherPayerServiceFacilityLocation(X12LoopBridge):
    loopName = "2330G"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class OtherPayerAssistantSurgeon(X12LoopBridge):
    loopName = "2330H"
    name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
    secondary_identifiers = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))


class _PricingInformation(X12SegmentBridge):
    repricing_methodology = ElementAccess(
        "HCP",
        1,
        x12type=enum(
            {
                "00": "Zero Pricing (Not Covered Under Contract)",
                "01": "Priced as Billed at 100%",
                "02": "Priced at the Standard Fee Schedule",
                "03": "Priced at a Contractual Percentage",
                "04": "Bundled Pricing",
                "05": "Peer Review Pricing",
                "07": "Flat Rate Pricing",
                "08": "Combination Pricing",
                "09": "Maternity Pricing",
                "10": "Other Pricing",
                "11": "Lower of Cost",
                "12": "Ratio of Cost",
                "13": "Cost Reimbursed",
                "14": "Adjustment Pricing",
            }
        ),
    )
    repriced_allowed_amount = ElementAccess("HCP", 2)
    repriced_saving_amount = ElementAccess("HCP", 3)
    repricing_organization_identifier = ElementAccess("HCP", 4)
    rate = ElementAccess("HCP", 5)
    repricing_patient_group_code = ElementAccess("HCP", 6)
    reject_reason = ElementAccess(
        "HCP",
        13,
        x12type=enum(
            {
                "T1": "Cannot Identify Provider as TPO (Third Party Organization) Participant",
                "T2": "Cannot Identify Payer as TPO (Third Party",
                "T3": "Cannot Identify Insured as TPO (Third Party",
                "T4": "Payer Name or Identifier Missing",
                "T5": "Certification Information Missing",
                "T6": "Claim does not contain enough information for repricing",
            }
        ),
    )
    policy_compliance_code = ElementAccess(
        "HCP",
        14,
        x12type=enum(
            {
                "1": "Procedure Followed (Compliance)",
                "2": "Not Followed - Call Not Made (Non-Compliance Call Not Made)",
                "3": "Not Medically Necessary (Non-Compliance NonMedically Necessary)",
                "4": "Not Followed Other (Non-Compliance Other)",
                "5": "Emergency Admit to Non-Network Hospital",
            }
        ),
    )
    exception_code = ElementAccess(
        "HCP",
        15,
        x12type=enum(
            {
                "1": "Non-Network Professional Provider in Network Hospital",
                "2": "Emergency Care",
                "3": "Services or Specialist not in Network",
                "4": "Out-of-Service Area",
                "5": "State Mandates",
                "6": "Other",
            }
        ),
    )


class LineAdjudicationInformation(X12LoopBridge):
    loopName = "2430"

    class _LineAdjudicationInformation(X12SegmentBridge):
        id_code = ElementAccess("SVD", 1)
        paid_amount = ElementAccess("SVD", 2, x12type=Money)
        # TODO: compistiie key
        procedure_identifier = ElementAccess("SVD", 3)
        quantity = ElementAccess("SVD", 5)
        bundled_or_unbundled_line_number = ElementAccess("SVD", 6)

    adjudication_information = SegmentAccess("SVD", x12type=SegmentConversion(_LineAdjudicationInformation))
    dates = SegmentSequenceAccess("DTP", x12type=SegmentConversion(DateOrTimePeriod))
    remaining_patient_iability_amount = ElementAccess("AMT", 2, (1, "EAF"), x12type=Money)

    def __init__(self, anX12Message, *args, **kwargs):
        super(LineAdjudicationInformation, self).__init__(anX12Message, *args, **kwargs)
        self.claim_adjustments = OtherSubscriberInformation._ClaimAdjustments(anX12Message)


class _ContractInformation(X12SegmentBridge):
    type = ElementAccess(
        "CN1",
        1,
        x12type=enum(
            {
                "02": "Per Diem",
                "03": "Variable Per Diem",
                "04": "Flat",
                "05": "Capitated",
                "06": "Percent",
                "09": "Other",
            }
        ),
    )
    amount = ElementAccess("CN1", 2, x12type=Money)
    percentage = ElementAccess("CN1", 3)
    code = ElementAccess("CN1", 4)
    discount_percentage = ElementAccess("CN1", 5)
    version_id = ElementAccess("CN1", 6)


class ServiceLine(Facade, X12LoopBridge):
    loopName = "2400"
    number = SegmentSequenceAccess("LX")

    class _DentalService(X12SegmentBridge):
        # TODO: fix composite key 1 for procedure
        procedure = ElementAccess("SV3", 1)
        charge_amount = ElementAccess("SV3", 2)
        place_of_service_code = ElementAccess("SV3", 3)
        # TODO: another composite key for oral cavity designation
        oral_cavity_designation_code = ElementAccess("SV3", 4)
        inlay_code = ElementAccess("SV3", 5, x12type=enum({"I": "Initial Placement", "R": "Replacement"}))
        quantity = ElementAccess("SV3", 6)
        # TODO: another composite key for diagnosis code pointer
        diagnosis_code_pointer = ElementAccess("SV3", 11)

    class _ToothInformation(X12SegmentBridge):
        id_code_qualifier = ElementAccess("TOO", 1)
        code = ElementAccess("TOO", 2)
        # # TODO: also a composite key
        surface = ElementAccess("TOO", 3)

    dental_service = SegmentAccess("SV3", x12type=SegmentConversion(_DentalService))
    teeth_information = SegmentSequenceAccess("TOO", (1, "JP"), x12type=SegmentConversion(_ToothInformation))
    dates = SegmentSequenceAccess("DTP", x12type=SegmentConversion(DateOrTimePeriod))
    contract_information = SegmentAccess("CN1", x12type=SegmentConversion(_ContractInformation))
    reference_identifications = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))
    sales_tax_amount = ElementAccess("AMT", 2, (1, "T"), x12type=Money)
    fixed_format_file_information = ElementSequenceAccess("K3", 1)
    service_pricing_Information = SegmentAccess("HCP", x12type=SegmentConversion(_PricingInformation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(ServiceLine, self).__init__(anX12Message, *args, **kwargs)
        self.rendering_provider = first(self.loops(RenderingProvider, anX12Message, loppName="2420A"))
        self.assistant_surgeon = first(self.loops(AssistantSurgeon, anX12Message, loppName="2420B"))
        self.supervising_provider = first(self.loops(SupervisingProvider, anX12Message, loppName="2420C"))
        self.service_facility_location = first(self.loops(ServiceFacilityLocation, anX12Message, loppName="2420D"))
        self.line_adjudication_information = self.loops(LineAdjudicationInformation, anX12Message)


class BillingProvider(Facade, X12LoopBridge):
    loopName = "2000A"

    class _CurrencyInformation(X12SegmentBridge):
        id_code = ElementAccess("CUR", 2, x12type=enum({"85": "Billing Provider"}))
        currency_code = ElementAccess("CUR", 2)

    class _BillingProviderName(X12LoopBridge):
        loopName = "2010AA"
        name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
        address = SegmentAccess("N3", x12type=SegmentConversion(Address))
        location = SegmentAccess("N4", x12type=SegmentConversion(Location))
        tax_identification = SegmentAccess("REF", qualifier=(1, ["EI", "SY"]), x12type=SegmentConversion(ReferenceID))
        upin_and_license_information = SegmentSequenceAccess(
            "REF", qualifier=(1, ["0B", "1G"]), x12type=SegmentConversion(ReferenceID)
        )
        contact_information = SegmentSequenceAccess("PER", x12type=SegmentConversion(ContactInformation))

    class _PayToAddressName(X12LoopBridge):
        loopName = "2010AB"
        name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
        address = SegmentAccess("N3", x12type=SegmentConversion(Address))
        location = SegmentAccess("N4", x12type=SegmentConversion(Location))

    class _PayToPlanName(X12LoopBridge):
        loopName = "2010AC"
        name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
        address = SegmentAccess("N3", x12type=SegmentConversion(Address))
        location = SegmentAccess("N4", x12type=SegmentConversion(Location))
        tax_identification = SegmentAccess("REF", qualifier=(1, ["EI"]), x12type=SegmentConversion(ReferenceID))
        secondary_identification = SegmentSequenceAccess(
            "PER", qualifier=(1, ["2U", "FY", "NF"]), x12type=SegmentConversion(ReferenceID)
        )

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))
    currency_information = SegmentAccess("CUR", x12type=SegmentConversion(_CurrencyInformation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(BillingProvider, self).__init__(anX12Message, *args, **kwargs)
        self.billing_proivder_name = first(self.loops(BillingProvider._BillingProviderName, anX12Message))
        self.pay_to_provider = first(self.loops(BillingProvider._PayToAddressName, anX12Message))
        self.payee = first(self.loops(BillingProvider._PayToPlanName, anX12Message))


class Subscriber(Facade, X12LoopBridge):
    loopName = "2000B"

    class _SubscriberInformation(X12SegmentBridge):
        payer_responsibility_sequence_number_code = ElementAccess(
            "SBR",
            1,
            x12type=enum(
                {
                    "A": "Payer Responsibility Four",
                    "B": "Payer Responsibility Five",
                    "C": "Payer Responsibility Six",
                    "D": "Payer Responsibility Seven",
                    "E": "Payer Responsibility Eight",
                    "F": "Payer Responsibility Nine",
                    "G": "Payer Responsibility Ten",
                    "H": "Payer Responsibility Eleven",
                    "P": "Primary",
                    "S": "Secondary",
                    "T": "Tertiary",
                    "U": "Unknown",
                }
            ),
        )
        rel_code = ElementAccess("SBR", 2, x12type=enum({"18": "Self"}))
        reference = ElementAccess("SBR", 3)
        name = ElementAccess("SBR", 4)
        insurance_type = ElementAccess(
            "SBR",
            5,
            x12type=enum(
                {
                    "12": "Medicare Secondary Working Aged Beneficiary or Spouse with Employer Group Health Plan",
                    "13": "Medicare Secondary End-Stage Renal Disease Beneficiary in the Mandated Coordination Period with an Employer’s Group Health Plan",
                    "14": "Medicare Secondary, No-fault Insurance including Auto is Primary",
                    "15": "Medicare Secondary Worker’s Compensation",
                    "16": "Medicare Secondary Public Health Service (PHS) or Other Federal Agency",
                    "41": "Medicare Secondary Black Lung",
                    "42": "Medicare Secondary Veteran’s Administration",
                    "43": "Medicare Secondary Disabled Beneficiary Under Age 65 with Large Group Health Plan (LGHP)",
                    "47": "Medicare Secondary, Other Liability Insurance is Primary",
                }
            ),
        )
        claim_code = ElementAccess(
            "SBR",
            9,
            x12type=enum(
                {
                    "11": "Other Non-Federal Programs",
                    "12": "Preferred Provider Organization (PPO)",
                    "13": "Point of Service (POS)",
                    "14": "Exclusive Provider Organization (EPO)",
                    "15": "Indemnity Insurance",
                    "16": "Health Maintenance Organization (HMO) Medicare Risk",
                    "17": "Dental Maintenance Organization",
                    "AM": "Automobile Medical",
                    "BL": "Blue Cross/Blue Shield",
                    "CH": "Champus",
                    "CI": "Commercial Insurance Co.",
                    "DS": "Disability",
                    "FI": "Federal Employees Program",
                    "HM": "Health Maintenance Organization",
                    "LM": "Liability Medical",
                    "MA": "Medicare Part A",
                    "MB": "Medicare Part B",
                    "MC": "Medicaid",
                    "OF": "Other Federal Program 1484",
                    "TV": "Title V",
                    "VA": "Veterans Affairs Plan",
                    "WC": "Workers’ Compensation Health Claim",
                    "ZZ": "Mutually Defined",
                }
            ),
        )

    class _SubscriberName(X12LoopBridge):
        loopName = "2010BA"
        name = SegmentAccess("NM1", qualifier=(1, ["IL"]), x12type=SegmentConversion(NamedEntity))
        address = SegmentAccess("N3", x12type=SegmentConversion(Address))
        location = SegmentAccess("N4", x12type=SegmentConversion(Location))
        secondary_identification = SegmentSequenceAccess(
            "PER", qualifier=(1, ["SY"]), x12type=SegmentConversion(ReferenceID)
        )
        property_and_casualty_claim_number = SegmentAccess(
            "REF", qualifier=(1, ["Y4"]), x12type=SegmentConversion(ReferenceID)
        )

    class _Payer(X12LoopBridge):
        loopName = "2010BB"
        name = SegmentAccess("NM1", x12type=SegmentConversion(NamedEntity))
        address = SegmentAccess("N3", x12type=SegmentConversion(Address))
        location = SegmentAccess("N4", x12type=SegmentConversion(Location))
        secondary_identification = SegmentSequenceAccess(
            "PER", qualifier=(1, ["2U", "FY", "NF", "EI"]), x12type=SegmentConversion(ReferenceID)
        )
        billing_provider_secondary_identification = SegmentAccess(
            "REF", qualifier=(1, ["G2", "LU"]), x12type=SegmentConversion(ReferenceID)
        )

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))
    subscriber_information = SegmentAccess("SBR", x12type=SegmentConversion(_SubscriberInformation))
    demographic_information = SegmentAccess("DMG", x12type=SegmentConversion(DemographicInformation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Subscriber, self).__init__(anX12Message, *args, **kwargs)
        self._SubscriberInformation = first(self.loops(Subscriber._SubscriberName, anX12Message))
        self.payee = first(self.loops(Subscriber._Payer, anX12Message))


# Patient DATA
class Patient(Facade, X12LoopBridge):
    loopName = "2000C"

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))
    rel = ElementAccess(
        "PAT",
        1,
        x12type=enum(
            {
                "01": "Spouse",
                "19": "Child",
                "20": "Employee",
                "21": "Unknown",
                "39": "Organ Donor",
                "40": "Cadaver Donor",
                "53": "Life Partner",
                "G8": "Other Relationship",
            }
        ),
    )

    class _PatientName(X12LoopBridge):
        loopName = "2010CA"
        name = SegmentAccess("NM1", qualifier=(1, ["QC"]), x12type=SegmentConversion(NamedEntity))
        address = SegmentAccess("N3", x12type=SegmentConversion(Address))
        location = SegmentAccess("N4", x12type=SegmentConversion(Location))
        demographic_information = SegmentAccess("DMG", x12type=SegmentConversion(DemographicInformation))
        property_and_casualty_claim_number = SegmentAccess(
            "REF", qualifier=(1, ["Y4"]), x12type=SegmentConversion(ReferenceID)
        )

    def __init__(self, anX12Message, *args, **kwargs):
        super(Patient, self).__init__(anX12Message, *args, **kwargs)
        self.patient_name = first(self.loops(Patient._PatientName, anX12Message))
        self.claims = self.loops(ClaimInformation, anX12Message)


# Patient DATA
class ClaimInformation(Facade, X12LoopBridge):
    loopName = "2300"

    class _ClaimInformation(X12SegmentBridge):
        patient_control_number = ElementAccess(
            "CLM",
            1,
        )
        total_charge_amount = ElementAccess("CLM", 2, x12type=Money)
        # TODO: compositeAccess is not working, infact it is not working for other types as well, we need to fix
        # one idea is simply to get the element -> it will be something like this B:A:C, and then split and get by
        # position
        # 3, 4 5 elemnets are not used in dental claim
        composite_element_5 = ElementAccess("CLM", 5)
        provider_or_supplier_signature_indicator = ElementAccess("CLM", 6, x12type=enum({"N": "No", "Y": "Yes"}))
        provider_accept_assignment_code = ElementAccess("CLM", 7, x12type=enum({"A": "Assigned", "C": "Not Assigned"}))
        benefit_assignment_certififcation_indicator = ElementAccess(
            "CLM", 8, x12type=enum({"N": "No", "Y": "Yes", "W": "Not Applicable"})
        )
        release_of_information_code = ElementAccess(
            "CLM",
            9,
            x12type=enum(
                {
                    "I": "Informed Consent to Release Medical Information for Conditions or Diagnoses Regulated by Federal Statutes",
                    "Y": "Yes, Provider has a Signed Statement Permitting Release of Medical Billing Data Related to a Claim",
                }
            ),
        )
        releated_causes_information = ElementAccess("CLM", 10)
        composite_element_11 = ElementAccess("CLM", 11)
        special_program_indicator = ElementAccess(
            "CLM",
            12,
            x12type=enum(
                {
                    "01": "Early & Periodic Screening, Diagnosis, and Treatment (EPSDT)",
                    "02": "Physically Handicapped Children’s Program",
                    "03": "Special Federal Funding",
                    "04": "Disability",
                }
            ),
        )
        predetermination_of_Benefits_code = ElementAccess(
            "CLM",
            19,
            x12type=enum(
                {
                    "PB": "Predetermination of Dental Benefits",
                }
            ),
        )
        delay_reason_code = ElementAccess(
            "CLM",
            11,
            x12type=enum(
                {
                    "1": "Proof of Eligibility Unknown or Unavailable",
                    "2": "Litigation",
                    "3": "Authorization Delays",
                    "4": "Delay in Certifying Provider",
                    "5": "Delay in Supplying Billing Forms",
                    "6": "Delay in Delivery of Custom-made Appliances",
                    "7": "Third Party Processing Delay",
                    "8": "Delay in Eligibility Determination",
                    "9": "Original Claim Rejected or Denied Due to a Reason",
                    "Unrelated": "to the Billing Limitation Rules",
                    "10": "Administration Delay in the Prior Approval Process",
                    "11": "Other",
                    "15": "Natural Disaster",
                }
            ),
        )

    class _OrthodonticTotalMonthsOfTreatment(X12SegmentBridge):
        estimated_treatment_months_count = ElementAccess("DN1", 1)
        remaining_treatment_months_count = ElementAccess("DN1", 2)
        treatment_indicator = ElementAccess("DN1", 3)

    class _ToothStatus(X12SegmentBridge):
        tooth_number = ElementAccess("DN2", 1)
        tooth_status = ElementAccess("DN2", 2, x12type=enum({"E": "To Be Extracted", "M": "Missing"}))

    class _ClaimSupplementalInformation(X12SegmentBridge):
        attatchment_report_type = ElementAccess(
            "PWK",
            1,
            x12type=enum(
                {
                    "B4": "Referral Form",
                    "DA": "Dental Models",
                    "DG": "Diagnostic Report",
                    "EB": "Explanation of Benefits (Coordination of Benefits or Medicare Secondary Payor)",
                    "OZ": "Support Data for Claim",
                    "P6": "Periodontal Charts",
                    "RB": "Radiology Films",
                    "RR": "Radiology Reports",
                }
            ),
        )
        attatchment_transmission = ElementAccess(
            "PWK",
            2,
            x12type=enum(
                {
                    "B4": "Referral Form",
                    "AA": "Available on Request at Provider Site",
                    "BM": "By Mail",
                    "EB": "Electronically Only",
                    "EM": "E-Mail",
                    "FT": "File Transfer",
                    "FX": "By Fax",
                }
            ),
        )
        attachment_control_number = ElementAccess("PWK", 6, (5, "AC"))

    class _ClaimNotes(X12SegmentBridge):
        code = ElementAccess("NTE", 1, x12type=enum({"ADD": "Additional Information"}, raw_unknowns=True))
        note = ElementAccess("NTE", 2)

    class _HealthcareInformation(X12SegmentBridge):
        code1 = ElementAccess("HI", 1)
        code2 = ElementAccess("HI", 2)
        code3 = ElementAccess("HI", 3)
        code4 = ElementAccess("HI", 4)

    claim_information = SegmentAccess("CLM", x12type=SegmentConversion(_ClaimInformation))
    dates = SegmentSequenceAccess("DTP", x12type=SegmentConversion(DateOrTimePeriod))
    orthodontic_total_months_of_treatment = SegmentAccess(
        "DN1", x12type=SegmentConversion(_OrthodonticTotalMonthsOfTreatment)
    )
    teeth_statuses = SegmentSequenceAccess("DN2", x12type=SegmentConversion(_ToothStatus))
    supplemental_information = SegmentSequenceAccess("PWK", x12type=SegmentConversion(_ClaimSupplementalInformation))
    contract_information = SegmentAccess("CN1", x12type=SegmentConversion(_ContractInformation))
    patient_amount_paid = ElementAccess("AMT", 2, (1, "F5"), x12type=Money)
    references_identification = SegmentSequenceAccess("REF", x12type=SegmentConversion(ReferenceID))
    fixed_format_file_information = ElementAccess("K3", 1)
    notes = SegmentSequenceAccess("NTE", x12type=SegmentConversion(_ClaimNotes))
    healthcare_information = SegmentAccess("HI", x12type=SegmentConversion(_HealthcareInformation))
    claim_pricing_Information = SegmentAccess("HCP", x12type=SegmentConversion(_PricingInformation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(ClaimInformation, self).__init__(anX12Message, *args, **kwargs)
        self.referring_provider = self.loops(ReferringProvider, anX12Message)
        self.rendering_provider = first(self.loops(RenderingProvider, anX12Message))
        self.service_facility_location = first(self.loops(ServiceFacilityLocation, anX12Message))
        self.assistant_surgeon = first(self.loops(AssistantSurgeon, anX12Message))
        self.supervising_provider = first(self.loops(SupervisingProvider, anX12Message))
        self.other_subscriber_information = self.loops(OtherSubscriberInformation, anX12Message)
        self.service_lines = self.loops(ServiceLine, anX12Message)
