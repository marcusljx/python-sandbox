"""
    Sandbox :: filesystem_commons
        created by Marcus LJX on 2016-07-20
"""
from __future__ import print_function

import os

def yield_all_dirpaths(rootdir):
    for root, subdir, _ in os.walk(rootdir):
        for s in subdir:
            yield os.path.join(root, s)

def yield_all_filepaths(rootdir):
    for root, _, files in os.walk(rootdir):
        for f in files:
            yield os.path.join(root, f)

def find_file_by(rootdir, extension):
    return [filepath for filepath in yield_all_filepaths(rootdir) if filepath.endswith(extension)]



def main():
    ext = ['txt', 'py']
    x = [x for e in ext for x in find_file_by("D:\\", e)]
    print(x)
    pass


if __name__ == '__main__':
    main()
