from tigershark.facade.control import ControlHeaders
from tigershark.parsers import parse_control_headers


def identify_simple_x12(x12_contents):
    """
    Return (transaction set id, version tuple) for simple X12.

    Simple X12 has only one kind of transaction set and one version.

    :param x12_contents: A string with X12 content.
    :returns: (transaction set id, version_tuple)
    :raises ValueError: if we cannot find any transaction set.
    :raises ValueError: if we find more than one kind of transaction set
        or version.
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
