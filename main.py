from flask import Flask, render_template, url_for
from forms import RegistrationForm
app = Flask(__name__)

preset_data = [
    {
        "one_thing": "info about one thing",
        "two_thing": "info about two thing",
        "three_thing": "info about three thing"
    },
    {
        "one_thing": "info about another one thing blah blah blah",
        "two_thing": "info about another two thing blah blah blah",
        "three_thing": "info about three thing again blah blah"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/presets")
def json_dump():
    return render_template('presets.html', title='Base Data', preset_data = preset_data)

# run on debug mode to not re-start server after changes
if __name__ == '__main__':
    app.run(debug = True)