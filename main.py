from flask import Flask, request
import  os
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return("Hello World!", 200)


if(__name__=='__main__'):
    app.run(host="0.0.0.0", port=8080)