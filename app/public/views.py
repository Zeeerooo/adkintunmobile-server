from flask import render_template, json, jsonify, redirect

from app import app


@app.route("/")
def index():
    return redirect("http://www.adkintunmobile.cl", code=302)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


@app.route("/terms_and_conditions")
def terms_and_conditions():
    try:
        data = json.load(
            open("app/static/text/terms_and_conditions.json", "r"))
        return jsonify(data)
    except Exception as e:
        return page_not_found(e)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
