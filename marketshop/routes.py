from flask import render_template, session, redirect, url_for, request, current_app as app

from marketshop import db
from marketshop.entidades import Usuario


#----------------------------------PAGINA HOME----------------------------------

@app.route('/')
@app.route('/home')
def home_pag():
    return render_template('Home.html')


@app.route('/profile')
def profile_pag():
    return render_template('profile.html')


#                                - NavBar Home -
@app.route('/about')
def about_pag():
    return render_template('about.html')

@app.route('/we_offer')
def offer_pag():
    return render_template('we_offer.html')

@app.route('/Security')
def Security_pag():
    return render_template('security.html')

#@app.route('/Suport')
#def Suport_pag():
#   return render_template('suport.html')

@app.route('/Feedback')
def feed_pag():
    return render_template('Feed.html')

@app.route('/more')
def more_pag():
    return render_template('more.html')

@app.route('/mobile')
def mobile_pag():
    return render_template('mobile.html')


#-------------------------------FIM DA PAGINA HOME------------------------------



#---------------------------------ROTA DE LOGIN---------------------------------

# - LOGIN -
@app.route('/Sign_In', methods=['GET', 'POST'])
def Sign_In():
#    return render_template('Sign_In.html')
#    nome_usuario = request.form['User_Login']
#    senha = request.form['User_Pass']

#    if nome_usuario == 'admin':
#        if senha == 'admin':
#           return redirect('/')
 #       else:
 #           return redirect('/Sign_Up.html')
 #   else:
  #      redirect('/Sign_Up.html')
    return render_template('Sign_In.html')

# - RECUPERAÇÃO DE CONTA -
@app.route('/Recovery')
def Recovery_pag():
    return render_template('Recovery.html')

#----------------------------FIM DA ROTA DE LOGIN-------------------------------



#----------------------------ROTA PARA REGISTRAR--------------------------------

# ESCOLHER A FORMA DE REGISTRO
@app.route('/choose_sub')
def Choose_sub():
    return render_template('Choose_sub.html')


#   - PESSOA FISICA -
@app.route('/sign_Up')
def Sign_Up():
#    nome_c = request.form['n_user']
#    senha = request.form['pass_user']
#    s_conf = request.form['pass_user_conf']

#    alguem = Usuario.query.filter_by(nome=nome_c).first()

#    if alguem is not None:
#        session['mensagem'] = 'Usuário já cadastrado'
#        return redirect('/Sign_Up')
#    else:
#        if senha != s_conf:
#            session['mensagem'] = 'Senhas não conferem'
#            return redirect('/Sign_Up')
#        else:
#            novo = Usuario()
#            novo.nome = nome_c
#            novo.senha = senha

#            db.session.add(novo)
#            db.session.commit()
    return render_template('Sign_Up.html')


#   - Profissional aut -
@app.route('/Sign_Up2')
def Sign_Up2_pag():
    return render_template('Sign_Up2.html')

#  - TERMOS DE POLITICA -
@app.route('/terms')
def terms_pag():
    return render_template('terms.html')

@app.route('/registro')
def reg_pag():
    return render_template('testeRegister.html')
#----------------------FIM DA FUNÇÃO REGISTRAR----------------------------------



#----------------------------FUNÇÃO INDEX---------------------------------------

# - PAGINA INDEX -
@app.route('/Index')
def index_pag():
    return render_template('Index.html')

#                              - NAVBAR -

# - DROPDOWN PERFIL
@app.route('/Edit_profile')
def Edit_profile_pag():
    return render_template('Edit_Profile.html')

#@app.route('/Favorites')
#def Favorites_pag():
#    return render_template('Favorites.html')

#@app.route('/Historic')
#def Historic_pag():
#    return render_template('Historic.html')

#@app.route('/Config')
#def Config_pag():
#    return render_template('Config.html')

# - MENSAGENS
@app.route('/All_Chat')
def All_Chat_pag():
    return render_template('All_Chat.html')

# - NOTIFICAÇÃO
# FAZER UM BOTÃO DROPDOWN ESTILO FACEBOOK

#----------------------------FUNÇÃO INDEX---------------------------------------



#-------------------------FUNÇÃO PERFIL AUTONOM---------------------------------

@app.route('/Perfil_Autonomo')
def PerfilAUT_pag():
    return render_template('PerfilSegundario.html')

@app.route('/Chat')
def chat_pag():
    return render_template('Chat.html')

#----------------------FIM DA FUNÇÃO PERFIL AUTONOMO----------------------------



#-------------------------LOCAL PARA TESTES-------------------------------------
@app.route('/teste')
def test_pag():
    return render_template('teste.html')

@app.route('/AmbienteTeste')
def Atest_pag():
    return render_template('AmbienteTeste.html')


