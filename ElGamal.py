#El Gamal
import sympy
# import primefac
import random

def gen_p():
    """ generiert eine 200-stellige Primzahl p
    und einen passenden 60-stelligen Generator g"""
    p = sympy.randprime(10**199, 10**200-1) # 200-stelligen Primzahl
    factors = sympy.factorint(p - 1) # zerlegt p-1 in Primfaktoren (vllt. schneller: primefac.primefac) 
    while True:
        g = random.randint(10**59, 10**60-1) # 60-stellige Zahl als Kandidat
        # Bedingung: g^((p-1)/q) darf nicht 1 sein für alle Primfaktoren q von (p-1)
        if all(pow(g, (p-1) // q, p) != 1 for q in factors):
            return (p, g)

def choose_b():
    """ wählt eine zufällige 4-stellige Zahl b (privat) """
    b = random.randint(1000,9999)
    return b

def elgamal_keys():
    """erzeugt Schlüssel:(g, p, b, beta) """
    p, g = gen_p() # Primzahl und Generator
    b = choose_b() # geheimer Schlüssel
    beta = pow(g, b, p) # öffentlicher Schlüssel g^b mod p
    return (g,p,b,beta)

# Schlüssel generieren
keys = elgamal_keys()
# print("ElGamal Schlüssel: ", keys)

def digitize(s):
    """ wandelt string in ASCII-Werte um """
    m = int(''.join(f"{ord(char):03}" for char in s)) # führenden Nullen bleiben
    return m 

plain = input("Secret message: ")
m = digitize(plain)
print(m)

def elgamal_encr(p, g, beta, plain):
    """verschlüsselt Nachricht mit ElGamal """
    m = digitize(plain) # string zur Zahl
    k = random.randint(1, p-2)
    
    rA = pow(g, k, p)
    
    tA = (pow(beta, k, p) * m) % p
    
    return (rA, tA)

rA, tA = elgamal_encr(keys[1], keys[0], keys[3], plain)

print(f"Kryptertes Paar (rA, tA): {rA}, {tA}")