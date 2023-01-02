from flask import Flask, render_template, request  # needed to use flask.
from app import *  # imports all functions from app.py.

weather_app = Flask(__name__)  # create a new application instance called weather_app.


@weather_app.route('/', methods=('GET', 'POST'))  # Sets an app rout and gives it GET & POST methods.
def search():
    if request.method == "POST":  # checks if the user is sending a POST request.
        try:  # Checks if location_to_dict raised a typeError because the location was not valid.
            location_dict = location_to_dict(request.form["input_location"])
        except TypeError:  # send user to Error page.
            return render_template('weather_error.html')

        return render_template('weather_main.html', location_dict=location_dict)

    return render_template('weather_search.html')


if __name__ == "__main__":
    print(location_to_dict("holon"))
    weather_app.run(host='0.0.0.0')  # Runs weather_app.
