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


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    function to check if the password
    matches the hased password.
    '''
    my_password = password.encode()
    if bcrypt.checkpw(my_password, hashed_password):
        return True
    else:
        return False
