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
- Chrome
- Git dan akun GitHub  
  Terminal

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


# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "Cryptosystem Test"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
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
(Jawab pertanyaan diskusi yang diberikan pada modul.)  

1. Komponen Utama dalam Sebuah Kriptosistem
Kriptosistem adalah sistem yang digunakan untuk mengamankan data melalui proses enkripsi (mengubah data asli menjadi bentuk yang tidak bisa dibaca) dan dekripsi (mengembalikan data ke bentuk asli). Komponen utama dalam sebuah kriptosistem meliputi:
Plaintext: Data asli yang ingin diamankan.
Ciphertext: Data hasil enkripsi yang tidak bisa dibaca.
Kunci: Rahasia untuk enkripsi dan dekripsi.
Algoritma Enkripsi/Dekripsi: Aturan untuk mengubah data.
Pengguna: Pengirim dan penerima pesan.

3. Kelebihan dan Kelemahan Sistem Simetris Dibandingkan Asimetris
Kriptografi Simetris
Dalam kriptografi simetris, satu kunci digunakan untuk enkripsi dan dekripsi. Contoh algoritma simetris adalah AES (Advanced Encryption Standard) dan DES (Data Encryption Standard).
Simetris (1 kunci untuk enkripsi & dekripsi, contoh: AES):

  Kelebihan: Cepat, efisien untuk data besar, hemat sumber daya.
  Kelemahan: Sulit mendistribusikan kunci, tidak cocok untuk banyak pengguna, risiko keamanan kunci.

Asimetris (kunci publik & privat, contoh: RSA):
  Kelebihan: Distribusi kunci aman, cocok untuk komunikasi terbuka, mendukung tanda tangan digital.
  Kelemahan: Lambat, kurang efisien untuk data besar, kompleks.
  
3. Mengapa Distribusi Kunci Jadi Masalah di Kriptografi Simetris
Kunci harus dibagikan secara aman kepada penerima. Jika kunci bocor atau dikirim lewat saluran tidak aman, pihak ketiga bisa mendekripsi pesan. Selain itu, untuk banyak pengguna, jumlah kunci yang dibutuhkan jadi sangat banyak, menyulitkan manajemen


)
---

## 8. Kesimpulan

Kriptosistem merupakan metode untuk mengamankan data melalui proses enkripsi dan dekripsi, dengan komponen utama meliputi plaintext (data asli), ciphertext (data terenkripsi), kunci (rahasia untuk mengenkripsi/mendekripsi), algoritma enkripsi/dekripsi (aturan pengubahan data), serta pengguna (pengirim dan penerima pesan). Kriptografi simetris, seperti AES, menawarkan kecepatan dan efisiensi untuk data besar, tetapi distribusi kunci menjadi masalah utama karena kunci harus dibagikan secara aman untuk mencegah kebocoran, dan manajemen kunci sulit untuk banyak pengguna. Sebaliknya, kriptografi asimetris, seperti RSA, memudahkan distribusi kunci dengan menggunakan kunci publik dan privat, sehingga cocok untuk komunikasi terbuka, namun lebih lambat dan kurang efisien untuk data besar. Dengan demikian, pilihan antara simetris dan asimetris bergantung pada kebutuhan kecepatan, skala, dan keamanan distribusi kunci.

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
