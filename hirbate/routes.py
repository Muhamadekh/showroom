from flask import render_template, url_for, flash
from hirbate import app
from hirbate.forms import RegistrationForm





@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title='Home Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Submitted suscessfully' 'success')
    return render_template('register.html', title='Sign Up', form=form)
