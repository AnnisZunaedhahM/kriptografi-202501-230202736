# Laporan Praktikum Kriptografi
<<<<<<< HEAD
Minggu ke-: X  
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [annis zunaedhah muthoharoh]  
NIM: [230202736]  
Kelas: [5 IKRB]  
=======
Minggu ke-: 3
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [Annis Zunaedhah M]  
NIM: [230202736]  
Kelas: [ 5IKRB]  
>>>>>>> c90ac6548224b4edfb100b132df7b8a013efed7b

---
## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Menyelesaikan operasi aritmetika modular.
2.Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3.Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

1.Menyelesaikan operasi aritmetika modular.
2.Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3.Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
---
## 2. Dasar Teori
Ringkasan Teori Modular Arithmetic dan GCD
 1. Modular Arithmetic (Aritmetika Modular)
Aritmetika modular** adalah cabang matematika yang mempelajari operasi aritmetika di bawah modulus tertentu. Dalam konteks ini, hasil dari operasi aritmetika dibatasi dalam rentang dari 0 hingga \( m-1 \), di mana \( m \) adalah modulus.
Konsep Dasar
- Modulus: Bilangan bulat positif yang digunakan untuk menentukan batasan. Misalnya, jika \( m = 5 \), maka hasil dari setiap operasi aritmetika akan berada dalam rentang 0 hingga 4.
  
- Notasi: Kita menuliskan \( a \equiv b \mod m \) untuk menunjukkan bahwa \( a \) dan \( b \) memiliki sisa yang sama ketika dibagi oleh \( m \). Contohnya, \( 7 \equiv 2 \mod 5 \) karena sisa dari \( 7 \) dibagi \( 5 \) adalah \( 2 \).

Operasi Dasar

1. Penjumlahan: 
   \[
   (a + b) \mod m
   \]
   Contoh: \( (7 + 4) \mod 5 = 11 \mod 5 = 1 \).

2. Pengurangan: 
   \[
   (a - b) \mod m
   \]
   Contoh: \( (3 - 5) \mod 5 = -2 \mod 5 = 3 \) (karena kita menambahkan \( 5 \)).

3. Perkalian: 
   \[
   (a \times b) \mod m
   \]
   Contoh: \( (3 \times 4) \mod 5 = 12 \mod 5 = 2 \).

4. Eksponen: 
   \[
   (base^{exp}) \mod m
   \]
   Contoh: \( (2^3) \mod 5 = 8 \mod 5 = 3 \). Biasanya dihitung dengan metode eksponensiasi cepat untuk efisiensi.

2. GCD (Greatest Common Divisor)

GCD atau Faktor Persekutuan Terbesar adalah bilangan bulat terbesar yang dapat membagi dua bilangan bulat tanpa meninggalkan sisa. GCD sangat penting dalam berbagai aplikasi, termasuk penyederhanaan pecahan dan algoritma kriptografi.
Konsep Dasar
- Notasi: Ditulis sebagai \( \text{gcd}(a, b) \), di mana \( a \) dan \( b \) adalah dua bilangan bulat.
Algoritma Euclidean
Algoritma ini adalah metode efisien untuk menghitung GCD dari dua bilangan. Prosesnya adalah sebagai berikut:

1. Ambil dua bilangan \( a \) dan \( b \).
2. Hitung sisa \( r \) dari pembagian \( a \) oleh \( b \) (yaitu \( r = a \mod b \)).
3. Ganti \( a \) dengan \( b \) dan \( b \) dengan \( r \).
4. Ulangi langkah 2 dan 3 hingga \( b \) menjadi 0. Pada saat itu, nilai \( a \) adalah GCD.

Contoh:
Untuk menghitung \( \text{gcd}(48, 18) \):
- \( 48 \mod 18 = 12 \)
- Ganti: \( a = 18, b = 12 \)
- \( 18 \mod 12 = 6 \)
- Ganti: \( a = 12, b = 6 \)
- \( 12 \mod 6 = 0 \)
- GCD adalah \( 6 \).
 Aplikasi
- Modular Arithmetic: Banyak digunakan dalam kriptografi, pengkodean, dan algoritma komputer, terutama dalam penghitungan yang efisien.
- GCD: Mempermudah penyederhanaan pecahan, analisis bilangan, dan algoritma yang memerlukan komputasi dengan bilangan bulat.
Kesimpulan
Modular arithmetic dan GCD adalah dua konsep fundamental dalam matematika yang memiliki aplikasi luas dalam teori bilangan dan kriptografi. Memahami kedua konsep ini memungkinkan kita untuk melakukan operasi matematis yang lebih kompleks dan mendesain algoritma yang lebih efisien. Dengan demikian, pengetahuan tentang aritmetika modular dan GCD sangat penting dalam pengembangan aplikasi yang aman dan efektif.

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

