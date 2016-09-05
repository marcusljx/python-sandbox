""" Sandbox :: version

Description:
    Script for creating a timestamp_based _version.py file

Author:
    marcusljx

Created:
    2016-06-07
"""
import argparse
import time


class VersionTool():
    def __init__(self):
        self.time = time.clock()
        self.identifiers = {}
        self.format = []

    def update_time(self):
        self.time = time.clock()

    def set_attribute(self, key, value):
        self.identifiers[key] = value

    def get_attribute(self, key):
        try:
            return self.identifiers[key]

        except KeyError:
            print("KeyError: Key \"", key, "\" not found.")
            return None

    def add_format_keys(self, *args):
        self.format += args

    def get_format_keys(self):
        return self.format

    def __str__(self):
        return '.'.join([self.identifiers[key] for key in self.format])


def get_date_version():
    VT = VersionTool()
    VT.set_attribute("datetime", time.strftime("%Y%m%d.%H%M%S"))
    VT.add_format_keys("datetime")
    return VT.__str__()


def write_version_to_file(filepath, version_string):
    with open(filepath, 'w') as file:
        file.write("__version__ = \"" + version_string + "\"")


def main():
    P = argparse.ArgumentParser()
    P.add_argument('destination_file', help="Path to file to set version info.")
    options = P.parse_args()

    version_string = get_date_version()
    print("Updating version to ", version_string)
    write_version_to_file(options.destination_file, version_string)


if __name__ == '__main__':
    main()
