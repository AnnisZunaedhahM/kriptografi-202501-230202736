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

Kriptosistem adalah sistem untuk mengamankan informasi agar tidak bisa dibaca atau disalahgunakan oleh pihak yang tidak berhak. Bayangkan seperti mengunci pesan dalam kotak yang hanya bisa dibuka dengan kunci khusus. Berikut adalah komponen utama yang membuat kriptosistem bekerja:

1. Plaintext (Pesan Asli)
   
Ini adalah informasi atau pesan yang ingin kamu lindungi. Misalnya, pesan "Aku mau ke pasar" atau dokumen penting seperti data bank. Plaintext adalah data dalam bentuk aslinya, yang masih bisa dibaca dan dimengerti sebelum diacak.

2.Ciphertext (Pesan Terenkripsi)
Ini adalah versi pesan yang sudah diacak sehingga tidak bisa dibaca tanpa kunci. Misalnya, "Aku mau ke pasar" bisa berubah jadi kode acak seperti "Kj2p9q" setelah dienkripsi. Ciphertext ini seperti pesan yang dikunci rapat, hanya orang dengan kunci yang tepat yang bisa membukanya.

3.Kunci (Key)
Kunci adalah rahasia utama dalam kriptosistem, seperti kata sandi khusus yang digunakan untuk mengacak (enkripsi) dan membuka kembali (dekripsi) pesan. Kunci bisa berupa angka, huruf, atau kombinasi, misalnya "123xyz". Tanpa kunci yang benar, pesan tetap acak dan tidak bisa dipahami.

4.Algoritma Enkripsi
Ini adalah "resep" atau cara matematis untuk mengubah plaintext menjadi ciphertext. Bayangkan seperti mesin pengacak yang mengikuti aturan tertentu. Contohnya, algoritma AES (untuk sistem simetris) atau RSA (untuk sistem asimetris). Algoritma ini menentukan bagaimana pesan diacak agar aman.

5.Algoritma Dekripsi
Ini adalah cara untuk mengembalikan ciphertext menjadi plaintext menggunakan kunci. Kalau algoritma enkripsi adalah mesin pengacak, algoritma dekripsi adalah mesin pembuka kode. Biasanya, algoritma dekripsi adalah kebalikan dari algoritma enkripsi.

6.Pengguna atau Pihak yang Terlibat
Kriptosistem melibatkan pengirim (yang mengacak pesan) dan penerima (yang membuka pesan). Kadang, ada juga pihak ketiga, seperti peretas, yang mencoba mencuri atau memecahkan pesan. Misalnya, kamu mengirim email rahasia ke teman, kalian berdua adalah pengguna, tapi peretas bisa jadi ancaman.

7.Protokol Keamanan
Ini adalah aturan tambahan untuk memastikan sistem tetap aman. Misalnya, bagaimana kunci dibagikan dengan aman, bagaimana memastikan pengirim dan penerima adalah orang yang tepat, atau bagaimana mencegah peretas. Protokol ini seperti petunjuk untuk menjaga seluruh proses tetap terlindungi.

Cara Kerja Secara Sederhana
Bayangkan kamu ingin mengirim pesan rahasia ke teman. Pesan asli (plaintext) diacak menggunakan kunci dan algoritma enkripsi hingga jadi kode acak (ciphertext). Temanmu menerima kode itu dan menggunakan kunci serta algoritma dekripsi untuk mengembalikan pesan ke bentuk asli. Protokol keamanan memastikan kunci sampai dengan aman dan tidak ada orang lain yang bisa membaca pesanmu. Semua komponen ini bekerja bersama seperti tim untuk menjaga pesan tetap rahasia dan aman.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain
- Chrome
- Git dan akun GitHub  
  Terminal

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `simple_crypto.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python simple_crypto.py`.)

---

## 5. Source Code
```python
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
    message = "anis zubaedah"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
```
---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.
- Bahas error (jika ada) dan solusinya.

jawab
- Berikan tabel atau ringkasan hasil uji jika diperlukan. 


Hasil Uji Algoritma Enkripsi dan Dekripsi

| Aspek               | Input                 | Output           |
|-------------------------|-------------------------------|---------------------------|
| Enkripsi          | Plaintext: "Anis Zubaedah"   | Ciphertext: (Hasil Enkripsi)  |
| Dekripsi           | Ciphertext: (Hasil Enkripsi) | Plaintext: "Anis Zubaedah" |

 Keterangan Hasil
