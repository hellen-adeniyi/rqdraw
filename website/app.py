from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # for the databse
from flask_login import UserMixin # flask login framework

# create the flask instance
app=Flask(__name__)

#create a databse instance
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'game'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    phonenumber = db.Column(db.Integer(11), nullable=False)
    dob = db.Column(db.String(9), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    province = db.Column(db.String(20), nullable = False)

@app.route('/')
def game():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)