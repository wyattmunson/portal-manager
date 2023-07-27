import subprocess
import re
import time

# INTRO MESSAGE
def introMessage():
    print("WELCOME TO WAS")
    print("")
    print("           .---.   ,---,       .--.--.    ")
    print("          /. ./|  '  .' \     /  /    '.  ")
    print("      .--'.  ' ; /  ;    '.  |  :  /`. /  ")
    print("     /__./ \ : |:  :       \ ;  |  |--`   ")
    print(" .--'.  '   \' .:  |   /\   \|  :  ;_     ")
    print("/___/ \ |    ' '|  :  ' ;.   :\  \    `.  ")
    print(";   \  \;      :|  |  ;/  \   \`----.   \ ")
    print(" \   ;  `      |'  :  | \  \ ,'__ \  \  | ")
    print("  .   \    .\  ;|  |  '  '--' /  /`--'  / ")
    print("   \   \   ' \ ||  :  :      '--'.     /  ")
    print("    :   '  |--' |  | ,'        `--'---'   ")
    print("     \   \ ;    `--''                     ")
    print("      '---'                               ")
    print("")
                                          


    print("AUTO STARTER LOADING IN 5 SECONDS...")
    print("Interrupt the Auto Starter with [CTRL] + [C]")
    print("")
    time.sleep(5)

# introMessage()

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

# installHeadlines = []

class Warden:
    def __init__(self, fullTopicList):
        self.fullTopicList = fullTopicList
        self.deps = None
    
    def splitCommandString(self, string):
        # split into array if not already array type
        # certain commands have combined strings
        if type(string) == list:
            commandArray = string
        else:
            commandArray = string.split(" ")

            for x in range(len(commandArray)):
                commandArray[x] = commandArray[x].strip()
    
        return commandArray


    def runCommand(self, commandArray):
        print("Running command:", commandArray)
        command = subprocess.run(commandArray, capture_output=True, text=True, shell=True)
        print("Got command response:", command)
        return command


    def runCommandWithCheck(self, obj):
        commandArray = self.splitCommandString(obj["command"])
        command = self.runCommand(commandArray)

        # Check for failure
        if obj["failure"] == "returncode":
            if obj["failureValue"] == "nonzero" and command.returncode > 0:
                print("FAILED: ", obj["topic"])
                return False

        # Check for true, warn when failure or success not detected
        if obj["success"] == "returncode":
            if obj["successValue"] == 0 and command.returncode == 0:
                print("SUCCESS: ", obj["topic"])
                return True

        # success not detected, returning True for now
        print("WARN: did not meet success or failure criteria for:", obj["topic"])

    # START OF INSTALL SCRIPTS
    def installGithubCli():
        pass
    # END OF INSTALL SCRIPTS

    # CHECK PACKAGE
    def checkPackage(self, headline):
        # Check to see if a package was installed
        config = fullConfigMap[headline]
        return self.runCommandWithCheck(config)

    def installPackage(self, headline):
        print("Package installing...")
        config = fullConfigMap[headline]
        return self.runCommandWithCheck(config)
    

    def aptGetUpdate(self):
        print("INFO", "Updating apt-get")
        subprocess.run(["sudo", "apt-get", "update"])

    def processDeps(self):
        print("Processing deps...")
        uniqueTopics = []
        for topic in self.fullTopicList:
            match = re.match(r"deps/\w+/check$", topic)
            if match:
                if topic not in uniqueTopics:
                    uniqueTopics.append(topic)
        print("ALL TOPICS", uniqueTopics)
        self.deps = uniqueTopics

        for x in uniqueTopics:
            print("\n=== CHECKING ===", x)
            isInstalled = self.checkPackage(x)
            print("Is installed:", isInstalled)
            if not isInstalled:
                # Get install headline
                splitHeadline = x.split("/")[0:2]
                splitHeadline.append("install")
                installHeadline = "/".join(splitHeadline)

                installSuccessful = self.installPackage(installHeadline)
                if installSuccessful:
                    print("Installed succesfully")
                else:
                    print("Failed to install")
    


warden = Warden(fullTopicList)
warden.processDeps()


def mainRunner():
    print("HELLO")

