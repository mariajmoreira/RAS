from flask.helpers import make_response
from .controller import createUser, loginUser
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user, logout_user
import re


auth = Blueprint('auth',__name__)

@auth.route('/signup', methods=['GET','POST'])
def signup(): 
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        re_str = re.compile('^\ *[a-zA-Z]{4,120}\ *$')
        re_pass = re.compile('^.{8,120}$')
        re_mail = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if not re_str.match(first_name):
            flash('Invalid first name.', category='ERROR')
        elif not re_str.match(last_name):
            flash('Invalid last name.', category='ERROR')
        elif not re_pass.match(password):
            flash('Password must have 8 or more characters.', category='ERROR')
        elif not re_mail.match(email):
            flash('Invalid email.', category='ERROR')
        else:
            try:
                createUser(first_name, last_name, email, generate_password_hash(password,"sha256"))
                flash('Account created.', category='SUCCESS')
                return redirect(url_for('views.home'))
            except Exception:
                flash('E-mail already registed.', category='ERROR')

    return render_template('signup.html')


@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    
    flashs = []

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        flashs, page = loginUser(email, password, remember = True if request.form.get('remember') else False)

        for f in flashs:
            flash(f)

        return redirect(url_for(page))
    
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))