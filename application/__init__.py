# import sys
# sys.path.append('/home/mattc/dev/bin/')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# #'sqlite:///data.db' #'mysql+pymysql://root:password@host/dbname' DB location
# app.config['SECRET_KEY'] = 'sosecret-itsunreal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)