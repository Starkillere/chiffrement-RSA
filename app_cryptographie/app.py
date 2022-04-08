#-*- coding:utf-8 -*-

from flask import Flask, render_template, request
import algorithme_gestion_donnees as gd
from algorithme_chiffrement_rsa import RSA 

app = Flask(__name__)

config = {}

@app.route('/')
def aceuille():
    return render_template('aceuille.html')

@app.route('/Authentification', methods=["GET", "POST"])
def Authentification():
    global config
    if request.method =="POST":
        identifiant = request.form["identifiant"]
        password = request.form['password']
        if identifiant != '' and password != '':
            if gd.login(identifiant, password, 'database.db') != False:
                config = gd.login(identifiant, password, 'database.db')
                return render_template('menu_principale.html')
            else:
                return render_template('Authentification.html', texte='Incorrect')
        else:
            return render_template('Authentification.html')
    else:
        return render_template('Authentification.html')

@app.route('/S_inscrire', methods=["GET", "POST"])
def sigin():
    global config
    if request.method =="POST":
        identifiant = request.form["identifiant"]
        password = request.form['password']
        if identifiant != '' and password != '':
            if gd.user_register(identifiant, password, 'database.db') != False:
                config = gd.login(identifiant, password, 'database.db')
                return render_template('menu_principale.html')
            else:
                return render_template('/S_inscrire.html', text='Nom déjà utilisé')
        else:
            return render_template('/S_inscrire.html')
    else:
        return render_template('/S_inscrire.html')

@app.route('/menu_principal')
def menu_p():
    return render_template('menu_principale.html')

@app.route('/menu_text')
def menu_ct():
    return render_template('chiffrement_texte/menu_pricipale_texte.html')

@app.route('/CHIFFRER-TEXT', methods=["GET", "POST"])
def chiffrement_text():
    if request.method =="POST":
        clef = request.form['key']
        texte = request.form['texte']
        if clef == 'the key':
            my_rsa = RSA()
            chiffre = my_rsa.chiffrement(int(config['key publique'][0]), int(config['key publique'][1]), texte)
            return render_template('chiffrement_texte/menu_chiffre.html', texte=chiffre)
        else:
            return render_template('chiffrement_texte/menu_chiffre.html')
    else:
        return render_template('chiffrement_texte/menu_chiffre.html')

@app.route('/DECHIFFRER-TEXT', methods=["GET", "POST"])
def dechiffrement_text():
    if request.method =="POST":
        clef = request.form['key']
        texte = request.form['texte']
        if clef == 'the key':
            my_rsa = RSA()
            chiffre = my_rsa.dechiffrement(int(config['key priver'][0]), int(config['key priver'][1]), texte)
            return render_template('chiffrement_texte/menu_dechiffre.html', texte=chiffre)
        else:
            return render_template('chiffrement_texte/menu_dechiffre.html')
    else:
        return render_template('chiffrement_texte/menu_dechiffre.html')

if __name__ == "__main__":
    app.run(debug=True)