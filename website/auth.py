from flask import Blueprint
# routes that are for authentication

auth = Blueprint('auth', __name__)  # created a blueprint  

@auth.route('/login')
def login():
    return "Return the login page"

@auth.route('/logout')
def login():
    return "Return the logout page"

@auth.route('/sign in')
def login():
    return "Return the Signin page"

@auth.route('/sign-up')
def login():
    return "Return the Sign up"