from flask import Flask
from routes.urls import blueprint

app =  Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
app.register_blueprint(blueprint)
app.run(host='127.0.0.1', port=5000, debug=True)