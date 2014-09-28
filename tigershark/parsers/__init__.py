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

IdentifyingParser = Message(
    u'835W1',
    Properties(
        desc=u'HIPAA Health Care Claim Payment/Advice 005010X221A1 835W1',
    ),
    ISALoop,
)
