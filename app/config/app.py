import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG_APP = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or '736EC283F3F1BA75FA37CF2F08B8F78FEB37138379DF2D863BB7ECE395981547'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://root:test@172.17.0.2/opensara'
    SQLALCHEMY_TRACK_MODIFICATIONS = False