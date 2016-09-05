""" Sandbox :: issame

Description:
    Script for comparing two files on a per-byte basis

Author:
    marcusljx

Created:
    2016-07-28
"""
import argparse
import os

SECTOR_SIZE = 1024 * 1024


def compare_file(path1, path2):
    print("============================================")
    print(path1)
    print(path2)
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        data1 = f1.read(SECTOR_SIZE)
        while data1:
            if data1 != f2.read(SECTOR_SIZE):
                return False
            data1 = f1.read(SECTOR_SIZE)
        return True


def generate_file_paths(directory):
    for root, subdirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


def compare_dir(d1, d2):
    result = True
    for pair in zip([f for f in generate_file_paths(d1)], [g for g in generate_file_paths(d2)]):
        subresult = compare_file(pair[0], pair[1])
        print(subresult)
        result &= subresult
    return result


def main(options):
    if os.path.isfile(options.path1) and os.path.isfile(options.path2):
        result = compare_file(options.path1, options.path2)
    else:
        result = compare_dir(options.path1, options.path2)

    print("============================================\nALL FILES SAME: %s" % result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path1")
    parser.add_argument("path2")

    main(parser.parse_args())
