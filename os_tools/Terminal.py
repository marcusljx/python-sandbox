""" Sandbox :: Terminal

Description:
    Class for emulating the terminal

Author:
    marcusljx

Created:
    2016-04-28
"""
import logging
import subprocess
import sys

import _common


class Terminal:
    """ Terminal class for instantiating commands in a subprocess"""
    def __init__(self, name="Terminal"):
        self.logger = logging.getLogger(name)

    def runCommand(self, commandString):
        self.logger.info("{}::{}".format(_common.timestamp(), commandString))

        try:
            p = subprocess.Popen(commandString, stdout=subprocess.PIPE, bufsize=1)
            with p.stdout:
                for line in iter(p.stdout.readline, b''):
                    sys.stdout.write(line)
                    sys.stdout.flush()
                    self.logger.log(self.logger.level, line)
                    yield line
            status = p.wait()

        except subprocess.CalledProcessError:
            self.logger.error("Command {", commandString, "} returned non-zero exit status.")
            raise

        except OSError:
            cmd = commandString.split(' ').pop()
            self.logger.error("Command not found: ", cmd)
            raise

        yield status
