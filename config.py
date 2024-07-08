import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False
