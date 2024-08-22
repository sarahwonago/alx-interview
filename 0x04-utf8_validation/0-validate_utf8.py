#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False.
    """
    n_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not n_bytes:
            while byte & mask:
                n_bytes += 1
                mask >>= 1
            if not n_bytes:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        n_bytes -= 1
    return n_bytes == 0
