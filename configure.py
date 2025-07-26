from flask import Flask

def configure(app:Flask):
    app.config.from_pyfile('config.py')