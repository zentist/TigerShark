#!/usr/bin/env python
"""The test package contains test data files as well as unit tests.

run_tests
===========

..  automodule:: test.run_tests
    :members:

test_navigation
===============

..  automodule:: test.test_navigation
    :members:

test_parse
===========

..  automodule:: test.test_parse
    :members:

test_wsClaims
==============

..  automodule:: test.test_wsClaims
    :members:

test_convert
=============

..  automodule:: test.test_convert
    :members:

"""
from tigershark import X12_4010_X091A1
from tigershark import X12_4010_X092A1
from tigershark import X12_4010_X093A1
from tigershark import X12_4010_X094A1
from tigershark import X12_4010_X096A1
from tigershark import X12_4010_X098A1
from tigershark import X12_5010_X221A1

# (Transaction Set, X12VersionTuple) -> test file name
TEST_FILE_MAP = {
    ('271', X12_4010_X092A1): '271-dependent-benefits.txt',
    ('271', X12_4010_X092A1): '271-example-2.txt',
    ('271', X12_4010_X092A1): '271-example-dependent-rejection.txt',
    ('271', X12_4010_X092A1): '271-example.txt',
    ('271', X12_4010_X092A1): '271-related-entity.txt',
    ('276', X12_4010_X093A1): 'TEST 276 TXNs.txt',
    ('278', X12_4010_X094A1): 'TEST 278_13 TXNS.txt',
    ('835', X12_4010_X091A1): '835-example-2.txt',
    ('835', X12_4010_X091A1): '835-example.txt',
    ('835', X12_5010_X221A1): '5010-835-example-1.txt',
    ('835', X12_5010_X221A1): '5010-835-example-2.txt',
    ('835', X12_5010_X221A1): '5010-835-example-3.txt',
    ('837', X12_4010_X096A1): '837I-Examples.txt',
    ('837', X12_4010_X096A1): '837I-Patient-NotSubscriber.txt',
    ('837', X12_4010_X096A1): '837I-Patient-NotSubscriber2.txt',
    ('837', X12_4010_X096A1): '837I-Patient-Subscriber.txt',
    ('837', X12_4010_X098A1): '837-example.txt',
}
