# guerine aya dounia ISI1
def euclide(a, b):
    # initialisation :
    # r = reste courant, u et v sont les coefficients pour a
    r, u, v = a, 1, 0
    
    # r1 = reste suivant, u1 et v1 sont les coefficients pour b
    r1, u1, v1 = b, 0, 1

    # tant que le reste suivant n'est pas nul
    while r1 != 0:
        # q = quotient de la division de r par r1
        q = r // r1
        
        
        # on décale : (r, u, v) devient (r1, u1, v1)
        # et (r1, u1, v1) devient (r - q*r1, u - q*u1, v - q*v1)
        r, u, v, r1, u1, v1 = r1, u1, v1, r - q * r1, u - q * u1, v - q * v1

    # quand r1 = 0, r contient le PGCD, u et v sont les coefficients de Bézout
    return r, u, v  # retourne (pgcd, u, v) tels que a*u + b*v = pgcd



def inverse_modulaire(a, n):
    # on appelle euclide  pour trouver le PGCD et les coefficients
    d, u, _ = euclide(a, n)  # _ signifie qu'on ignore la 3ème valeur (v)
    
    # si le PGCD n'est pas 1, a n'est pas inversible modulo n
    if d != 1:
        raise Exception(f"{a} n'est pas inversible modulo {n}")
    
    # L'inverse modulaire est u modulo n (pour avoir un nombre entre 0 et n-1)
    return u % n



def encryption_aff(mess, a, b, n=26):
    # on met le message en majuscules et on enlève les espaces
    mess = mess.upper().replace(" ", "")
    result = ""
    
    
    for char in mess:
        # lettre -> nombre (A=0, B=1, ...)
        x = ord(char) - ord('A')
        
        # formule de chiffrement affine 
        y = (a * x + b) % n
        
        # nombre -> lettre et ajout au résultat
        result += chr(y + ord('A'))
    
    return result



def decryption_aff(cipher, a, b, n=26):
    # on calcule l'inverse modulaire de a 
    a_inv = inverse_modulaire(a, n)
    result = ""
    
    
    for char in cipher:
        #  lettre-> nombre
        y = ord(char) - ord('A')
        
        # formule de déchiffrement affine 
        x = (a_inv * (y - b)) % n
        
        # nombre-> lettre et ajout au résultat
        result += chr(x + ord('A'))
    
    return result




# exemple
a, b = 30, 18
pgcd, u, v = euclide(a, b)
print(f"pgcd({a}, {b}) = {pgcd}, u = {u}, v = {v}")
print(f"vérification : {a}*{u} + {b}*{v} = {a*u + b*v}\n")


a_mod, n = 7, 26
inv = inverse_modulaire(a_mod, n)
print(f"inverse de {a_mod} mod {n} = {inv}")
print(f"vérification : {a_mod} * {inv} mod {n} = {(a_mod * inv) % n}\n")


mess = "HELLOWORLD"        
a, b = 5, 8                

cipher = encryption_aff(mess, a, b)
print(f"Message original    : {mess}")

plaintxt = decryption_aff(cipher, a, b)
print(f"Message chiffré     : {cipher}")
print(f"Message déchiffré   : {plaintxt}")

# vérification que le déchiffrement redonne le message original
print(f"Réversible ? {mess == plaintxt}")