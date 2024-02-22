from flask import Flask 

def create_app():
    app=Flask(__name__)
    app.confug['SECRET_KEY'] = 'draw'

    from .app import app
    from .auth import auth

    app.register_blueprint(app, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app