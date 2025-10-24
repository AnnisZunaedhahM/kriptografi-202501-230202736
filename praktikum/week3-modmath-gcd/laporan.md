# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [annis zunaedhah muthoharoh]  
NIM: [230202736]  
Kelas: [5 IKRB]  

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

![Hasil Eksekusi](screenshots/hasil_3.JPG)
)

---

## 7. Jawaban Pertanyaan
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
)
---

## 8. Kesimpulan
Aritmetika modular memiliki peran yang sangat krusial dalam kriptografi modern, menjadi dasar bagi berbagai algoritma yang digunakan untuk melindungi data. Dengan menggunakan operasi pada bilangan bulat dalam suatu modulus, aritmetika modular memungkinkan proses enkripsi dan dekripsi pesan dilakukan dengan aman dan efisien.

Invers modular merupakan bagian penting dalam algoritma kunci publik, seperti RSA. Tanpa invers ini, dekripsi pesan tidak mungkin dilakukan, dan perhitungan kunci privat menjadi sulit. Ini menambah lapisan keamanan, karena menemukan invers modular pada bilangan bulat besar sangat sulit, sehingga membuat kunci privat menjadi aman dari upaya pemecahan oleh penyerang.

Namun, tantangan terbesar adalah menyelesaikan logaritma diskrit untuk modulus yang besar. Meskipun ada beberapa algoritma yang bisa digunakan, banyak di antaranya memiliki kompleksitas waktu yang tinggi, sehingga tidak praktis untuk digunakan dalam kriptografi. Kesulitan ini menjadi salah satu alasan mengapa sistem kriptografi tetap aman; jika ditemukan metode yang lebih efisien, bisa berisiko terhadap keamanan enkripsi yang ada saat ini.

Secara keseluruhan, memahami aritmetika modular, invers modular, dan logaritma diskrit sangat penting untuk menerapkan dan memahami keamanan dalam sistem kriptografi. Ketiga konsep ini saling terkait dan bekerja sama untuk menjaga kerahasiaan dan integritas data di dunia digital yang semakin kompleks.

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
Author: annis zunaedhah muthoharoh <email:anniszunaedah@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
