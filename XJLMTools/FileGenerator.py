""" Sandbox :: FileGenerator

Description:
    Script for generating a random file

Author:
    marcusljx

Created:
    2016-06-06
"""
import argparse
import io
import os

import _common

CHUNKSIZE = 2 ** 16


def chunk_range(total, divisor):
    while total > divisor:
        yield divisor
        total -= divisor
    yield total


class FileGenerator():
    def __init__(self):
        pass

    def generate(self, filename, filesize_bytes):
        with io.open(filename, 'wb', buffering=1024 * 1024) as F:
            for i in chunk_range(filesize_bytes, CHUNKSIZE):
                F.write(_common.get_randbytes(i))


if __name__ == "__main__":
    P = argparse.ArgumentParser(description="Generate a random file of specified bytes size.")
    P.add_argument("-d", "--destination", default=os.path.join(os.getcwd(), "GeneratedFile"),
                   help="Path of file to be created/appended")
    P.add_argument("-s", "--size", type=int, default=CHUNKSIZE, help="Size (in bytes) to create/append (default=65536)")
    options = P.parse_args()

    FG = FileGenerator()
    FG.generate(options.destination, options.size)
