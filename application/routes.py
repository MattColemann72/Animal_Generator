from application import app
from application.forms import AnimalNameSubmit
from flask import render_template

@app.route('/')
def index():
    form = AnimalNameSubmit()
    
    return render_template('index.html', title="Home Page")
    #return '<h1>Hello World</h1>'
