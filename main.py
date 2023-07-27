from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = subprocess.run(["date"], capture_output=True)
    return "<p>Hello, World! %s</p>" % (response.stdout)