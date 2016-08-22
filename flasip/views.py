from flask import render_template
from app import app
import socket


@app.route('/')
def index():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return render_template("index.html", hostname=hostname, host_ip=host_ip)
