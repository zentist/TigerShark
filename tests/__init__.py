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

# Map (version tuple, transaction set identifier) to test file names.
TEST_FILES = {
    ((4,), '271'): '271-dependent-benefits.txt',
    ((4,), '271'): '271-example-2.txt',
    ((4,), '271'): '271-example-dependent-rejection.txt',
    ((4,), '271'): '271-example.txt',
    ((4,), '271'): '271-related-entity.txt',
    ((4,), '276'): 'TEST 276 TXNs.txt',
    ((4,), '278'): 'TEST 278_13 TXNS.txt',
    ((4,), '278'): 'TEST 278_28 TXNS_SOA.txt',
    ((4,), '835'): '835-example-2.txt',
    ((4,), '835'): '835-example.txt',
    ((4,), '837'): '837-example.txt',
    ((4,), '837'): '837I-Examples.txt',
    ((4,), '837'): '837I-Patient-NotSubscriber.txt',
    ((4,), '837'): '837I-Patient-NotSubscriber2.txt',
    ((4,), '837'): '837I-Patient-Subscriber.txt',
    ((5,), '835'): '5010-835-example-1.txt',
    ((5,), '835'): '5010-835-example-2.txt',
    ((5,), '835'): '5010-835-example-3.txt',
}
