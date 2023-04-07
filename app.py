from flask import Flask, render_template, request, jsonify, abort
from dotenv import load_dotenv
import os

from open_ai.open_ai import chat
import line.linebot as line


def create_app():
    load_dotenv()
    app = Flask(__name__)
    # dev
    if os.getenv("ENV") == "dev":
        app.debug = True
    # line
    line.lineInit()

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            msg = request.json.get("msg")

            gptResponse = chat("#zh-tw " + msg)

            response = jsonify({"response": gptResponse})
            response.headers["Content-Type"] = "application/json"

            return response

        return render_template("index.html")

    @app.route("/linebot", methods=["POST"])
    def linebot():
        # get X-Line-Signature header value
        signature = request.headers["X-Line-Signature"]

        # get request body as text
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)

        err = line.lineHandle(body, signature)
        if err:
            abort(400)

        return "ok"

    return app


if __name__ == "__main__":
    app = create_app()
    # start build server
    app.run(host="0.0.0.0", port=8080)
