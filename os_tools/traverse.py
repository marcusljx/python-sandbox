"""
    Sandbox :: filesystem_commons
        created by Marcus LJX on 2016-07-20
"""
""" Sandbox :: traverse

Description:
    module containing functions/generators for use in filesystem traversal

Author:
    marcusljx

Created:
    2016-07-20

Doctests:
"""
import os

def yield_all_dirpaths(rootdir):
    """ Generator yielding all qualified paths of directories only

    :param rootdir: Path to the root directory to traverse
    :return: Yields qualified paths of all subdirectories from root directory
    """
    for root, subdir, _ in os.walk(rootdir):
        for s in subdir:
            yield os.path.join(root, s)

def yield_all_filepaths(rootdir):
    """ Generator yielding all qualified paths of files only

    :param rootdir: Path to the root directory to traverse
    :return: Yields qualified paths of all files from root directory
    """
    for root, _, files in os.walk(rootdir):
        for f in files:
            yield os.path.join(root, f)


def find_filetype_from(rootdir, extension):
    """ Function to find files from a relative root directory

    :param rootdir: Path to the root directory to traverse
    :param extension: Extension (filetype) of file to search for
    :return: Returns a list of qualified paths matching the filetype. Each path is relative from the root directory
    """
    return [filepath for filepath in yield_all_filepaths(rootdir) if filepath.endswith(extension)]