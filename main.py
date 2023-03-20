from open_ai.open_ai import chat, messenge
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        msg = request.form["msg"]
        chat("#zh-tw " + msg)
        return json.dumps(messenge)
    return render_template("index.html", result=messenge)


# start build server
app.run(host='0.0.0.0', port=8080)
