"""
TigerShark - An X12 EDI message parser.
"""
__all__ = ['X12VersionTuple']
__version__ = "0.3.4"
__authors__ = [
    "Steven Buss <steven.buss@gmail.com>",
    "Steven Lott <slott56@gmail.com>",
    "Dave Peticolas <dave.peticolas@gmail.com>",
    "Cloud Cray <cloudcray@gmail.com>",
]

from collections import namedtuple

_X12VersionTuple = namedtuple('X12VersionTuple', (
    'version',
    'release',
    'subrelease',
    'industry_identifier_code',
))


class X12VersionTuple(_X12VersionTuple):
    """
    A structured representation of an X12 version / release / industry id code.

    Attributes:
      * version: The integer version number.
      * release: The integer release number.
      * subrelease: The integer subrelease number.
      * industry_identifier_code: The string industry identifer code.

    For example, the representation of 004010X091 is:

        X12VersionTuple(
            version=4,
            release=1,
            subrelease=0,
            industry_identifier_code='X091')
    """

    @classmethod
    def for_4010(cls, industry_identifier_code):
        """
        Construct an X12VersionTuple for 4010 with the given industry id code.
        """
        return cls(version=4, release=1, subrelease=0,
                   industry_identifier_code=industry_identifier_code)

    @classmethod
    def for_5010(cls, industry_identifier_code):
        """
        Construct an X12VersionTuple for 5010 with the given industry id code.
        """
        return cls(version=5, release=1, subrelease=0,
                   industry_identifier_code=industry_identifier_code)

    @property
    def is_4010(self):
        """
        True if this is a 4010 version.
        """
        return (
            self.version == 4
            and self.release == 1
            and self.subrelease == 0
        )

    @property
    def is_5010(self):
        """
        True if this is a 5010 version.
        """
        return (
            self.version == 5
            and self.release == 1
            and self.subrelease == 0
        )

    @property
    def version_string(self):
        """
        The string representation of a version without the industry id code.
        """
        return '{}{:02}{}'.format(self.version, self.release, self.subrelease)


X12_4010_X061A1 = X12VersionTuple.for_4010('X061A1')
X12_4010_X070 = X12VersionTuple.for_4010('X070')
X12_4010_X091A1 = X12VersionTuple.for_4010('X091A1')
X12_4010_X092A1 = X12VersionTuple.for_4010('X092A1')
X12_4010_X093A1 = X12VersionTuple.for_4010('X093A1')
X12_4010_X094A1 = X12VersionTuple.for_4010('X094A1')
X12_4010_X095A1 = X12VersionTuple.for_4010('X095A1')
X12_4010_X096A1 = X12VersionTuple.for_4010('X096A1')
X12_4010_X097A1 = X12VersionTuple.for_4010('X097A1')
X12_4010_X098A1 = X12VersionTuple.for_4010('X098A1')
X12_4010_XXXC = X12VersionTuple.for_4010('XXXC')
X12_5010_X221A1 = X12VersionTuple.for_5010('X221A1')
X12_5010_X279A1 = X12VersionTuple.for_5010('X279A1')
X12_5010_X222A1 = X12VersionTuple.for_5010('X222A1')
X12_5010_X223A1 = X12VersionTuple.for_5010('X223A1')
