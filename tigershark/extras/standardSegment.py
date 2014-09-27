"""Define :mod:`X12.parse` structures for some standard X12 Segments.

These are definitions of some standard Segments without a lot
of supporting detail.  This can be used (or extended) to cover
cases where X12 segment metadata is not available.

This module includes a conversion to emit "better-than-nothing"
:class:`X12.parse.Segment` definitions for a few standard
X12 Segments.

:var isa: ISA Segment
:var gs: GS Segment
:var st: ST Segment
:var se: SE Segment
:var ge: GE Segment
:var iea: IEA Segment

..  autofunction:: buildSegment
"""
from __future__ import print_function

from tigershark.X12.parse import Element
from tigershark.X12.parse import Properties
from tigershark.X12.parse import Segment

ISAFields = """\
ISA01 Authorization Information Qualifier
ISA02 Authorization Information
ISA03 Security Information Qualifier
ISA04 Security Information
ISA05 Interchange ID Qualifier
ISA06 Interchange Sender ID
ISA07 Interchange ID Qualifier
ISA08 Interchange Receiver ID
ISA09 Interchange Date
ISA10 Interchange Time
ISA11 Interchange Control Standards ID
ISA12 Interchange Control Version Number
ISA13 Interchange Control Number
ISA14 Acknowledgement Requested
ISA15 Test Indicator
ISA16 Subelement Separator
"""

GSFields = """\
GS01  Functional ID code
GS02  Application Sender's Code
GS03  Application Receiver's Code
GS04  Date
GS05  Time
GS06  Group Control Number
GS07  Responsible Agency Code
GS08  Version/Rel. Ind. ID Code"""

STFields = """\
ST01  Transaction set ID code
ST02  Transaction set control number
"""

# SE02 must match ST02
SEFields = """\
SE01  Number of included segments
SE02  Transaction set control number"""

# GE02 must match GS06
GEFields = """\
GE01  Number of Transaction Sets Included in this Function Group
GE02  Group Control Number"""

# IEA02 must match ISA13
IEAFields = """\
IEA01 Number of Included Functional Groups
IEA02 Interchange Control Number (same as ISA13)
"""


def buildSegment(name, desc, fieldText):
    """Convert a block of text to a Segment definition.
    The block of text has one Element defined on each line.
    The Element definition is an Element name, one or more spaces, and the
    element description.

    :param name: the name of the segment
    :param desc: the description of the segment
    :param fieldText: a block of text, with one Element name
        and description per line.
    :returns: :class:`X12.parse.Segment` definition
    """
    segment = Segment(name, Properties(desc=desc))
    for line in filter(None, fieldText.splitlines()):
        name, description = line.strip().split(None, 1)
        element = Element(name, Properties(desc=description, codes=[]))
        segment.append(element)
    return segment

isa = buildSegment("ISA", "ISA", ISAFields)
gs = buildSegment("GS", "GS", GSFields)
st = buildSegment("ST", "ST", STFields)
se = buildSegment("SE", "SE", SEFields)
ge = buildSegment("GE", "GE", GEFields)
iea = buildSegment("IEA", "IEA", IEAFields)