![Hasil Eksekusi](screenshots/hasil_3.JPG)
)

---

## 7. Jawaban Pertanyaan
<<<<<<< HEAD
(Jawab pertanyaan diskusi yang diberikan pada modul. 
soal: 
1.Apa peran aritmetika modular dalam kriptografi modern?
2.Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)? 
3.Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
jawab:
1. Peran Aritmetika Modular dalam Kriptografi Modern
Aritmetika modular adalah cabang matematika yang berurusan dengan operasi pada bilangan bulat di bawah modulus tertentu. Dalam konteks kriptografi modern, perannya sangat krusial:

Enkripsi dan Dekripsi: Banyak algoritma kriptografi menggunakan operasi modular untuk mengenkripsi dan mendekripsi pesan. Misalnya, dalam algoritma RSA, pesan diubah menjadi bilangan bulat dan operasi modular digunakan untuk mengenkripsi data dengan kunci publik dan mendekripsinya dengan kunci privat.

Keamanan Kunci: Aritmetika modular menyediakan keamanan yang kuat dengan menggunakan bilangan besar. Pengoperasian bilangan bulat besar dalam modulus yang besar membuatnya sulit untuk memecahkan kunci tanpa informasi yang tepat.

Fungsi Hash: Beberapa fungsi hash kriptografi, yang digunakan untuk memastikan integritas data, juga memanfaatkan aritmetika modular untuk menghasilkan nilai hash yang unik dan aman.

Pengacakan: Dalam protokol komunikasi, aritmetika modular digunakan untuk menghasilkan angka acak yang membantu dalam pengacakan, sehingga sulit bagi penyerang untuk memprediksi kunci atau pesan yang terenkripsi.
2. Pentingnya Invers Modular dalam Algoritma Kunci Publik (misalnya RSA)
Invers modular adalah elemen kunci dalam banyak algoritma kunci publik karena:

Dekripsi: Dalam RSA, pesan yang telah dienkripsi dengan kunci publik dapat didekripsi menggunakan kunci privat yang dihitung berdasarkan invers modular. Tanpa invers ini, proses dekripsi tidak bisa dilakukan.

Penghitungan Kunci Privat: Kunci privat dalam RSA dihitung dari kunci publik dengan menggunakan invers modular dari 𝑒
e (kunci publik) terhadap 𝜙(𝑛)
ϕ(n) (fungsi totien dari modulus 𝑛
n). Ini memastikan bahwa penerima dapat mendekripsi pesan dengan benar.

Keamanan: Keberadaan invers modular yang sulit dicari dalam konteks bilangan bulat besar memberikan tingkat keamanan tinggi. Ini membuat serangan untuk menemukan kunci privat menjadi sangat sulit.
3. Tantangan Utama dalam Menyelesaikan Logaritma Diskrit untuk Modulus Besar
Menyelesaikan logaritma diskrit, yaitu mencari 𝑥
x dari persamaan 
𝑔𝑥≡ℎmod𝑝g x
 ≡hmodp (di mana 𝑔
g adalah basis, ℎ
h adalah hasil, dan 𝑝
p adalah modulus), memiliki beberapa tantangan utama:

Kompleksitas Waktu: Algoritma yang ada untuk menyelesaikan logaritma diskrit, seperti algoritma Baby-step Giant-step atau Pollard's rho, memiliki waktu komputasi yang tinggi, terutama untuk bilangan yang besar. Ini membuatnya tidak praktis untuk digunakan dalam kriptografi.

Keterbatasan Algoritma: Meskipun ada beberapa metode, tidak ada algoritma yang sepenuhnya efisien untuk semua kasus logaritma diskrit. Hal ini menciptakan tantangan dalam menemukan solusi dengan cepat, terutama ketika modulus sangat besar.

Keamanan Sistem Kriptografi: Kesulitan dalam menyelesaikan logaritma diskrit menjadi dasar keamanan banyak sistem kriptografi, seperti Diffie-Hellman dan ElGamal. Jika metode baru yang lebih efisien ditemukan, keamanan sistem ini dapat terancam.
=======
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

\
>>>>>>> c90ac6548224b4edfb100b132df7b8a013efed7b
)
---

