from flask import Flask
app = Flask(sashu)

@app.route("/")
def hello():
    return "Hello, World!"
