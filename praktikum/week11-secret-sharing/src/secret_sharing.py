import random

# =========================
# Shamir Secret Sharing
# =========================

PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def eval_polynomial(coeffs, x, prime):
    result = 0
    for power, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, power, prime)) % prime
    return result

def split_secret(secret, k, n):
    secret_int = int.from_bytes(secret.encode(), 'big')
    coeffs = [secret_int] + [random.randrange(1, PRIME) for _ in range(k - 1)]
    shares = [(x, eval_polynomial(coeffs, x, PRIME)) for x in range(1, n + 1)]
    return shares

def recover_secret(shares):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        num, den = 1, 1
        for i, (xi, _) in enumerate(shares):
            if i != j:
                num = (num * (-xi)) % PRIME
                den = (den * (xj - xi)) % PRIME
        secret = (secret + yj * num * pow(den, -1, PRIME)) % PRIME
    return secret

def int_to_string(secret_int):
    length = (secret_int.bit_length() + 7) // 8
    return secret_int.to_bytes(length, 'big').decode()

# =========================
# MAIN
# =========================

secret = "KriptografiUPB2025"

shares = split_secret(secret, k=3, n=5)
print("Shares:")
for s in shares:
    print(s)

recovered_int = recover_secret(shares[:3])
recovered_secret = int_to_string(recovered_int)

print("\nRecovered secret:", recovered_secret)