from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username(root):pasword@'
# #'sqlite:///data.db' #'mysql+pymysql://root:crudapppass@host/fantasyfootball' DB location
# app.config['SECRET_KEY'] = 'A SOOCRET KOO'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)