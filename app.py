from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tweede")
def hello_worldandere():
    x = 3
    y = x * x
    return "<p>Vanalles"+str(y)+"</p>"