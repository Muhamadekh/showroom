from flask import render_template, url_for, flash, redirect
from hirbate import app, bcrypt, db
from hirbate.forms import RegistrationForm
from hirbate.models import User, Car





@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title='Home Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.username.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'An account has been created for {form.username.data} suscessfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Sign Up', form=form)
