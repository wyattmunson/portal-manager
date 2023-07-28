import subprocess
import Warden

fullConfigMap = {
    "deps/git/check": {
        "topic": "install/verify/git",
        "command": ["git --version"],
        "success": "returncode",
        "successValue": 0,
        "failure": "returncode",
        "failureValue": "nonzero"
    },
    "deps/git/install": {
        "command": "sudo apt-get install git -y",
        "success": "returncode",
        "successValue": 0,
        "failure": "returncode",
        "failureValue": "nonzero"
    },
    "deps/docker/check": {
        "topic": "install/verify/docker",
        "command": ["docker --version"],
        "success": "returncode",
        "successValue": 0,
        "failure": "returncode",
        "failureValue": "nonzero"
    },
    "deps/docker/install": {
        "command": ["sudo sh install-docker.sh"],
        "success": "returncode",
        "successValue": 0,
        "failure": "returncode",
        "failureValue": "nonzero"
    },
    "deps/tiki/check": {
        "topic": "install/verify/docker",
        "command": ["tiki --version"],
        "success": "returncode",
        "successValue": 0,
        "failure": "returncode",
        "failureValue": "nonzero"
    }
}

fullTopicList = [
    "deps/git/check",
    "deps/git/install",
    "deps/git/upgrade",
    "deps/docker/check",
    "deps/tiki/check"
]

warden = Warden(fullTopicList)

def getContainers():
    print("Checking containers...")

def getCoreMetrics():
    commands = [
        "uname -a",

    ]

def getMemoryUsage():
    cmd = """free | jq --raw-input --slurp 'split("\n")'"""
    warden.runCommand([cmd])

getMemoryUsage()

## VALIDATED
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

    # TODO: return value (return code, body)

def systemctl_start(service, vanity=False):
    # Return Codes [LSB/systemd]
    # 0 - Command not reject, may not have started service
    # 5 - Service is not found

    command = "sudo systemctl start %s" % (service)
    res = run_command(command)
    print("GOT RES", res)
    return_code = res.returncode

    if vanity:
        # returns array with each line as element
        formatting = """ | head | jq --raw-input --slurp 'split("\n")'"""
        res = run_command(command + formatting)

    # handle change config
    if res.stderr:
        pass
    # TODO: return value (return code, body)


def systemctl_daemon_reload():
    # Return Codes [LSB/systemd]
    # 0 - Command not reject, may not have started service
    # 5 - Service is not found

    command = "sudo systemctl daemon-reload"
    res = run_command(command)
    print("GOT RES", res)
    return_code = res.returncode

    # handle change config
    if res.stderr:
        pass
    # TODO: return value (return code, body)


def systemctl_stop(service, vanity=False):
    # Return Codes [LSB/systemd]
    # 0 - Command not reject, may not have started service
    # 5 - Service is not found

    command = "sudo systemctl stop %s" % (service)
    res = run_command(command)
    print("GOT RES", res)
    return_code = res.returncode


    # handle change config
    if res.stderr:
        pass
    # TODO: return value (return code, body)