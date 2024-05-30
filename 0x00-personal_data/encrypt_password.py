#!/usr/bin/env python3
'''
hashing password.
'''


import bcrypt


def hash_password(password):
    '''
    function that returns hashed password.
    '''
    return bcrypt.hashpw(b'{password}', bcrypt.gensalt())
