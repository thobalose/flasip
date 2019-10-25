import socket

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return render_template("index.html", hostname=hostname, host_ip=host_ip)
