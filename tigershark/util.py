from tigershark.facade import get_facade
from tigershark.facade.control import ControlHeaders
from tigershark.parsers import SimpleParser
from tigershark.parsers import parse_control_headers


def identify_simple_x12(x12_contents):
    """
    Return (transaction set id, version tuple) for simple X12.

    Simple X12 has only one kind of transaction set and one version.

    :param x12_contents: A string with X12 content.
    :returns: (transaction set id, version_tuple)
    :raises ValueError: If we cannot find any transaction set.
    :raises ValueError: If we find more than one kind of transaction set
        or version.
    :raises ParseError: If the X12 cannot be parsed.
    """
    identifers = set()  # (transaction set id, version tuple)

    headers = ControlHeaders(parse_control_headers(x12_contents))

    for control in headers.interchange_controls:
        for group in control.functional_groups:
            for transaction_set in group.transaction_sets:
                identifers.add((
                    transaction_set.transaction_set_identifier_code,
                    group.version_tuple))

    if not identifers:
        raise ValueError('No transaction sets')
    elif len(identifers) > 1:
        raise ValueError('Multiple kinds of transaction sets.', identifers)
    else:
        return identifers.pop()


def apply_facade_to_simple_x12(x12_contents):
    """
    Identify, parse, and apply a facade to simple X12.

    If the X12 can be identified and parsed, the appropriate
    Facade is applied and returned.

    :param x12_contents: A string with X12 content.
    :returns: A Facade instance.
    :raises ValueError: If we cannot find any transaction set.
    :raises ValueError: If we find more than one kind of transaction set
        or version.
    :raises ValueError: If we cannot find an appropriate Facade.
    :raises ParseError: If the X12 cannot be parsed.
    """
    transaction_set_id, version_tuple = identify_simple_x12(x12_contents)
    parser = SimpleParser(transaction_set_id, version_tuple)
    x12 = parser.unmarshall(x12_contents)
    return get_facade(transaction_set_id, version_tuple)(x12)
