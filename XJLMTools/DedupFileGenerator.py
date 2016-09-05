""" Sandbox :: DedupFileGenerator

Description:
    Script for generating a random file

Author:
    marcusljx

Created:
    2016-07-07
"""
import argparse
import io
import os
import random
import sys


def size_chunker(total, divisor):
    q, r = divmod(total, divisor)
    for _ in range(q):
        yield divisor
    if r:
        yield r


class DedupFileGenerator():
    def __init__(self, chunk_size=4096):
        self.block_size = chunk_size
        self.blocks = []

    def generate_duplicate_block(self):
        pos = random.randint(0, len(self.blocks) - 1)
        return self.blocks[pos]

    def generate_unique_block(self, size):
        block = os.urandom(size)
        self.blocks.append(block)
        return block

    def write(self, filepath, size, dedup_probability=0.0):
        unique = 0
        duplicate = 0
        total = 0
        grand_total = size / self.block_size
        with io.open(filepath, 'wb', buffering=536870912) as file:
            for s in size_chunker(size, self.block_size):
                total += 1
                if random.random() <= dedup_probability and len(self.blocks) > 0 and s == self.block_size:
                    duplicate += 1
                    file.write(self.generate_duplicate_block())
                    # print("dup!")
                else:
                    unique += 1
                    file.write(self.generate_unique_block(s))
                    # print("unq!")
                sys.stdout.write("\r%d / %d blocks" % (total, grand_total))
                sys.stdout.flush()

        print("\n%d blocks written with %.2f duplicity." % (total, (float(duplicate) / (total))))


def main(options):
    D = DedupFileGenerator(options.chunk_size)
    D.write(options.file_path, options.size, options.dedup_ratio)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('size', type=int, help="Size of file to generate")
    parser.add_argument('-c', '--chunk_size', default=4096, type=int, help="Size of each chunk")
    parser.add_argument('-d', '--dedup_ratio', default=0.0, type=float, help="Dedup Ratio of file based on chunk size")
    parser.add_argument('-f', '--file_path', default="DupFile", type=str, help="Name of file")

    main(parser.parse_args())
