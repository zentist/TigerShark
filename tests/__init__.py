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
from tigershark import X12_4010_X059
from tigershark import X12_4010_X091A1
from tigershark import X12_4010_X092A1
from tigershark import X12_4010_X093A1
from tigershark import X12_4010_X096A1
from tigershark import X12_4010_X098A1
from tigershark import X12_5010_X221A1

# Map (X12VersionTuple, Transaction Set Identifier) to test file names.
TEST_FILE_MAP = {
    (X12_4010_X092A1, '271'): '271-dependent-benefits.txt',
    (X12_4010_X092A1, '271'): '271-example-2.txt',
    (X12_4010_X092A1, '271'): '271-example-dependent-rejection.txt',
    (X12_4010_X092A1, '271'): '271-example.txt',
    (X12_4010_X092A1, '271'): '271-related-entity.txt',
    (X12_4010_X093A1, '276'): 'TEST 276 TXNs.txt',
    (X12_4010_X059, '278'): 'TEST 278_13 TXNS.txt',
    (X12_4010_X059, '278'): 'TEST 278_28 TXNS_SOA.txt',
    (X12_4010_X091A1, '835'): '835-example-2.txt',
    (X12_4010_X091A1, '835'): '835-example.txt',
    (X12_4010_X098A1, '837'): '837-example.txt',
    (X12_4010_X096A1, '837'): '837I-Examples.txt',
    (X12_4010_X096A1, '837'): '837I-Patient-NotSubscriber.txt',
    (X12_4010_X096A1, '837'): '837I-Patient-NotSubscriber2.txt',
    (X12_4010_X096A1, '837'): '837I-Patient-Subscriber.txt',
    (X12_5010_X221A1, '835'): '5010-835-example-1.txt',
    (X12_5010_X221A1, '835'): '5010-835-example-2.txt',
    (X12_5010_X221A1, '835'): '5010-835-example-3.txt',
}
