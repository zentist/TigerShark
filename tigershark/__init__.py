"""
TigerShark - An X12 EDI message parser.
"""
__all__ = ['X12VersionTuple']
__version__ = "0.2.7"
__authors__ = [
    "Steven Buss <steven.buss@gmail.com>",
    "Steven Lott <slott56@gmail.com>",
    "Dave Peticolas <dave.peticolas@gmail.com>",
]

from collections import namedtuple

_X12VersionTuple = namedtuple('X12VersionTuple', (
    'version',
    'release',
    'subrelease',
    'industry_identifier_code',
))


class X12VersionTuple(_X12VersionTuple):

    @classmethod
    def for_4010(cls, industry_identifier_code):
        return cls(version=4, release=1, subrelease=0,
                   industry_identifier_code=industry_identifier_code)

    @classmethod
    def for_5010(cls, industry_identifier_code):
        return cls(version=5, release=1, subrelease=0,
                   industry_identifier_code=industry_identifier_code)

    @property
    def is_4010(self):
        return (
            self.version == 4
            and self.release == 1
            and self.subrelease == 0
        )

    @property
    def is_5010(self):
        return (
            self.version == 5
            and self.release == 1
            and self.subrelease == 0
        )

X12_4010_X059 = X12VersionTuple.for_4010('X059')
X12_4010_X091A1 = X12VersionTuple.for_4010('X091A1')
X12_4010_X092A1 = X12VersionTuple.for_4010('X092A1')
X12_4010_X093A1 = X12VersionTuple.for_4010('X093A1')
X12_4010_X096A1 = X12VersionTuple.for_4010('X096A1')
X12_5010_X221A1 = X12VersionTuple.for_5010('X221A1')
