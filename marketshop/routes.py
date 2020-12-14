from marketshop import app
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home_pag():
    return render_template('Home.html')


@app.route('/All_Chat')
def All_Chat_pag():
    return render_template('All_Chat.html')

@app.route('/Feedback')
def feed_pag():
    return render_template('Feed.html')

@app.route('/Chat')
def chat_pag():
    return render_template('Chat.html')

@app.route('/Index')
def index_pag():
    return render_template('Index.html')

@app.route('/Perfil_Autonomo')
def PerfilAUT_pag():
    return render_template('PerfilSegundario.html')

@app.route('/terms')
def terms_pag():
    return render_template('terms.html')

@app.route('/Security')
def Security_pag():
    return render_template('security.html')

@app.route('/Recovery')
def Recovery_pag():
    return render_template('Recovery.html')

@app.route('/Sign_In', methods=['GET', 'POST'])
def Sign_In():
    return render_template('Sign_In.html')
    nome_usuario = request.form['User_Login']
    senha = request.form['User_Pass']

    if nome_usuario == 'admin':
        if senha == 'admin':
            return redirect('/')
        else:
            return redirect('/Sign_Up.html')
    else:
        redirect('/Sign_Up.html')


@app.route('/Sign_Up')
def Sign_Up():
    return render_template('Sign_Up.html')

@app.route('/Choose_sub')
def Choose_sub():
    return render_template('Choose_sub.html')

@app.route('/about')
def about_pag():
    return render_template('about.html')

@app.route('/we_offer')
def offer_pag():
    return render_template('we_offer.html')