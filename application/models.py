from sqlalchemy.orm import backref, relationship
from application import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,String,Column

class Animal_Group1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))

class Animal_Group2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))