#!/urs/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page """
    # return a list of State object.
    states = list(storage.all(State).values())

    print("states_list")
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
