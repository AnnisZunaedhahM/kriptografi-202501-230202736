# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [Annis Zunaedhah M]  
NIM: [230202736]  
Kelas: [ 5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Menyelesaikan operasi aritmetika modular.
2.Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3.Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )
# src/modular_math.py

def mod_add(a, b, m):
    """Menjumlahkan dua bilangan dalam aritmetika modular."""
    return (a + b) % m

def mod_sub(a, b, m):
    """Mengurangi dua bilangan dalam aritmetika modular."""
    return (a - b) % m

def mod_mul(a, b, m):
    """Mengalikan dua bilangan dalam aritmetika modular."""
    return (a * b) % m

def mod_exp(base, exp, mod):
    """Menghitung eksponen dalam aritmetika modular."""
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # Jika exp adalah ganjil
            result = (result * base) % mod
        exp = exp >> 1  # Bagi exp dengan 2
        base = (base * base) % mod
    return result

def gcd(a, b):
    """Menghitung GCD menggunakan algoritma Euclidean."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Menghitung GCD dan koefisien x dan y."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Menghitung invers modular dari a mod m."""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Invers tidak ada")
    else:
        return x % m

def is_prime(n):
    """Menentukan apakah n adalah bilangan prima."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def discrete_log(g, y, p):
    """Mencari x di mana g^x ≡ y (mod p)."""
    current = 1
    for x in range(p - 1):
        if current == y:
            return x
        current = (current * g) % p
    return None  # Jika tidak ditemukan
Berikut adalah kode Python lengkap yang mencakup semua fungsi yang Anda butuhkan untuk aritmetika modular, GCD, invers modular, dan logaritma diskrit, lengkap dengan contoh penggunaannya.

```python
# src/modular_math.py

def mod_add(a, b, m):
    """Menjumlahkan dua bilangan dalam aritmetika modular."""
    return (a + b) % m

def mod_sub(a, b, m):
    """Mengurangi dua bilangan dalam aritmetika modular."""
    return (a - b) % m

def mod_mul(a, b, m):
    """Mengalikan dua bilangan dalam aritmetika modular."""
    return (a * b) % m

def mod_exp(base, exp, mod):
    """Menghitung eksponen dalam aritmetika modular."""
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:  # Jika exp adalah ganjil
            result = (result * base) % mod
        exp = exp >> 1  # Bagi exp dengan 2
        base = (base * base) % mod
    return result

def gcd(a, b):
    """Menghitung GCD menggunakan algoritma Euclidean."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Menghitung GCD dan koefisien x dan y."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Menghitung invers modular dari a mod m."""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Invers tidak ada")
    else:
        return x % m

def is_prime(n):
    """Menentukan apakah n adalah bilangan prima."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def discrete_log(g, y, p):
    """Mencari x di mana g^x ≡ y (mod p)."""
    current = 1
    for x in range(p - 1):
        if current == y:
            return x
        current = (current * g) % p
    return None  # Jika tidak ditemukan

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh Modular Arithmetic
    print("Modular Addition: ", mod_add(17, 5, 12))  # Output: 10
    print("Modular Subtraction: ", mod_sub(17, 5, 12))  # Output: 12
    print("Modular Multiplication: ", mod_mul(4, 3, 5))  # Output: 2
    print("Modular Exponentiation: ", mod_exp(3, 4, 11))  # Output: 9

    # Contoh GCD
    print("GCD of 48 and 18: ", gcd(48, 18))  # Output: 6

    # Contoh Modular Inverse
    print("Modular Inverse of 3 mod 11: ", mod_inverse(3, 11))  # Output: 4

    # Contoh Bilangan Prima
    print("Apakah 29 bilangan prima? ", is_prime(29))  # Output: True
    print("Apakah 30 bilangan prima? ", is_prime(30))  # Output: False

    # Contoh Discrete Log
    print("Discrete Log of 3^x ≡ 4 mod 11: ", discrete_log(3, 4, 11))  # Output: 4
