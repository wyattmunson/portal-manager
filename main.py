from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
    # TODO: This should return the FE
    response = subprocess.run(["date"], capture_output=True)
    return "<p>Hello, World! %s</p>" % (response.stdout)

# get list of running containers

# where it all went wrong
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=True)