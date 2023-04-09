#!/usr/bin/python3
"""
starts a Flask web application with routes and variables
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(what):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    states = list(storage.all(State).values())
    states.sort(key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
