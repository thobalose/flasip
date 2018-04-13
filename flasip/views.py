from flask import render_template
from app import app
import socket
import os


@app.route('/')
def index():
    hostname = os.getenv(
        'DEFAULT_VERSION_HOSTNAME') or socket.gethostname()
    host_ip = os.getenv('SERVER_SOFTWARE',
                        '') or socket.gethostbyname(hostname)
    return render_template("index.html", hostname=hostname, host_ip=host_ip)
