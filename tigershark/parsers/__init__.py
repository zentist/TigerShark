from tigershark.extras import standardSegment
from tigershark.X12.parse import Loop
from tigershark.X12.parse import Message
from tigershark.X12.parse import Properties


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
