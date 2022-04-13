#-*- coding:utf-8 -*-

import sqlite3
import hashlib
from algorithme_keys_generator_rsa import generate_keys
from  algorithme_steganographie import random_image_key

def user_register(nom:str, master_password:str, database:str):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = ? "
        cursor.execute(requete, [(nom)])
        user = cursor.fetchone()
        if user == None:
            my_pass = generate_keys()
            my_image = random_image_key()
            public_key = my_pass['key publique']
            privet_key = my_pass['key priver']
            requete = "insert into user (nom, master_password, public_key, privet_key, img) values (?, ?, ?, ?, ?)"
            cursor.execute(requete, [(nom), (hashlib.sha1(master_password.encode()).hexdigest()), f'{str(public_key[0])}, {str(public_key[1])}', f'{str(privet_key[0])}, {str(privet_key[1])}', my_image])
            connection.commit()
            return {'key publique':my_pass['key publique'], 'key priver':my_pass['key priver'], 'hote':my_image}
    return False

def login(nom:str, master_password:str, database:str):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        requete = "select * from user WHERE nom = ? AND master_password = ?"
        cursor.execute(requete, [(nom), (hashlib.sha1(master_password.encode()).hexdigest())])
        user = cursor.fetchone()
        if user != None:
            public_key = tuple(user[3].split(','))
            privet_key =  tuple(user[4].split(','))
            return {'key publique':public_key, 'key priver':privet_key, 'hote':user[5]}
    return False

if __name__ == '__main__':
    print(user_register('Anrezki', '123456', 'database.db'))