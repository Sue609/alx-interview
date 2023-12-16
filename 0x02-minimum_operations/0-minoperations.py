#!/usr/bin/python3
'''
This module introduces a function
'''


def minOperations(n):
    '''
    Method that calculates the fewest number of operations
    needed to result in exactly n H characters in the fule.
    '''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
