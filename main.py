from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import forms


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
csrf = CSRFProtect(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        return redirect('userDashboard')
    return render_template('login.html', form = form)

@app.route('/userDashboard')
def userDashboard():
    return render_template('userDashboard.html')
@app.route("/presets")
def json_dump():
    return render_template('presets.html', title='Base Data', preset_data = preset_data)

# run on debug mode to not re-start server after changes
if __name__ == '__main__':
    app.run(debug = True)