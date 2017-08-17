from flask import Flask, jsonify
import consul
import os
import socket

app = Flask(__name__)

likes=0
host=os.environ['CONSUL_HOST']
port=os.environ['CONSUL_PORT']
hostname=socket.gethostname()
print("hostname=%s" % (hostname))
print("\nCONSUL_HOST=%s\nCONSUL_PORT=%s\n" % (host, port))
# connect to consul and register
c = consul.Consul(host=host,port=port)
c.agent.service.register('python', 
    address=hostname,
    port=5000,
    tags=["language"],
    check=consul.Check.http(
        url=("http://%s:%s/health" % (hostname, 5000)),
        interval="5s"
    )
)


@app.route("/health")
def healthy():
    return 'healthy'

@app.route("/language")
def language():
    return jsonify({
        'name': 'python',
        'description': 'A interpreter language',
        'likes': likes
    })

@app.route("/language/like", methods=['POST'])
def language_like():
    global likes
    likes=likes+1
    return jsonify({
        'name': 'python',
        'description': 'A interpreter language',
        'likes': likes
    })
