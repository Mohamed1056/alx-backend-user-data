#!/usr/bin/env python3
'''
hashing password.
'''


import bcrypt


def hash_password(password):
    '''
    function that returns hashed password.
    '''
    encoded = password.encode()
    return bcrypt.hashpw(encoded, bcrypt.gensalt())
