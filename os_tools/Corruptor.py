""" Sandbox :: Corruptor

Description:
    Corruptor class/script that modifies a file in chunks based on a corruption ratio

Author:
    marcusljx

Created:
    2016-07-05
"""
from __future__ import print_function

import argparse
import io
import os
import random

random.seed()

class Corruptor():
    def __init__(self, chunksize=4096, ratio=0.2):
        assert 0.0 < ratio < 1.0
        self.ratio = ratio
        self.chunk_size = chunksize
        self.data = bytes()

    def corrupt(self, infile_path, outfile_path):
        with io.open(infile_path, 'rb') as infile, io.open(outfile_path, 'wb') as outfile:
            data = infile.read(self.chunk_size)
            while data:
                if random.random() <= self.ratio:
                    outfile.write(os.urandom(self.chunk_size))
                else:
                    outfile.write(data)
                data = infile.read(self.chunk_size)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_in", help="Path of directory to corrupt.")
    parser.add_argument("--dir_out", help="Path of directory to write corrupt files.")
    parser.add_argument("-c", "--chunksize", default=4096, type=int, help="Path of directory to write corrupt files.")
    parser.add_argument("-r", "--ratio", default=0.2, type=float, help="Path of directory to write corrupt files.")
    options = parser.parse_args()

    C = Corruptor(options.chunksize, options.ratio)

    for root, subdirs, files in os.walk(options.dir_in):
        for file in files:
            infile_path = os.path.join(root, file)
            outfile_path = os.path.join(root, "CORRUPTED_%s" % file)
            C.corrupt(infile_path, outfile_path)


if __name__ == '__main__':
    main()