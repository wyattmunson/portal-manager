from flask import Flask
import subprocess

app = Flask(__name__)

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

def run_command(command):
    command_array = split_string(command)
    response = subprocess.run(command_array, capture_output=True, text=True)
    return response

@app.route("/")
def hello_world():
    # TODO: This should return the FE
    response = subprocess.run(["date"], capture_output=True, text=True)
    return "<p>Hello, World! %s</p>" % (response.stdout)

# get list of running containers

# where it all went wrong
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=True)