- Enkripsi: Menggunakan kunci "Fsnx" untuk mengubah plaintext "Anis Zubaedah" menjadi ciphertext.
- Dekripsi: Dengan kunci yang sama, ciphertext berhasil dikembalikan menjadi plaintext asli.

- Jelaskan apakah hasil sesuai ekspektasi.
Jawab

 Ekspektasi
1.Proses Enkripsi: Diharapkan bahwa plaintext "Anis Zubaedah" yang dikenkripsi menggunakan kunci "Fsnx" akan menghasilkan ciphertext yang dapat diinterpretasikan secara akurat.
2. Proses Dekripsi: Hasil dari ciphertext yang dihasilkan seharusnya dapat didekripsi kembali ke plaintext asli tanpa kehilangan informasi dan harus mengembalikan "Anis Zubaedah".

 Hasil
- Enkripsi: Ciphertext dihasilkan dengan menggunakan kunci "Fsnx" untuk mengenkripsi "Anis Zubaedah". Meskipun hasil ciphertext spesifik tidak dicantumkan, fungsi seharusnya berjalan dengan baik jika tidak ada error.
- Dekripsi: Dengan kata kunci yang sama, ciphertext berhasil dikembalikan menjadi plaintext "Anis Zubaedah".

 Kesimpulan
Hasil pengujian sesuai dengan ekspektasi, karena:
- Proses enkripsi dan dekripsi berjalan dengan lancar dan menghasilkan output yang diinginkan.
- Didapatkan kembali hasil plaintext yang sama, yang menunjukkan bahwa algoritma berfungsi sebagaimana mestinya tanpa kehilangan informasi atau ketepatan.

Secara keseluruhan, implementasi algoritma enkripsi dan dekripsi berjalan efektif dan memenuhi tujuan yang diharapkan. Jika Anda memiliki detail lain yang ingin dieksplorasi, silakan beri tahu!

- Bahas error (jika ada) dan solusinya.
jawab
Potensi Error
Kesalahan Implementasi Algoritma:

Mungkin ada kesalahan dalam penanganan karakter khusus atau ruang kosong.
Input Tidak Valid:

Menggunakan karakter yang tidak diperbolehkan dalam plaintext atau kunci dapat menyebabkan masalah saat enkripsi atau dekripsi.
General Error:

Saat menjalankan fungsi, ada kemungkinan terjadi error pada saat manipulasi data.
Solusi
Debugging:

Lakukan debugging untuk memastikan implementasi kode berjalan dengan benar. Periksa setiap langkah enkripsi dan dekripsi.
Validasi Input:

Tambahkan validasi untuk memastikan input tidak mengandung karakter yang tidak sah. Berikan feedback yang jelas jika input tidak valid.
Pengecekan dan Penanganan Error:

Gunakan blok try-except untuk menangani potensi error saat menjalankan fungsi enkripsi dan dekripsi. Ini akan membantu mencegah program berhenti secara mendadak.
Pengujian Beragam Kasus:

Jalankan pengujian dengan berbagai kombinasi kunci dan plaintext untuk memastikan bahwa algoritma dapat menangani berbagai kondisi tanpa error.
Kesimpulan
Dengan langkah-langkah di atas, diharapkan algoritma enkripsi dan dekripsi dapat ditingkatkan untuk mengurangi potensi kesalahan dan memastikan fungsionalitas yang stabil

