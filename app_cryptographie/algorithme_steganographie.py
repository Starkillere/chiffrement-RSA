#-*- coding:utf-8 -*-

import numpy as np
from PIL import Image
import random

def random_image_key():
    images = [
        'static\\images\\super.png',
        'static\\images\\waterfall-ge75953c51_1920.jpg',
        'static\\images\\tree-gfe7c44327_1280.jpg',
        'static\\images\\programming-g669be4625_1920.png',
        'static\\images\\matrix-g51ec18d3e_1280.jpg',
        'static\\images\\math-gc81f6134f_1920.jpg',
        'static\\images\\lune _1o.jpg',
        'static\\images\\fjord-g090d5ce98_1920.jpg',
        'static\\images\\cook-ge6e8d4968_1920.jpg',
        'static\\images\\code-g30c18b112_1920.jpg'
    ]
    return random.choice(images)

class Steganographie:
    def __init__(self, hote):
        self.hote = Image.open(hote)
        self.tableau_hote = np.array(self.hote)
        self.nb_ligne_hote = len(self.tableau_hote)
        self.nb_colonne_hote = len(self.tableau_hote[0])

    def encode(self, image:str) -> bool:
        image_o = Image.open(image)
        tableau_hote = self.tableau_hote
        tableau_image =  np.array(image_o)
        if len(tableau_image) > self.nb_ligne_hote:
            tableau_image = tableau_image[:len(tableau_hote)]
        #if len(tableau_image[0]) > self.nb_colonne_hote:
            #for i in range(len(tableau_image)):
                #tableau_image[i] = tableau_image[i][:len(tableau_hote[0])]
        for i in range(self.nb_ligne_hote):
            for j in range(self.nb_colonne_hote):
                for p in range(3):
                    valeur_rgb_hote_bin = bin(tableau_hote[i][j][p])[2:]
                    valeur_rgb_image_bin = bin(tableau_image[i][j][p])[2:]
                    while len(valeur_rgb_hote_bin) < 8:
                        valeur_rgb_hote_bin = '0'+valeur_rgb_hote_bin
                    while len(valeur_rgb_image_bin) < 8:
                        valeur_rgb_image_bin = '0'+valeur_rgb_image_bin
                    new_value_bin = valeur_rgb_hote_bin[:4] + valeur_rgb_image_bin[:4]
                    tableau_image[i][j][p] = int(new_value_bin,2)
        cacher_image = Image.fromarray(tableau_image)
        cacher_image.save('hide.png')
        return True

    def decode(self, image):
        image_o = Image.open(image)
        tableau_image =  np.array(image_o)
        if len(tableau_image[0]) > self.nb_colonne_hote:
            return False
        for i in range(self.nb_ligne_hote):
            for j in range(self.nb_colonne_hote):
                for p in range(3):
                    valeur_rgb_image_bin = bin(tableau_image[i][j][p])[2:]
                    while len(valeur_rgb_image_bin) < 8:
                        valeur_rgb_image_bin = '0'+valeur_rgb_image_bin
                    new_value_bin = valeur_rgb_image_bin[3:] + '0000'
                    tableau_image[i][j][p] = int(new_value_bin,2)
        cacher_image = Image.fromarray(tableau_image)
        cacher_image.save('claire.png')
        return True
if __name__ == '__main__':
    my_steg = Steganographie('static\\images\\fjord-g090d5ce98_1920.jpg')
    my_steg.decode('hide.png')
    
    
