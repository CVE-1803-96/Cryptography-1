class BigIntMath:

    @staticmethod
    def extendedGCD(a: int, b: int) -> tuple:
        r, r_prime = a, b
        u, u_prime = 1, 0
        v, v_prime = 0, 1

        while r_prime != 0:
            q = r // r_prime
            r, u, v, r_prime, u_prime, v_prime = (
                r_prime,
                u_prime,
                v_prime,
                r - q * r_prime,
                u - q * u_prime,
                v - q * v_prime,
            )

        if r < 0:
            r, u, v = -r, -u, -v

        return (r, u, v)

    @staticmethod
    def modInverse(a: int, n: int) -> int:
        if n < 2:
            raise ValueError(f"Le modulus n doit être >= 2, reçu : {n}")

        d, u, _ = BigIntMath.extendedGCD(a % n, n)

        if d != 1:
            raise ValueError(f"Pas d'inverse : gcd({a}, {n}) = {d} != 1")

        return u % n


class AffineCipher:

    def __init__(self, a: int, b: int, n: int = 26):
        self.n = n
        self.b = b % n

        d, _, _ = BigIntMath.extendedGCD(a % n, n)
        if d != 1:
            raise ValueError(
                f"Clé invalide : gcd({a}, {n}) = {d} != 1."
            )

        self.a = a % n
        self.a_inv = BigIntMath.modInverse(self.a, self.n)

    def encrypt(self, m: int) -> int:
        return (self.a * m + self.b) % self.n

    def decrypt(self, c: int) -> int:
        return (self.a_inv * (c - self.b)) % self.n

    def encrypt_text(self, plaintext: str) -> str:
        result = []
        for ch in plaintext.upper():
            if ch.isalpha():
                m = ord(ch) - ord('A')
                c = self.encrypt(m)
                result.append(chr(c + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)

    def decrypt_text(self, ciphertext: str) -> str:
        result = []
        for ch in ciphertext.upper():
            if ch.isalpha():
                c = ord(ch) - ord('A')
                m = self.decrypt(c)
                result.append(chr(m + ord('A')))
            else:
                result.append(ch)
        return ''.join(result)


def test_extended_gcd():
    print("\n== TEST -- Algorithme d'Euclide Étendu ==")
    exemples = [(35, 15), (240, 46), (17, 13), (100, 75)]
    for a, b in exemples:
        d, u, v = BigIntMath.extendedGCD(a, b)
        check = a * u + b * v
        ok = "OK" if check == d else "ERREUR"
        print(f"  a = {a}, b = {b}")
        print(f"  gcd({a}, {b}) = {d}")
        print(f"  u = {u}, v = {v}")
        print(f"  Vérification : {a}*{u} + {b}*({v}) = {check}  {ok}\n")


def test_mod_inverse():
    print("\n== TEST -- Inversion Modulaire ==")
    exemples = [(3, 26), (7, 26), (5, 26), (4, 26)]
    for a, n in exemples:
        try:
            inv = BigIntMath.modInverse(a, n)
            check = (a * inv) % n
            ok = "OK" if check == 1 else "ERREUR"
            print(f"  {a}^(-1) mod {n} = {inv}")
            print(f"  Vérification : {a} x {inv} mod {n} = {check}  {ok}\n")
        except ValueError as e:
            print(f"  modInverse({a}, {n}) -> {e}\n")


def test_affine():
    print("\n== TEST -- Chiffrement Affine ==")

    print("\n  [Entiers] a=5, b=8, n=26")
    cipher_int = AffineCipher(a=5, b=8, n=26)
    all_ok = all(cipher_int.decrypt(cipher_int.encrypt(m)) == m for m in range(26))
    print(f"  D(E(m)) = m pour tout m dans {{0..25}}  {'OK' if all_ok else 'ERREUR'}")

    print("\n  [Texte] a=7, b=3, n=26")
    cipher = AffineCipher(a=7, b=3, n=26)
    msgs = ["HELLO", "CRYPTOGRAPHIE", "UNIVERSITE", "BONJOUR MONDE"]
    for msg in msgs:
        enc = cipher.encrypt_text(msg)
        dec = cipher.decrypt_text(enc)
        lettres_in  = ''.join(c for c in msg.upper() if c.isalpha())
        lettres_out = ''.join(c for c in dec if c.isalpha())
        ok = "OK" if lettres_in == lettres_out else "ERREUR"
        print(f"\n  Original  : {msg}")
        print(f"  Chiffré   : {enc}")
        print(f"  Déchiffré : {dec}  {ok}")

    print("\n  [Clé invalide] a=4, b=3, n=26")
    try:
        AffineCipher(a=4, b=3)
    except ValueError as e:
        print(f"  Exception attendue :\n  {e}  OK")


if __name__ == "__main__":
    test_extended_gcd()
    test_mod_inverse()
    test_affine()
    print("\nTous les tests terminés avec succès.")