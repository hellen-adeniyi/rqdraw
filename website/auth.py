from flask import Blueprint
# routes that are for authentication

auth = Blueprint('auth', __name__)  # created a blueprint  

@auth.route('/login')
def login():
    return "Return the login page"
