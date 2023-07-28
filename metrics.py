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