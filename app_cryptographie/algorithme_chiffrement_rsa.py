#-*- coding:utf-8 -*-

class RSA:
    def chiffrement(self, n, e, text):
        asc = [str(ord(j)) for j in text]
        for i, k in enumerate(asc):
            if len(k) < 3:		
                while len(k) < 3:
                    k = '0' + k
                asc[i] = k       
        ascg = ''.join(asc)
        d , f = 0 , 4
        while len(ascg)%f != 0: 
            ascg = ascg + '0'
        l = []
        while f <= len(ascg):
            l.append(ascg[d:f])
            d , f = f , f + 4
        crypt = [str(((int(i))**e)%n) for i in l]
        texte_crypt = ''
        for i in range(len(crypt)):
            for j in range(len(crypt[i])):
                texte_crypt += chr(int(crypt[i][j]))
            texte_crypt += '/Reptemp°'
        
        return texte_crypt
	
    def dechiffrement(self, n, d, texte_crypt):

        texte_crypt = texte_crypt.split('/Reptemp°')[:-1]
        crypt = []
        for i in range(len(texte_crypt)):
            elements = ''
            for j in range(len(texte_crypt[i])):
                elements += str(ord(texte_crypt[i][j]))
            crypt.append(elements)    
        resultat = [str((int(i)**d)%n) for i in crypt]
        for i, s in enumerate(resultat):
            if len(s) < 4:
                while len(s) < 4:
                    s = '0' + s
                resultat[i] = s
        g = ''.join(resultat)
        asci = ''
        d , f = 0 , 3
        while f < len(g):
            asci = asci + chr(int(g[d:f]))
            d , f = f , f + 3
        
        return asci

if __name__ == '__main__':
    my_rsa = RSA()
    print(my_rsa.chiffrement(122669, 32909, 'Anrezki1 z4789*/+'))
    print(my_rsa.dechiffrement(122669, 389, my_rsa.chiffrement(122669, 32909, 'Anrezki74586921 z14789*/+')))