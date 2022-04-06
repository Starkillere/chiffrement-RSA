#-*- coding:utf-8 -*-

from flask import Flask, render_template, request
import algorithme_gestion_donnees as gd

app = Flask(__name__)

config = {}

@app.route('/')
def aceuille():
    return render_template('aceuille.html')

@app.route('/Authentification', methods=["GET", "POST"])
def Authentification():
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
    if request.method =="POST":
        identifiant = request.form["identifiant"]
        password = request.form['password']
        if identifiant != '' and password != '':
            if gd.user_register(identifiant, password, 'database.db') != False:
                config = gd.login(identifiant, password, 'database.db')
                return render_template('menu_principale.html')
            else:
                return render_template('/S_inscrire.html')
        else:
            return render_template('/S_inscrire.html')
    else:
        return render_template('/S_inscrire.html')

@app.route('/menu_principal')
def menu_p():
    return render_template('menu_principale.html')

if __name__ == "__main__":
    app.run(debug=True)