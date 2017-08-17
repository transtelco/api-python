from flask import Flask, jsonify
app = Flask(__name__)

likes=0

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
