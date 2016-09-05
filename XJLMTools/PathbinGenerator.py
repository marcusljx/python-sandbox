""" Sandbox :: PathbinGenerator

Description:
    Moves a copy of a script to the specified directory (on PATH), and creates an executable for it (windows).

Author:
    marcusljx

Created:
    2016-06-24
"""
import argparse
import os

cmdtext = \
    r"""
    @echo off

    C:\Program Files\Python35\python.exe %s %%*
    """


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("script_path", help="Script to call from function.")
    parser.add_argument("path_dir", help="Directory path to store bin/cmd/bat/sh file")
    parser.add_argument("-c", "--command", help="Command to call function", default=None)
    options = parser.parse_args()

    cmd = options.command
    if not cmd:
        cmd = os.path.splitext(os.path.basename(options.script_path))

    with open(os.path.join(options.path_dir, "%s.cmd" % cmd), 'w') as f:
        f.write(cmdtext % options.script_path)


if __name__ == '__main__':
    main()
