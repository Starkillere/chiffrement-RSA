"""
    choisir deux grand nombre premiers ordre 10^4 min  p et q
    calculer n = p * q
    calculer phi(n) = (p-1)*(q-1)
    choisir un exposant e telque pgcd(e, phi(n)) = 1
    colculer l'inverse d de e mod(phi(n)) par l'agorithme d'eucle 
    key de chiffrement = n et e
    key de déchiffrement  = d
"""
import random

csprng = random.SystemRandom()

def pgcde(a:int, b:int):
	r, u, v = a, 1, 0
	rp, up, vp = b, 0, 1
	
	while rp != 0:
		q = r//rp
		rs, us, vs = r, u, v
		r, u, v = rp, up, vp
		rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
	
	return (r, u, v)

def random_prime(min=100, max=1000) -> int:
    prime_list = []
    for n in range(min, max):
        isPrime = True
        for num in range(2, n):
            if n % num == 0:
                isPrime = False     
        if isPrime:
            prime_list.append(n)
    nb_random_prime = csprng.choice(prime_list)
    return nb_random_prime

def random_number(min=0, max=1000) -> int:
    return csprng.randint(min, max)

def generate_keys() -> dict:
    p,q = random_prime(), random_prime()
    n = p*q
    phi = (p-1) * (q-1)
    r = 10
    d = 0
    while r != 1 or d <= 2 or d >= phi:
        e = random_number()
        r, d, v = pgcde(e, phi)
    return {'key publique':(int(n), int(e)), 'key priver':(int(n),int(d))}

if __name__ == '__main__':
    my_keys = generate_keys()
    my_number = 47
    n = my_keys['key publique'][0]
    d = my_keys['key publique'][1]
    e = my_keys['key priver'][1]
    chiffre = my_number**d % n
    dechifre =  chiffre**e % n
    print(dechifre == my_number)