from flask import Flask

# Variable
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/one")
def route_one():
    return "<h1>Hello, World! This is route one.</h1>"

@app.route("/two")
def route_two():
    return "<h1>Hello, World! This is route two.</h1>"

@app.route("/custom/<name>")
def custom_route(name):
    return f"<h1>Hello, {name}! This is a custom route.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
