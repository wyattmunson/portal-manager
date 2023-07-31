from flask import Flask
import subprocess
import re


def split_string(string):
    # split into array if not already array type
    # certain commands have combined strings
    if type(string) == list:
        commandArray = string
    else:
        commandArray = string.split(" ")

        for x in range(len(commandArray)):
            commandArray[x] = commandArray[x].strip()

    return commandArray


def run_command(command, stdout_as_text=True):
    command_array = split_string(command)
    response = subprocess.run(command_array, capture_output=True, text=stdout_as_text)
    return response


def check_version(stdout, min_ver=None, max_ver=None):
    print("IN VER:", stdout)
    regex = r"\d+(\.\d+)+"
    ver_string = re.search(regex, stdout)
    ver_string = str(ver_string.group())
    print("OUT VER:", ver_string)
    if not stdout:
        # check version
        pass
    ver_arr = ver_string.split(".")
    print(ver_arr)


ressi = run_command("docker --version", stdout_as_text=True)
print(ressi)
print(ressi.stdout)
ver_check = check_version(ressi.stdout)
print(ver_check)


def systemctl_stats(service, vanity=False):
    # Return Codes [LSB/systemd]
    # 0 - Online
    # 1 - Program dead and lock file/unit not failed
    # 2 - program dead and no lock/unused
    # 3 - Not running Inactive
    # 4 - Service is not found
    command = "sudo systemctl status %s" % (service)
    res = run_command(command)
    print("GOT RES", res)
    return_code = res.returncode

    if vanity:
        # returns array with each line as element
        formatting = """ | head | jq --raw-input --slurp 'split("\n")'"""
        res = run_command(command + formatting)


# systemctl_start("portal-manager")
