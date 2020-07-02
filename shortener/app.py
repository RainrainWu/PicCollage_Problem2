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
    return {"message": "Welcome to shortener!"}


@app.route("/<string:flag>", methods=["GET"])
def short(*, flag: str):
    """
    short handles the process of registering new mapping.
    """
    url = database.get_source(flag)
    if url == "":
        logger.info("Flag not found")
        return {"error": "Flag not found"}, 400
    database.add_visited_times(flag)
    logger.info("Redirect {FLAG} to {URL}".format(FLAG=flag, URL=url))
    return redirect(url)


@app.route("/user/submit", methods=["POST"])
def submit():
    """
    submit handles the process of registering new mapping.
    """
    content = request.json
    if "tag" in content:
        if not digest.validate_tag(content["tag"]):
            logger.info("Invalid tag")
            return {"error": "Invalid tag"}, 400

    flag = digest.generate_flag(content)
    post_id = database.register_flag(flag, content["source"])
    if post_id == "":
        logger.error("Internal server error")
        return {"error", "Internal server error"}, 500
    logger.debug(
        "Register {SOURCE} to {FLAG}".format(SOURCE=content["source"], FLAG=flag)
    )
    return {"flag": flag}, 200


@app.route("/user/metrix/<string:flag>", methods=["GET"])
def metrix(*, flag: str):
    """
    metrix handles the requests for flag metrix.
    """
    data = database.get_metrix(flag)
    if data == {}:
        logger.info("Flag not found")
        return {"error": "Flag not found"}, 400
    logger.debug("Scrape {FLAG} metrix".format(FLAG=flag))
    return data, 200


@app.route("/admin/dashboard", methods=["GET"])
def dashboard():
    """
    short handles the dashboard demostration.
    """
    logger.debug("Show dashboard")
    return database.get_mapping(), 200


@app.route("/admin/delete", methods=["POST"])
def delete():
    """
    delete handles the process of deleting existed flag.
    """
    content = request.json
    if "flag" not in content:
        logger.info("Flag not specified")
        return {"error": "Please specified a flag"}, 400

    document = database.get_document(content["flag"])
    if document is None:
        logger.info("Flag not found")
        return {"error": "Flag not found"}, 400

    result = database.delete_document(content["flag"])
    if not result:
        logger.error("Internal server error")
        return {"error", "Internal server error"}, 500

    return {"message": "success"}, 200


if __name__ == "__main__":
    logger.add(
        LOG_DIRECTORY + "file_{time}.log",
        rotation=LOG_ROTATION,
        retention=LOG_RETENTION,
    )
    app.run()
