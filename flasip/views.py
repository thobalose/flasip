import socket

from flask import Flask, render_template

app = Flask(__name__)


def get_hostname():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "127.0.0.1"
    return hostname, ip


@app.route('/')
def index():
    hostname = get_hostname()[0]
    ip = get_hostname()[1]
    return render_template("index.html", hostname=hostname, host_ip=ip)