```

### Penjelasan Kode

1. **Fungsi Aritmetika Modular**:
   - `mod_add`: Menjumlahkan dua bilangan dan mengambil modulus.
   - `mod_sub`: Mengurangi dua bilangan dan mengambil modulus.
   - `mod_mul`: Mengalikan dua bilangan dan mengambil modulus.
   - `mod_exp`: Menghitung hasil pangkat dengan modulus menggunakan metode eksponensiasi cepat.

2. **GCD dan Extended Euclidean**:
   - `gcd`: Menghitung GCD dari dua bilangan menggunakan algoritma Euclidean.
   - `extended_gcd`: Mengembalikan GCD dan koefisien yang membentuk GCD sebagai kombinasi linear dari dua bilangan.

3. **Invers Modular**:
   - `mod_inverse`: Menghitung invers modular dari bilangan \( a \) modulo \( m \) menggunakan algoritma extended Euclidean.

4. **Bilangan Prima**:
   - `is_prime`: Memeriksa apakah bilangan \( n \) adalah bilangan prima.

5. **Logaritma Diskrit**:
   - `discrete_log`: Menghitung nilai \( x \) yang memenuhi \( g^x \equiv y \mod p \) dengan iterasi.

### Contoh Penggunaan
Bagian `if __name__ == "__main__":` menunjukkan contoh penggunaan untuk setiap fungsi. Anda dapat langsung menjalankan kode ini dalam lingkungan Python untuk melihat hasilnya.

Jika ada pertanyaan lebih lanjut atau butuh bantuan, silakan beri tahu!
# Contoh penggunaan
if __name__ == "__main__":
    # Contoh Modular Arithmetic
    print("Modular Addition: ", mod_add(17, 5, 12))  # Output: 10
    print("Modular Subtraction: ", mod_sub(17, 5, 12))  # Output: 12
    print("Modular Multiplication: ", mod_mul(4, 3, 5))  # Output: 2
    print("Modular Exponentiation: ", mod_exp(3, 4, 11))  # Output: 9

    # Contoh GCD
    print("GCD of 48 and 18: ", gcd(48, 18))  # Output: 6

    # Contoh Modular Inverse
    print("Modular Inverse of 3 mod 11: ", mod_inverse(3, 11))  # Output: 4

    # Contoh Bilangan Prima
    print("Apakah 29 bilangan prima? ", is_prime(29))  # Output: True
    print("Apakah 30 bilangan prima? ", is_prime(30))  # Output: False

    # Contoh Discrete Log
    print("Discrete Log of 3^x ≡ 4 mod 11: ", discrete_log(3, 4, 11))  # Output: 4
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
1.Menyelesaikan operasi aritmetika modular.
2.Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3.Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
jawab
Berikut adalah penjelasan terperinci mengenai masing-masing topik yang Anda sebutkan:

1. Menyelesaikan Operasi Aritmetika Modular?

Aritmetika modular adalah sistem aritmatika yang berhubungan dengan sisa dari pembagian. Notasi yang umum digunakan adalah:

\[ a \equiv b \mod m \]

yang berarti bahwa \( a \) dan \( b \) memiliki sisa yang sama ketika dibagi oleh \( m \).

 Contoh:

Misalkan kita ingin menghitung \( 17 + 5 \mod 12 \).

1. Hitung \( 17 + 5 = 22 \).
2. Hitung sisa pembagian \( 22 \div 12 \), yang memberikan sisa 10.

Jadi, \( 17 + 5 \equiv 10 \mod 12 \).

Operasi Dasar:

- **Penjumlahan: \( (a + b) \mod m \)
- **Pengurangan: \( (a - b) \mod m \)
- **Perkalian: \( (a \times b) \mod m \)
- **Pangkat: \( (a^b) \mod m \)

2. Menentukan Bilangan Prima dan Menghitung GCD?

 Bilangan Prima

Bilangan prima adalah bilangan bulat lebih besar dari 1 yang hanya memiliki dua faktor, yaitu 1 dan dirinya sendiri. Contoh bilangan prima: 2, 3, 5, 7, 11, 13, dll.

 Metode Menentukan Bilangan Prima:

1. Pembagian: Cek apakah bilangan tersebut dapat dibagi oleh bilangan prima lebih kecil dari akar kuadrat bilangan tersebut.
2. Sieve of Eratosthenes: Algoritma yang efisien untuk menemukan semua bilangan prima hingga angka tertentu.

Menghitung GCD

GCD (Greatest Common Divisor) adalah bilangan bulat terbesar yang dapat membagi dua bilangan tanpa sisa. Metode yang umum digunakan adalah Algoritma Euclidean.

 Contoh Menghitung GCD:

Misalkan kita ingin menghitung GCD dari 48 dan 18.

1. Bagi 48 dengan 18, sisa adalah 12 (48 = 18 * 2 + 12).
2. Bagi 18 dengan 12, sisa adalah 6 (18 = 12 * 1 + 6).
3. Bagi 12 dengan 6, sisa adalah 0 (12 = 6 * 2 + 0).

Karena sisa menjadi 0, GCD adalah 6.
 3. Menerapkan Logaritma Diskrit Sederhana dalam Simulasi Kriptografi

Logaritma diskrit adalah konsep yang digunakan dalam kriptografi untuk keamanan data. Dalam konteks ini, kita biasanya berbicara tentang masalah logaritma diskrit dalam kelompok bilangan modulo.

 Notasi:

Misalkan kita memiliki bilangan bulat \( g \) (basis) dan \( y \) (hasil), kita ingin menemukan \( x \) sehingga:

\[ g^x \equiv y \mod p \]

Contoh:

Misalkan \( g = 3 \), \( y = 4 \), dan \( p = 11 \). Kita ingin menemukan \( x \) sehingga:

\[ 3^x \equiv 4 \mod 11 \]

Coba nilai \( x \):

- \( x = 1 \): \( 3^1 = 3 \)
- \( x = 2 \): \( 3^2 = 9 \)
- \( x = 3 \): \( 3^3 = 27 \equiv 5 \mod 11 \)
- \( x = 4 \): \( 3^4 = 81 \equiv 4 \mod 11 \)

Jadi, \( x = 4 \) adalah solusi dari logaritma diskrit ini.
 Penerapan dalam Kriptografi:

Logaritma diskrit digunakan dalam protokol seperti Diffie-Hellman untuk pertukaran kunci, di mana keamanan bergantung pada kesulitan menghitung logaritma diskrit.

Dengan penjelasan di atas, Anda seharusnya dapat memahami dasar-dasar operasi aritmetika modular, bilangan prima dan GCD, serta penerapan logaritma diskrit dalam kriptografi. Jika ada yang ingin ditanyakan lebih lanjut, silakan!
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )
## Kesimpulan

Program Python yang disusun memberikan fondasi yang kuat dalam memahami dan menerapkan konsep-konsep penting dalam aritmetika modular dan teori bilangan. Berikut adalah ringkasan detail dari setiap komponen yang diimplementasikan:

1. **Aritmetika Modular**:
   - **Fungsi Penjumlahan (`mod_add`)**: Menghitung hasil penjumlahan dua bilangan dalam ruang modulo, berguna untuk menghindari overflow dan menjaga hasil dalam batas tertentu.
   - **Fungsi Pengurangan (`mod_sub`)**: Memungkinkan pengurangan dengan modulus, penting dalam berbagai algoritma yang melibatkan siklus atau pengulangan.
   - **Fungsi Perkalian (`mod_mul`)**: Mengalikan dua bilangan dan mengambil modulus, digunakan dalam kriptografi untuk operasi yang melibatkan kunci.
   - **Fungsi Eksponen Modular (`mod_exp`)**: Menghitung pangkat dengan modulus secara efisien menggunakan metode eksponensiasi cepat, mengurangi kompleksitas waktu dalam perhitungan besar.

2. **GCD (Greatest Common Divisor)**:
   - **Fungsi GCD (`gcd`)**: Menghitung GCD dari dua bilangan menggunakan algoritma Euclidean, yang sangat efisien dan dasar untuk banyak aplikasi di teori bilangan, termasuk dalam penyederhanaan pecahan.

3. **Extended Euclidean & Invers Modular**:
   - **Fungsi Extended GCD (`extended_gcd`)**: Menghitung GCD dan koefisien \( x \) dan \( y \) yang memenuhi persamaan \( ax + by = \text{GCD}(a, b) \). Ini berguna untuk menyelesaikan masalah di mana kombinasi linear diperlukan.
   - **Fungsi Invers Modular (`mod_inverse`)**: Mengembalikan invers dari bilangan \( a \) modulo \( m \) jika \( a \) dan \( m \) relatif prima. Invers modular sangat penting dalam algoritma kriptografi untuk dekripsi kunci.

4. **Bilangan Prima**:
   - **Fungsi Bilangan Prima (`is_prime`)**: Menentukan apakah suatu bilangan adalah prima. Bilangan prima merupakan elemen kunci dalam banyak algoritma kriptografi, termasuk dalam pembangkitan kunci.

5. **Logaritma Diskrit**:
   - **Fungsi Logaritma Diskrit (`discrete_log`)**: Mencari nilai \( x \) yang memenuhi \( g^x \equiv y \mod p \). Ini adalah masalah yang sulit dan menjadi dasar bagi banyak protokol kriptografi, seperti Diffie-Hellman, yang memanfaatkan kesulitan menghitung logaritma diskrit untuk keamanan.

### Implikasi dan Aplikasi
Implementasi fungsi-fungsi ini tidak hanya menunjukkan dasar-dasar matematika, tetapi juga bagaimana konsep-konsep ini diterapkan dalam kriptografi modern. Dengan memahami dan menggunakan fungsi ini, pengguna dapat:
- Mengembangkan algoritma kr
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