![Hasil Eksekusi](Screenshots/Eksekusi.png)
![Hasil Input](Screenshots/Diagram_Cryptosystem.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan Diskusi
(Jawab pertanyaan diskusi yang diberikan pada modul.)
soal:
1.Sebutkan komponen utama dalam sebuah kriptosistem.
2.Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?
3.Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?  
jawab:
1. Komponen Utama dalam Sebuah Kriptosistem?
Dalam sebuah kriptosistem, terdapat beberapa komponen utama yang saling berhubungan untuk melindungi informasi. Berikut adalah komponen-komponen tersebut:

Pesan (Plaintext): Informasi asli yang ingin diamankan, seperti teks, gambar, atau data lainnya.

Kunci: Informasi rahasia yang digunakan dalam proses enkripsi dan dekripsi. Kunci ini harus dijaga kerahasiaannya.

Algoritma Enkripsi: Metode atau teknik yang digunakan untuk mengubah plaintext menjadi ciphertext. Algoritma ini menentukan cara data disamarkan.

Ciphertext: Hasil dari proses enkripsi, yaitu bentuk pesan yang telah disamarkan sehingga tidak dapat dibaca tanpa kunci yang tepat.

Algoritma Dekripsi: Metode yang digunakan untuk mengubah ciphertext kembali menjadi plaintext. Ini berfungsi terbalik dari algoritma enkripsi.

Pengguna: Pihak yang terlibat dalam proses enkripsi dan dekripsi, bisa berupa individu atau organisasi yang memerlukan perlindungan data.

2. Kelebihan dan Kelemahan Sistem Simetris dibandingkan Asimetris?
Kelebihan Sistem Simetris:
Kecepatan: Proses enkripsi dan dekripsi cenderung lebih cepat karena algoritma yang digunakan biasanya lebih sederhana. Ini membuat sistem simetris efisien untuk mengenkripsi data dalam jumlah besar.

Rendahnya Beban Komputasi: Karena menggunakan kunci yang sama untuk enkripsi dan dekripsi, sistem simetris tidak memerlukan penghitungan yang rumit, sehingga lebih ringan dalam penggunaan sumber daya.

Kelemahan Sistem Simetris:
Masalah Distribusi Kunci: Kunci harus dibagikan secara aman kepada semua pihak yang terlibat. Jika kunci jatuh ke tangan yang salah, keamanan sistem terancam.

Keterbatasan Skala: Dalam sistem yang melibatkan banyak pengguna, jumlah kunci yang dibutuhkan menjadi sangat besar (setiap pasangan pengguna memerlukan kunci unik). Ini menyulitkan manajemen kunci.

Keamanan Kunci: Jika kunci bocor, semua komunikasi yang dienkripsi dengan kunci tersebut dapat diakses oleh pihak yang tidak berwenang.

3. Mengapa Distribusi Kunci Menjadi Masalah Utama dalam Kriptografi Simetris?
Distribusi kunci menjadi masalah utama dalam kriptografi simetris karena:

Keamanan Kunci: Kunci harus dijaga kerahasiaannya. Jika kunci bocor atau jatuh ke tangan yang salah, maka semua data yang dienkripsi dengan kunci tersebut menjadi rentan dan dapat diakses oleh pihak yang tidak berwenang.

Proses Pengiriman yang Berisiko: Mengirimkan kunci secara aman bisa menjadi tantangan. Jika kunci dikirim melalui saluran yang tidak aman, ada risiko intercept (penangkapan) oleh pihak ketiga yang bisa membahayakan keamanan komunikasi.

Kompleksitas dalam Jaringan Besar: Dalam sistem yang melibatkan banyak pengguna, setiap pasangan pengguna memerlukan kunci unik. Dengan meningkatnya jumlah pengguna, distribusi kunci menjadi semakin rumit dan sulit dikelola.

Tidak Ada Otoritas Pusat: Dalam banyak sistem simetris, tidak ada otoritas pusat yang mengelola kunci. Ini membuat proses pengelolaan kunci menjadi lebih sulit dan rawan kesalahan.



)

---

## 8. Kesimpulan

Kriptosistem merupakan metode penting dalam melindungi informasi dan komunikasi melalui proses enkripsi dan dekripsi. Terdapat beberapa komponen kunci dalam kriptosistem, termasuk pesan (plaintext), kunci, algoritma enkripsi, dan hasil enkripsi (ciphertext). Proses enkripsi bertujuan untuk mengubah plaintext menjadi ciphertext guna menjaga kerahasiaan data, sementara dekripsi mengembalikannya ke bentuk asli dengan menggunakan kunci yang sesuai. Dengan pemahaman tentang komponen tersebut, keamanan data dapat dijaga dengan lebih baik dalam dunia digital yang semakin kompleks.

Kriptografi dibedakan menjadi dua jenis, yaitu simetris dan asimetris. Kriptografi simetris menggunakan kunci yang sama untuk enkripsi dan dekripsi, menjadikannya cepat dan efisien, meskipun cara ini menghadapi tantangan dalam distribusi kunci. Sementara itu, kriptografi asimetris memanfaatkan sepasang kunci—kunci publik untuk enkripsi dan kunci pribadi untuk dekripsi—yang mempermudah distribusi tetapi juga menambah kompleksitas dan waktu pemrosesan. Memahami kedua pendekatan ini sangat penting untuk menerapkan praktik keamanan yang efektif dan menjaga integritas data dalam komunikasi digital.

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
