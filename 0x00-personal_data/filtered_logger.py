#!/usr/bin/env python3
'''
filter_datum function.
'''


import re


def filter_datum(fields, redaction, message, separator):
    '''
    function that will return regular expression.
    '''
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
        return message
