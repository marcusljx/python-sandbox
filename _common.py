""" Sandbox :: _common

Description:
    Common module containing functions for general usage

Author:
    marcusljx

Created:
    2016-09-05
"""
import datetime
import os
import random

def timestamp():
    return datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H%M%S.%f")


def get_randbytes(N, crypto=False):
    """
    :param N: Number of bytes to generate
    :param crypto: Set to True to generate a random string suitable for cryptographic purposes
    :return: Returns a sequence of N random bytes
    """
    if crypto:
        return os.urandom(N)
    else:
        random.getrandbits(8 * N).to_bytes(N, 'little')
