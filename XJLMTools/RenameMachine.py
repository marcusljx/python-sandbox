""" Sandbox :: RenameMachine

Description:
    Script for renaming machine

Author:
    marcusljx

Created:
    2016-08-05
"""
import argparse

from os_tools.Terminal import Terminal

RENAME_CMD = "$(gwmi win32_computersystem).Rename(\"%s\") ;; Restart-Computer"


def runCommand(commandString):
    for output in Terminal().runCommand(commandString):
        print(output)
    return output


def main(options):
    user = "-u %s" % options.username
    pw = "-p %s" % options.password
    sub_cmd = RENAME_CMD % options.new_name
    cmd = "PsExec.exe %s %s %s \"%s\"" % (options.machine_ip, user, pw, sub_cmd)
    print(cmd)
    runCommand(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("machine_ip", help="IP address of the remote machine to rename.")
    parser.add_argument("new_name", type=str, help="Name to change the remote machine to.")
    parser.add_argument("-u", "--username", help="Login username of the remote machine", default='')
    parser.add_argument("-p", "--password", help="Login password of the remote machine", default='')
    main(parser.parse_args())
