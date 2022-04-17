#-*-  coding:utf-8 -*-

import sqlite3

"""    
       *** creattable.py ***

       Création des Table:
              - gestionnaire : contient tout les mot de passe et compte associé.
              - user : contient tout les utilisateur 
"""

def creat_gestionnaire_table():
       """
              *** creat_gestionnaire_table ***
       
              Création de la Table gestionnaire
              colonnes:
              --------
                     id: id de l'utilisateur
                     platforme: la platforme pour la quelle on souhaite enregistré notre mot de passe
                     nom: pseudo sur la platforme
                     password: notre mot de passe sur la platforme
                     mail: adresse mail utilisé sur la platforme
       """
       con = sqlite3.connect('database.db')
       cursor = con.cursor()

       cursor.execute('''CREATE TABLE IF NOT EXISTS gestionnaire (
                         id INTEGER NOT NULL,
                         platforme TEXT NOT NULL,
                         nom TEXT NOT NULL,
                         password TEXT NOT NULL,
                         mail TEXT   
                  );''')
       con.commit()
       con.close() 

def creat_user_table():
       """
              *** creat_user_table ***

              Création de la Table user
              colonnes:
              ---------
                     id : position de l'utilisateur dans la table
                     nonm: identifiant de l'utilisateur
                     master_password : mot de pass de l'utilisateur (hasher)
                     public_key: master key de l'utilisteur (chiffré)
                     privet_key:

       """
       con = sqlite3.connect('database.db')
       cursor = con.cursor()
       cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         nom TEXT NOT NULL,
                         master_password TEXT NOT NULL,
                         public_key TEXT NOT NULL,
                         privet_key TEXT NOT NULL,
                         img TEXT NOT NULL
                  );''')
       con.commit()
       con.close()
       
creat_user_table()