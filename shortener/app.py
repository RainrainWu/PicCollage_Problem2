"""
PicCollage_Problem2.shortener.app is the backbone process of shortener
server.
"""

from flask import Flask, request, redirect
from loguru import logger

from shortener import digest, database
from shortener.config import (
    LOG_DIRECTORY,
    LOG_ROTATION,
    LOG_RETENTION,
)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """
    hello handles the root route and response Hello World message.
    """
    return {"message": "Hello World"}


@app.route("/<string:flag>", methods=["GET"])
def short(*, flag: str):
    """
    short handles the process of registering new mapping.
    """
    url = database.get_source(flag)
    if url == "":
        return {"error": "Flag not found"}, 400
    database.add_visited_times(flag)
    return redirect(url)


@app.route("/user/submit", methods=["POST"])
def submit():
    """
    submit handles the process of registering new mapping.
    """
    content = request.json
    if "tag" in content:
        if not digest.validate_tag(content["tag"]):
            return {"error": "Invalid tag"}, 400

    flag = digest.generate_flag(content)
    post_id = database.register_flag(flag, content["source"])
    if post_id == "":
        return {"error", "Internal server error"}, 500
    return {"flag": flag}, 200


@app.route("/user/metrix/<string:flag>")
def metrix(*, flag: str):
    """
    metrix handles the requests for flag metrix.
    """
    data = database.get_metrix(flag)
    if data == {}:
        return "Flag not found", 400
    return data, 200


@app.route("/admin/dashboard")
def dashboard():
    """
    short handles the dashboard demostration.
    """
    return database.get_mapping(), 200


@app.route("/admin/delete", methods=["POST"])
def delete():
    """
    delete handles the process of deleting existed flag.
    """
    content = request.json
    if "flag" not in content:
        return {"error": "Please specified a flag"}, 400

    document = database.get_document(content["flag"])
    if document is None:
        return {"error": "Flag not found"}, 400

    result = database.delete_document(content["flag"])
    if not result:
        return {"error", "Internal server error"}, 500

    return {"message": "success"}, 200


if __name__ == "__main__":
    logger.add(
        LOG_DIRECTORY + "file_{time}.log",
        rotation=LOG_ROTATION,
        retention=LOG_RETENTION
    )
    app.run()
