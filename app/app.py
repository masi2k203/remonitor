from flask import Flask
app = Flask(__name__)

@app.route('/remonitor')
def hello_world():
    return 'Hello, Remote Flask!'