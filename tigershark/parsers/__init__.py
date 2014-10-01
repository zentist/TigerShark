from tigershark import X12_4010_X061A1
from tigershark import X12_4010_X070
from tigershark import X12_4010_X091A1
from tigershark import X12_4010_X092A1
from tigershark import X12_4010_X093A1
from tigershark import X12_4010_X094A1
from tigershark import X12_4010_X095A1
from tigershark import X12_4010_X096A1
from tigershark import X12_4010_X097A1
from tigershark import X12_4010_X098A1
from tigershark import X12_4010_XXXC
from tigershark import X12_5010_X221A1
from tigershark import X12_5010_X279A1
from tigershark.extras import standardSegment
from tigershark.X12.parse import Loop
from tigershark.X12.parse import Message
from tigershark.X12.parse import Properties

# (X12VersionTuple, Transaction Set Identifier) -> (parser module, parser name)
PARSER_MAP = {
    (X12_4010_X092A1, '270'): ('M270_4010_X092_A1', 'parsed_270'),
    (X12_5010_X279A1, '270'): ('M270_5010_X279_A1', 'parsed_270'),
    (X12_4010_X092A1, '271'): ('M271_4010_X092_A1', 'parsed_271'),
    (X12_5010_X279A1, '271'): ('M271_5010_X279_A1', 'parsed_271'),
    (X12_4010_X093A1, '276'): ('M276_4010_X093_A1', 'parsed_276'),
    (X12_4010_X070, '277U'): ('M277U_4010_X070', 'parsed_277U'),
    (X12_4010_X093A1, '277'): ('M277_4010_X093_A1', 'parsed_277'),
    (X12_4010_X094A1, '278'): ('M278_4010_X094_27_A1', 'parsed_278'),
    (X12_4010_X061A1, '820'): ('M820_4010_X061_A1', 'parsed_820'),
    (X12_4010_X095A1, '834'): ('M834_4010_X095_A1', 'parsed_834'),
    (X12_4010_X091A1, '835'): ('M835_4010_X091_A1', 'parsed_835'),
    (X12_5010_X221A1, '835'): ('M835_5010_X221_A1', 'parsed_835'),
    (X12_4010_X096A1, '837'): ('M837_4010_X096_A1', 'parsed_837'),
    (X12_4010_X097A1, '837'): ('M837_4010_X097_A1', 'parsed_837'),
    (X12_4010_X098A1, '837'): ('M837_4010_X098_A1', 'parsed_837'),
    (X12_4010_XXXC, '841'): ('M841_4010_XXXC', 'parsed_841'),
}


def load_parser(version_tuple, transaction_set_id):
    """
    Load a parser from the version tuple and transaction set ID.
    """
    module_name, parser_name = PARSER_MAP[version_tuple, transaction_set_id]
    module = __import__('tigershark.parsers.' + module_name,
                        fromlist=[parser_name])
    return getattr(module, parser_name)


STLoop = Loop(
    u'ST_LOOP',
    Properties(
        position=u'0200',
        looptype=u'explicit',
        repeat=u'>1',
        req_sit=u'R',
        desc=u'Transaction Set Header',
    ),
    standardSegment.st,
)

GSLoop = Loop(
    u'GS_LOOP',
    Properties(
        position=u'0200',
        looptype=u'explicit',
        repeat=u'>1',
        req_sit=u'R',
        desc=u'Functional Group Header',
    ),
    standardSegment.gs,
    STLoop,
)

ISALoop = Loop(
    u'ISA_LOOP',
    Properties(
        position=u'0010',
        looptype=u'explicit',
        repeat=u'>1',
        req_sit=u'R',
        desc=u'Interchange Control Header',
    ),
    standardSegment.isa,
    GSLoop,
)

ControlParser = Message(
    u'ASC X12 Interchange Control Structure',
    Properties(
        desc=u'ASC X12 Control Structure',
    ),
    ISALoop,
)


def parse_control_headers(x12_contents):
    """Parse only the control headers of an X12 message.

    This parses the three outer control headers of the given X12 message:

    * Interchange Control (ISA)
    * Functional Group (GS)
    * Transaction Set (ST).

    These can be used to identify the X12 versions and transaction set types
    contained in the message.
    """
    return ControlParser.unmarshall(x12_contents, ignoreExtra=True)