## 8. Kesimpulan
<<<<<<< HEAD
Aritmetika modular memiliki peran yang sangat krusial dalam kriptografi modern, menjadi dasar bagi berbagai algoritma yang digunakan untuk melindungi data. Dengan menggunakan operasi pada bilangan bulat dalam suatu modulus, aritmetika modular memungkinkan proses enkripsi dan dekripsi pesan dilakukan dengan aman dan efisien.

Invers modular merupakan bagian penting dalam algoritma kunci publik, seperti RSA. Tanpa invers ini, dekripsi pesan tidak mungkin dilakukan, dan perhitungan kunci privat menjadi sulit. Ini menambah lapisan keamanan, karena menemukan invers modular pada bilangan bulat besar sangat sulit, sehingga membuat kunci privat menjadi aman dari upaya pemecahan oleh penyerang.

Namun, tantangan terbesar adalah menyelesaikan logaritma diskrit untuk modulus yang besar. Meskipun ada beberapa algoritma yang bisa digunakan, banyak di antaranya memiliki kompleksitas waktu yang tinggi, sehingga tidak praktis untuk digunakan dalam kriptografi. Kesulitan ini menjadi salah satu alasan mengapa sistem kriptografi tetap aman; jika ditemukan metode yang lebih efisien, bisa berisiko terhadap keamanan enkripsi yang ada saat ini.

Secara keseluruhan, memahami aritmetika modular, invers modular, dan logaritma diskrit sangat penting untuk menerapkan dan memahami keamanan dalam sistem kriptografi. Ketiga konsep ini saling terkait dan bekerja sama untuk menjaga kerahasiaan dan integritas data di dunia digital yang semakin kompleks.
=======
Program Python yang disusun memberikan fondasi yang kuat dalam memahami dan menerapkan konsep-konsep penting dalam aritmetika modular dan teori bilangan. Berikut adalah ringkasan detail dari setiap komponen yang diimplementasikan:
>>>>>>> c90ac6548224b4edfb100b132df7b8a013efed7b

1. Aritmetika Modular:
   - Fungsi Penjumlahan (`mod_add`): Menghitung hasil penjumlahan dua bilangan dalam ruang modulo, berguna untuk menghindari overflow dan menjaga hasil dalam batas tertentu.
   - Fungsi Pengurangan (`mod_sub`): Memungkinkan pengurangan dengan modulus, penting dalam berbagai algoritma yang melibatkan siklus atau pengulangan.
   - Fungsi Perkalian (`mod_mul`): Mengalikan dua bilangan dan mengambil modulus, digunakan dalam kriptografi untuk operasi yang melibatkan kunci.
   - Fungsi Eksponen Modular (`mod_exp`): Menghitung pangkat dengan modulus secara efisien menggunakan metode eksponensiasi cepat, mengurangi kompleksitas waktu dalam perhitungan besar.

2. GCD (Greatest Common Divisor):
   - Fungsi GCD (`gcd`): Menghitung GCD dari dua bilangan menggunakan algoritma Euclidean, yang sangat efisien dan dasar untuk banyak aplikasi di teori bilangan, termasuk dalam penyederhanaan pecahan.

3. Extended Euclidean & Invers Modular:
   - ungsi Extended GCD (`extended_gcd`)**: Menghitung GCD dan koefisien \( x \) dan \( y \) yang memenuhi persamaan \( ax + by = \text{GCD}(a, b) \). Ini berguna untuk menyelesaikan masalah di mana kombinasi linear diperlukan.
   - Fungsi Invers Modular (`mod_inverse`)**: Mengembalikan invers dari bilangan \( a \) modulo \( m \) jika \( a \) dan \( m \) relatif prima. Invers modular sangat penting dalam algoritma kriptografi untuk dekripsi kunci.

4. Bilangan Prima:
   - Fungsi Bilangan Prima (`is_prime`)**: Menentukan apakah suatu bilangan adalah prima. Bilangan prima merupakan elemen kunci dalam banyak algoritma kriptografi, termasuk dalam pembangkitan kunci.

5. Logaritma Diskrit:
   - Fungsi Logaritma Diskrit (`discrete_log`)**: Mencari nilai \( x \) yang memenuhi \( g^x \equiv y \mod p \). Ini adalah masalah yang sulit dan menjadi dasar bagi banyak protokol kriptografi, seperti Diffie-Hellman, yang memanfaatkan kesulitan menghitung logaritma diskrit untuk keamanan.

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
<<<<<<< HEAD
Author: annis zunaedhah muthoharoh <email:anniszunaedah@gmail.com>
=======
Author: Annis Zunaedhah M <email:anniszunaedah@gmail.com>
>>>>>>> c90ac6548224b4edfb100b132df7b8a013efed7b
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
