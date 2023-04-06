from open_ai.open_ai import chat, messenge
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        msg = request.json.get('msg')
        gptResponse = chat("#zh-tw " + msg)
        response = jsonify({'response': gptResponse})
        response.headers['Content-Type'] = 'application/json'
        return response

    return render_template("index.html", result=messenge)


if __name__ == '__main__':
    app.debug = True
    # start build server
    app.run(host='0.0.0.0', port=8080)
