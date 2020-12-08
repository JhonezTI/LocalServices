from marketshop import app
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def index_pag():
    return render_template('Index.html')

@app.route('/Feedback')
def feed_pag():
    return render_template('Feed.html')

@app.route('/Welcome')
def home_pag():
    return render_template('Home.html')

@app.route('/Perfil_Autonomo')
def PerfilAUT_pag():
    return render_template('PerfilSegundario.html')

@app.route('/Recovery')
def Recovery_pag():
    return render_template('Recovery.html')

@app.route('/Sign_In')
def Sign_In():
    return render_template('Sign_In.html')

@app.route('/Sign_Up')
def Sign_Up():
    return render_template('Sign_In.html')

