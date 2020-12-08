from marketshop import app
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def index_pag():
    return render_template('Index.html')

@app.route('/Home')
def home_pag():
    return render_template('Home.html')