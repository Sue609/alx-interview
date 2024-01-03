#!/usr/bin/python3
'''
This module introduces a function
'''


def validUTF8(data):
    '''
    Function that determines if a given data set represents a
    valid utf-8 encoding.
    Returns: True if the data is a valid utf-8 encoding else False
    '''
    num_bytes = 0

    for byte in data:
        mask = 1 << 7

        if num_bytes == 0:
            # Determine the number of bytes needed for this UTF-8
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # Validate the number of bytes in the character
            if num_bytes == 0:
                continue  # Single byte character

            elif num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # check if the byte is a valid continuation byte
            if not (byte >> 6 == 0b10):
                return False

        num_bytes -= 1

    return num_bytes == 0
