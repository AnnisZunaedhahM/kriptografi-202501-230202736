import hashlib

# =========================
# Simulasi Hash MD5 Lemah
# =========================
password_asli = "admin123"
hash_md5 = hashlib.md5(password_asli.encode()).hexdigest()

print("Hash MD5 target:", hash_md5)

# =========================
# Dictionary Attack
# =========================
dictionary = [
    "123456",
    "password",
    "admin",
    "admin123",
    "qwerty",
    "letmein"
]

found = False

for word in dictionary:
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    print(f"Mencoba: {word} -> {hashed_word}")

    if hashed_word == hash_md5:
        print("\n❌ PASSWORD BERHASIL DITEMUKAN!")
        print("Password:", word)
        found = True
        break

if not found:
    print("\nPassword tidak ditemukan.")
