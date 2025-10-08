# Laporan Praktikum Kriptografi
Minggu ke-: 02
Topik: [Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)]  
Nama: [annis zunaedhah muthoharoh ]  
NIM: [230202736]  
Kelas: [5 IKRB ]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2.Menggambarkan proses enkripsi dan dekripsi sederhana.
3.Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Ringkasan


Cryptosystem adalah sistem yang digunakan untuk mengamankan informasi melalui proses enkripsi dan dekripsi. Secara umum, cryptosystem terdiri dari beberapa komponen utama yang bekerja sama untuk memastikan bahwa data tetap aman dari pihak yang tidak berwenang.
Komponen Utama
Plaintext: Data asli yang ingin dilindungi.
Ciphertext: Data yang telah dienkripsi dan tidak dapat dibaca tanpa kunci.
Kunci: Informasi rahasia untuk enkripsi dan dekripsi, bisa simetris (sama) atau asimetris (berbeda).
Algoritma: Metode matematis untuk mengubah plaintext menjadi ciphertext dan sebaliknya.
Proses
Enkripsi: Mengubah plaintext menjadi ciphertext untuk menjaga kerahasiaan.
Dekripsi: Mengubah ciphertext kembali menjadi plaintext menggunakan kunci yang tepat.
Jenis Kriptografi
Simetris: Menggunakan kunci yang sama untuk enkripsi dan dekripsi (contoh: AES). Proses cepat, tetapi sulit dalam distribusi kunci.
Asimetris: Menggunakan dua kunci berbeda; kunci publik untuk enkripsi dan kunci privat untuk dekripsi (contoh: RSA). Memudahkan distribusi, tetapi lebih lambat.

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

## 7. Jawaban Pertanyaan Diskusi
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
