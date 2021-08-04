from tigershark import (
    X12_4010_X061A1,
    X12_4010_X070,
    X12_4010_X091A1,
    X12_4010_X092A1,
    X12_4010_X093A1,
    X12_4010_X094A1,
    X12_4010_X095A1,
    X12_4010_X096A1,
    X12_4010_X097A1,
    X12_4010_X098A1,
    X12_4010_XXXC,
    X12_5010_X221A1,
    X12_5010_X279A1,
    X12_5010_X222A1,
    X12_5010_X223A1,
)
from tigershark.extras import standardSegment
from tigershark.X12.parse import (
    Loop,
    Message,
    ParseError,
    Properties
)

# Transaction Set ID -> X12VersionTuple -> [(parser module, parser name)]
PARSER_MAP = {
    '270': {
        X12_4010_X092A1: [('M270_4010_X092_A1', 'parsed_270')],
        X12_5010_X279A1: [('M270_5010_X279_A1', 'parsed_270')],
    },
    '271': {
        X12_4010_X092A1: [('M271_4010_X092_A1', 'parsed_271')],
        X12_5010_X279A1: [('M271_5010_X279_A1', 'parsed_271')],
    },
    '276': {
        X12_4010_X093A1: [('M276_4010_X093_A1', 'parsed_276')],
    },
    '277U': {
        X12_4010_X070: [('M277U_4010_X070', 'parsed_277U')],
    },
    '277': {
        X12_4010_X093A1: [('M277_4010_X093_A1', 'parsed_277')],
    },
    '278': {
        X12_4010_X094A1: [('M278_4010_X094_27_A1', 'parsed_278'),
                          ('M278_4010_X094_A1', 'parsed_278')],
    },
    '820': {
        X12_4010_X061A1: [('M820_4010_X061_A1', 'parsed_820')],
    },
    '834': {
        X12_4010_X095A1: [('M834_4010_X095_A1', 'parsed_834')],
    },
    '835': {
        X12_4010_X091A1: [('M835_4010_X091_A1', 'parsed_835')],
        X12_5010_X221A1: [('M835_5010_X221_A1', 'parsed_835')],
    },
    '837': {
        X12_4010_X096A1: [('M837_4010_X096_A1', 'parsed_837')],
        X12_4010_X097A1: [('M837_4010_X097_A1', 'parsed_837')],
        X12_4010_X098A1: [('M837_4010_X098_A1', 'parsed_837')],
        X12_5010_X222A1: [('M837_5010_X222_A1', 'parsed_837')],  # Professional Claims
        X12_5010_X223A1: [('M837_5010_X223_A1', 'parsed_837')],  # Institutional Claims
    },
    '841': {
        X12_4010_XXXC: [('M841_4010_XXXC', 'parsed_841')],
    },
}


def get_parsers(transaction_set_id, version_tuple):
    """
    Generate the parsers to try for a given transaction_set and version.

    The parsers should be tried in the given order.
    """
    try:
        parsers = PARSER_MAP[transaction_set_id][version_tuple]
    except KeyError:
        raise ValueError("Unsupported transaction set and version.",
                         transaction_set_id, version_tuple)

    for index, (module_name, parser_name) in enumerate(parsers):
        module = __import__('tigershark.parsers.' + module_name,
                            fromlist=[parser_name])
        yield getattr(module, parser_name)


class SimpleParser(object):
    """
    A parser for a particular transaction set and version.
    """
    def __init__(self, transaction_set_id, version_tuple):
        self.transaction_set_id = transaction_set_id
        self.version_tuple = version_tuple

    def unmarshall(self, x12_contents, **kwargs):
        for parser in get_parsers(self.transaction_set_id, self.version_tuple):
            try:
                return parser.unmarshall(x12_contents, **kwargs)
            except ParseError:
                continue
        else:
            # Let the last parser raise.
            return parser.unmarshall(x12_contents, **kwargs)


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
