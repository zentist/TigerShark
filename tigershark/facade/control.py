from tigershark import X12VersionTuple
from tigershark.facade import D8
from tigershark.facade import ElementAccess
from tigershark.facade import Facade
from tigershark.facade import TM
from tigershark.facade import X12LoopBridge


class ControlHeaders(Facade):

    def __init__(self, x12_message):
        super(ControlHeaders, self).__init__()
        isa_loops = x12_message.descendant('LOOP', name='ISA_LOOP')
        self.interchange_controls = [InterchangeControlHeader(loop) for loop in isa_loops]


class InterchangeControlHeader(X12LoopBridge):

    authorization_information_qualifier = ElementAccess("ISA", 1)
    authorization_information = ElementAccess("ISA", 2)

    security_information_qualifier = ElementAccess("ISA", 3)
    security_information = ElementAccess("ISA", 4)

    interchange_sender_id_qualifier = ElementAccess("ISA", 5)
    interchange_sender_id = ElementAccess("ISA", 6)

    interchange_receiver_id_qualifier = ElementAccess("ISA", 7)
    interchange_receiver_id = ElementAccess("ISA", 8)

    interchange_date = ElementAccess("ISA", 9, x12type=D8)
    interchange_time = ElementAccess("ISA", 10, x12type=TM)

    interchange_control_standards_id = ElementAccess("ISA", 11)
    interchange_control_version_number = ElementAccess("ISA", 12)
    interchange_control_number = ElementAccess("ISA", 13)

    acknowledgement_requested = ElementAccess("ISA", 14)
    test_indicator = ElementAccess("ISA", 15)
    subelement_separator = ElementAccess("ISA", 16)

    def __init__(self, x12_message):
        super(InterchangeControlHeader, self).__init__(x12_message)
        gs_loops = x12_message.descendant('LOOP', name='GS_LOOP')
        self.functional_groups = [FunctionalGroupHeader(loop) for loop in gs_loops]


class FunctionalGroupHeader(X12LoopBridge):

    functional_id_code = ElementAccess("GS", 1)

    application_sender_code = ElementAccess("GS", 2)
    application_receiver_code = ElementAccess("GS", 3)

    date = ElementAccess("GS", 4, x12type=D8)
    time = ElementAccess("GS", 5, x12type=TM)

    group_control_number = ElementAccess("GS", 6)

    responsible_agency_code = ElementAccess("GS", 7)

    version_indicator_code = ElementAccess("GS", 8)

    def __init__(self, x12_message):
        super(FunctionalGroupHeader, self).__init__(x12_message)
        st_loops = x12_message.descendant('LOOP', name='ST_LOOP')
        self.transaction_sets = [
            TransactionSetHeader(self, st_loop)
            for st_loop in st_loops]

    @property
    def version_tuple(self):
        """
        Return a tuple of (version, release, subrelease) numbers.

        Returns None if no version is given or has a different format.
        """
        if self.responsible_agency_code == 'X':
            return X12VersionTuple(
                version=int(self.version_indicator_code[0:3]),
                release=int(self.version_indicator_code[3:5]),
                subrelease=int(self.version_indicator_code[5:6]),
                industry_identifier_code=self.version_indicator_code[6:],
            )


class TransactionSetHeader(X12LoopBridge):

    transaction_set_identifier_code = ElementAccess("ST", 1)

    transaction_set_control_number = ElementAccess("ST", 2)

    def __init__(self, functional_group, x12_message):
        super(TransactionSetHeader, self).__init__(x12_message)
        self.functional_group = functional_group
