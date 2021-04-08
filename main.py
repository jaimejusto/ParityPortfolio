from flask import Flask, render_template, url_for
from forms import RegistrationForm
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')



# run on debug mode to not re-start server after changes
if __name__ == '__main__':
    app.run(debug = True)