#!/usr/bin/env python3
'''
hashing password.
'''


import bcrypt


def hash_password(password: str) -> bytes:
    '''
    function that returns hashed password.
    '''
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed
