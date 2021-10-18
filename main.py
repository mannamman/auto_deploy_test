from flask import Flask, request
import  os
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    env1 = os.environ["env1"]
    env2 = os.environ["env2"]
    env1_type = type(env1)
    env2_type = type(env2)
    return(f"{env1} {env1_type}, {env2} {env2_type}", 200) 


if(__name__=='__main__'):
    app.run(host="0.0.0.0", port=8080)