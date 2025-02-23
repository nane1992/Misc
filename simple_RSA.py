import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_valid_e(_phi_n):
    valid_e=[]
    for _e in range(2, _phi_n): # 1 < e < phi_n
        if gcd(_e, _phi_n) == 1: # e must be coprime with phi_n
            valid_e.append(_e)
    return valid_e

def find_decryption_key_d(_e, _phi_n):
    # so that e*d ≡ 1 (mod φ(n))
    _d = 1
    while (_e * _d) % _phi_n !=1:
        _d += 1
    return _d

# RSA setup example
p=443
q=733
n=p*q
phi_n = (p-1)*(q-1)

e = random.choice(find_valid_e(phi_n))

d = find_decryption_key_d(e, phi_n)

# message
M = 181901

# encrypt
C = pow(M,e,n)
print(f"Encrypted message: {C}")

# decrypt
M_decrypted=pow(C,d,n)
print(f"Decrypted message: {M_decrypted}")

