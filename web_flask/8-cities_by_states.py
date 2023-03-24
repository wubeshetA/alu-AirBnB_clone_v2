#!/usr/bin/python3
""" A flask server to return id and name of a State object

Returns:
    _type_: _description_
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page """
    # return a list of State object.
    states = list(storage.all(State).values())

    print("states_list")
    print(states)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ display a HTML page """
    # return a list of State object.
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda state: state.name)
    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    # store states in a dictionary where the key is state and value is list of cities
    states_dict = {}
    for state in states:
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            states_dict[state] = sorted(
                state.cities, key=lambda city: city.name)
        else:
            states_dict[state] = sorted(
                state.cities(), key=lambda city: city.name)

    # print(states_dict)
    # for state in states_dict:
    #     print(state.name)
    #     for city in states_dict[state]:
    #         print("         ",city.name)
    return render_template('8-cities_by_states.html',
                           states=states_dict)


@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
