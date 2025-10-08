# Laporan Praktikum Kriptografi
Minggu ke-: 01
Topik: [ praktikum Kriptografi]  
Nama: annis zunaedhah muthoharoh
NIM:  230202736 
Kelas: [5IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2.Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3.Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4.Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )
Ringkasan
Cipher Klasik
Cipher klasik adalah metode enkripsi yang menyembunyikan pesan dengan mengganti atau mengacak huruf dalam teks asli. Contoh yang terkenal adalah Caesar cipher, di mana setiap huruf digeser sejumlah posisi dalam alfabet. Meskipun mudah digunakan, cipher klasik rentan terhadap analisis pola.
Modular Aritmetika
Modular aritmetika adalah sistem aritmetika yang bekerja dengan angka dalam siklus tertentu, dikenal sebagai modulus. Dalam kriptografi, ini digunakan untuk perhitungan dengan angka besar, seperti dalam algoritma RSA, yang menghasilkan kunci publik dan privat. Konsep ini meningkatkan efisiensi dalam enkripsi.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain
- Chrome
- Git dan akun GitHub  
- Terminal

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
 1. Siapa Tokoh yang Dianggap sebagai Bapak Kriptografi Modern?
Tokoh yang dianggap sebagai bapak kriptografi modern adalah Whitfield Diffie. Bersama dengan Martin Hellman, Diffie mengembangkan konsep kriptografi kunci publik pada tahun 1976. Inovasi ini memungkinkan dua pihak untuk berkomunikasi secara aman tanpa perlu bertukar kunci rahasia sebelumnya, menggantikan metode kriptografi simetris yang sebelumnya dominan.

2. Sebutkan Algoritma Kunci Publik yang Populer Digunakan Saat Ini
Beberapa algoritma kunci publik yang populer dan banyak digunakan saat ini antara lain:

RSA (Rivest-Shamir-Adleman): Salah satu algoritma paling awal dan paling umum untuk enkripsi dan tanda tangan digital. RSA menggunakan dua kunci, yaitu kunci publik untuk enkripsi dan kunci privat untuk dekripsi.

DSA (Digital Signature Algorithm): Digunakan khusus untuk tanda tangan digital. DSA juga menggunakan kunci publik dan privat, tetapi metode matematikanya berbeda dari RSA.

ECC (Elliptic Curve Cryptography): Menggunakan struktur matematika dari kurva eliptik untuk memberikan keamanan yang lebih tinggi dengan ukuran kunci yang lebih kecil dibandingkan RSA atau DSA.

ElGamal: Digunakan untuk enkripsi dan tanda tangan digital, algoritma ini juga berbasis pada masalah logaritma diskrit.

3. Apa Perbedaan Utama antara Kriptografi Klasik dan Kriptografi Modern?
Perbedaan utama antara kriptografi klasik dan kriptografi modern dapat dijelaskan sebagai berikut:

Pendekatan Kunci:

Kriptografi Klasik: Mengandalkan metode simetris, di mana kunci yang sama digunakan untuk enkripsi dan dekripsi. Contohnya termasuk metode Caesar dan Vigenère. Masalah utama adalah pengiriman kunci yang aman.
Kriptografi Modern: Menggunakan metode asimetris (kunci publik dan kunci privat). Ini memungkinkan pertukaran kunci yang aman tanpa memerlukan saluran komunikasi yang aman.
Keamanan:

Kriptografi Klasik: Keamanan bergantung pada kerumitan algoritma dan panjang kunci. Banyak metode klasik telah dipecahkan dengan kemajuan dalam analisis matematika dan komputasi.
Kriptografi Modern: Mengandalkan prinsip matematika yang lebih kompleks seperti teori bilangan dan masalah matematis yang sulit, sehingga lebih sulit untuk dipecahkan bahkan dengan teknologi komputer yang canggih.
Penggunaan:

Kriptografi Klasik: Terutama digunakan dalam situasi di mana komunikasi aman dapat dilakukan, seperti surat-menyurat rahasia.
Kriptografi Modern: Digunakan dalam berbagai aplikasi, termasuk transaksi keuangan online, komunikasi aman di internet, dan sistem identifikasi digital.
)
---

## 8. Kesimpulan
Kriptografi telah mengalami perkembangan yang signifikan dari metode klasik hingga modern. Tokoh penting seperti Whitfield Diffie telah memainkan peran krusial dalam memperkenalkan konsep kriptografi kunci publik, yang memungkinkan komunikasi aman tanpa perlu bertukar kunci rahasia. Algoritma seperti RSA, DSA, ECC, dan ElGamal telah menjadi standar dalam keamanan digital saat ini.

Perbedaan utama antara kriptografi klasik dan modern terletak pada pendekatan kunci, tingkat keamanan, dan aplikasi penggunaannya. Kriptografi klasik, dengan metode simetriknya, lebih rentan terhadap serangan, sementara kriptografi modern menawarkan solusi yang lebih aman dan efisien dengan penggunaan kunci publik dan privat. Dengan demikian, pemahaman mengenai kedua jenis kriptografi ini sangat penting untuk melindungi informasi dalam era digital yang semakin kompleks.
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
Author: annis zunaedhah muthoharoh <anniszunaedah@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
