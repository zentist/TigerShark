"""
TigerShark - An X12 EDI message parser.
"""
__all__ = ['X12VersionTuple', 'X12_VERSION_4010', 'X12_VERSION_5010']
__version__ = "0.2.7"
__authors__ = [
    "Steven Buss <steven.buss@gmail.com>",
    "Steven Lott <slott56@gmail.com>",
    "Dave Peticolas <dave.peticolas@gmail.com>",
]

from collections import namedtuple

X12VersionTuple = namedtuple('X12VersionTuple',
                             ('version', 'release', 'subrelease'))

X12_VERSION_4010 = X12VersionTuple(4, 1, 0)
X12_VERSION_5010 = X12VersionTuple(5, 1, 0)
