#!/usr/bin/python3
""" script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display HTML page with the list of all State objects present"""
    states = storage.all(State).values()
    list_states = []
    for key in storage:
        list_states.append(states[key])
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_appcontext():
    """ remove the current SQLAlchemy Session2"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)