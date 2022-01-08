from werkzeug.security import check_password_hash
from flask_login import login_user
from .models import User
#from enum import Enum, unique
from . import db


def createUser(first_name, last_name, email, password):
    new_user = User(email, password, first_name, last_name)
    db.session.add(new_user)
    db.session.commit()

    
def loginUser(email, password, remember = True):
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return ['Please check your login details and try again.'], 'auth.login'

    else:
        login_user(user, remember=remember)
        return [], 'views.home'