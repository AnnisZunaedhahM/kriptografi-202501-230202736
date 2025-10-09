# Laporan Praktikum Kriptografi                                   
Minggu ke-: 01
Topik: CIA_intro.md 
Nama: annis zunaedhah muthoharoh
NIM:  230202736 
Kelas: [5 IKRB]  

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2.Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3.Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4.Menyiapkan repositori GitHub sebagai media kerja praktikum.

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Sejarah Kriptografi & Prinsip CIA Confidentiality

Langkah 1 — Ringkasan Sejarah Kriptografi
Kriptografi adalah seni dan ilmu untuk menyamarkan pesan agar tidak dapat dibaca oleh pihak yang tidak berwenang. Perkembangan kriptografi dapat dibagi menjadi tiga era utama, yang menunjukkan evolusi dari metode fisik yang sederhana hingga algoritma matematika yang kompleks.

1. Era Kriptografi Klasik (Manual dan Fisik)
Pada masa ini, enkripsi dilakukan tanpa mesin elektronik dan lebih mengandalkan teknik penggantian (substitusi) atau pengacakan posisi (transposisi).

Caesar Cipher: Diciptakan oleh Julius Caesar, ini adalah contoh sederhana dari sandi substitusi. Setiap huruf pada pesan diganti dengan huruf lain yang memiliki pergeseran tetap dalam alfabet.
Vigenère Cipher: Merupakan metode yang lebih kuat dibandingkan Caesar karena menggunakan kunci berupa kata. Penggantian huruf dilakukan berdasarkan huruf dari kunci, sehingga membuat analisis frekuensi lebih sulit dan meningkatkan keamanan pesan.
2. Perkembangan Kriptografi Modern (Komputer dan Matematika)
Era ini dimulai ketika kriptografi mulai dipublikasikan secara terbuka dan memanfaatkan kekuatan komputer serta teori matematika yang kompleks.

Kriptografi Kunci Simetris (Symmetric-Key): Menggunakan satu kunci yang sama untuk enkripsi dan dekripsi. Contoh yang terkenal adalah AES (Advanced Encryption Standard), algoritma enkripsi simetris yang paling umum digunakan untuk melindungi data, baik saat transit maupun saat disimpan.
Kriptografi Kunci Asimetris/Publik (Asymmetric/Public-Key): Menggunakan dua kunci yang berbeda dan berpasangan—Kunci Publik yang dapat dibagikan untuk enkripsi dan Kunci Privat yang dirahasiakan untuk dekripsi. Contohnya adalah RSA, algoritma kunci publik yang banyak digunakan untuk tanda tangan digital dan pertukaran kunci yang aman.
3. Evolusi Menuju Kriptografi Kontemporer (Era Desentralisasi)
Kriptografi kini tidak hanya digunakan untuk mengamankan komunikasi, tetapi juga menjadi dasar bagi sistem keuangan dan otentikasi baru.

Blockchain dan Cryptocurrency: Teknologi ini, seperti Bitcoin dan Ethereum, bergantung pada kriptografi untuk menjamin integritas data dalam blok dan menggunakan kriptografi kunci publik untuk membuktikan kepemilikan aset tanpa perantara seperti bank.
Kriptografi Pasca-Quantum: Fokus penelitian saat ini adalah mengembangkan algoritma baru yang tahan terhadap serangan dari komputer kuantum, yang dapat memecahkan sandi RSA dan ECC dengan mudah.

Definisi Cipher Klasik

Cipher Klasik adalah metode enkripsi yang digunakan untuk menyembunyikan pesan dengan mengubah teks asli (plaintext) menjadi bentuk yang tidak dapat dibaca (ciphertext) menggunakan teknik tertentu. Contohnya mencakup metode substitusi dan transposisi:

Caesar Cipher: Menggeser setiap huruf dalam alfabet dengan jumlah tertentu.
Vigenère Cipher: Menggunakan kunci untuk mengubah huruf dalam pesan, membuatnya lebih kompleks dan sulit dipecahkan.
Cipher klasik memiliki kelemahan, seperti kerentanan terhadap analisis frekuensi, yang membuatnya lebih mudah dipecahkan dibandingkan metode kriptografi modern.

Konsep Modular Aritmetika

Modular Aritmetika adalah cabang matematika yang berfokus pada operasi aritmetika dalam konteks sisa pembagian. Dalam notasi modular, kita menuli
Operasi dasar dalam modular aritmetika meliputi penjumlahan, pengurangan, dan perkalian. Konsep ini sangat penting dalam kriptografi, terutama dalam algoritma seperti RSA, di mana operasi dilakukan dalam modulus untuk menghasilkan nilai yang aman dan tidak dapat diprediksi.

Soal 2 — Prinsip CIA Triad

CIA Triad (Confidentiality, Integrity, Availability) adalah tiga pilar fundamental yang membentuk kerangka kerja keamanan informasi. Untuk memastikan bahwa sebuah sistem aman, ketiga prinsip ini harus dipertahankan.

1. Confidentiality (Kerahasiaan)
Prinsip ini bertujuan untuk melindungi informasi dari akses yang tidak berhak atau pengungkapan kepada pihak yang tidak memiliki izin.

Analoginya: Seperti surat yang tersegel dalam amplop.
Tujuannya: Menjaga privasi data, seperti kata sandi dan catatan medis, agar tetap rahasia.
Mekanisme: Menggunakan enkripsi, password yang kuat, dan otorisasi untuk membatasi akses sesuai dengan peran pengguna.
2.Integrity (Integritas)
Prinsip ini memastikan bahwa informasi akurat, lengkap, dan tidak diubah oleh pihak yang tidak berwenang selama penyimpanan atau transmisi.

Analoginya: Seperti dokumen yang memiliki segel atau tanda tangan digital asli.
Tujuannya: Menjamin keutuhan data sehingga penerima yakin bahwa pesan yang diterima sama persis dengan yang dikirim oleh sumber yang sah.
Mekanisme: Menggunakan fungsi hash untuk mendeteksi perubahan dan tanda tangan digital untuk verifikasi.

3.Availability (Ketersediaan)

Prinsip ini memastikan bahwa sistem dan sumber daya informasi dapat diakses dan digunakan oleh pengguna yang sah kapan pun diperlukan.

Analoginya: Seperti pintu bank yang selalu terbuka pada jam operasional.
Tujuannya: Menjamin kelangsungan layanan sehingga kegagalan sistem tidak menghalangi akses informasi.
Mekanisme: Menggunakan perangkat keras yang andal, bandwidth jaringan yang memadai, dan rencana pemulihan bencana

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
(Jawab pertanyaan diskusi yang diberikan pada modul.)  

Jawaban Soal Quiz

1. Siapa Tokoh yang Dianggap sebagai Bapak Kriptografi Modern?

Claude Shannon adalah tokoh yang dianggap sebagai bapak kriptografi modern. Pada tahun 1949, ia menerbitkan karya penting yang berjudul "Communication Theory of Secrecy Systems," di mana ia memperkenalkan konsep-konsep dasar tentang keamanan informasi dan kriptografi. Shannon mengembangkan teori informasi yang menjelaskan bagaimana cara mengukur dan mengelola informasi dalam komunikasi. Karyanya menjadi landasan bagi banyak teknik kriptografi modern yang kita gunakan saat ini.

2. Sebutkan Algoritma Kunci Publik yang Populer Digunakan Saat Ini
Beberapa algoritma kunci publik yang populer dan banyak digunakan saat ini antara lain:

RSA (Rivest-Shamir-Adleman): Salah satu algoritma paling awal dan paling umum untuk enkripsi dan tanda tangan digital. RSA menggunakan dua kunci, yaitu kunci publik untuk enkripsi dan kunci privat untuk dekripsi.

DSA (Digital Signature Algorithm): Digunakan khusus untuk tanda tangan digital. DSA juga menggunakan kunci publik dan privat, tetapi metode matematikanya berbeda dari RSA.

ECC (Elliptic Curve Cryptography): Menggunakan struktur matematika dari kurva eliptik untuk memberikan keamanan yang lebih tinggi dengan ukuran kunci yang lebih kecil dibandingkan RSA atau DSA.

ElGamal: Digunakan untuk enkripsi dan tanda tangan digital, algoritma ini juga berbasis pada masalah logaritma diskrit.

3. Apa Perbedaan Utama antara Kriptografi Klasik dan Kriptografi Modern?
   
Perbedaan utama antara kriptografi klasik dan kriptografi modern dapat dijelaskan sebagai berikut:
Pendekatan Kunci
Kriptografi Klasik: Mengandalkan metode simetris, di mana kunci yang sama digunakan untuk enkripsi dan dekripsi. Contohnya termasuk metode Caesar dan Vigenère. Masalah utama adalah pengiriman kunci yang aman.
Kriptografi Modern: Menggunakan metode asimetris (kunci publik dan kunci privat). Ini memungkinkan pertukaran kunci yang aman tanpa memerlukan saluran komunikasi yang aman.

Keamanan
Kriptografi Klasik: Keamanan bergantung pada kerumitan algoritma dan panjang kunci. Banyak metode klasik telah dipecahkan dengan kemajuan dalam analisis matematika dan komputasi.
Kriptografi Modern: Mengandalkan prinsip matematika yang lebih kompleks seperti teori bilangan dan masalah matematis yang sulit, sehingga lebih sulit untuk dipecahkan bahkan dengan teknologi komputer yang canggih.

Penggunaan
Kriptografi Klasik: Terutama digunakan dalam situasi di mana komunikasi aman dapat dilakukan, seperti surat-menyurat rahasia.
Kriptografi Modern: Digunakan dalam berbagai aplikasi, termasuk transaksi keuangan online, komunikasi aman di internet, dan sistem identifikasi digital.Quiz Singkat

)
---

## 8. Kesimpulan
Kriptografi telah mengalami perkembangan yang signifikan dari era klasik hingga modern, yang mencerminkan evolusi teknologi dan kebutuhan keamanan informasi.

Di era klasik, metode kriptografi seperti Caesar Cipher dan Vigenère Cipher menggunakan teknik sederhana yang mudah dipecahkan. Keamanan bergantung pada kerahasiaan kunci, dan metode ini sering kali rentan terhadap analisis frekuensi. Dengan adanya kemajuan dalam matematika dan teknologi, kriptografi modern muncul dengan algoritma yang jauh lebih kompleks, seperti RSA dan AES. Algoritma ini tidak hanya lebih aman tetapi juga memungkinkan penggunaan kunci publik dan kunci privat, meningkatkan cara kita melindungi informasi.

Tokoh kunci dalam transisi ini adalah Claude Shannon, yang menciptakan fondasi teoritis untuk kriptografi modern. Ia memperkenalkan konsep-konsep yang memungkinkan kita untuk memahami dan mengukur keamanan dalam komunikasi digital.

Dalam konteks saat ini, prinsip-prinsip keamanan informasi—Confidentiality, Integrity, dan Availability (CIA)—menjadi landasan bagi sistem keamanan yang efektif. Kerahasiaan menjaga data tetap aman dari akses yang tidak sah, integritas memastikan bahwa informasi tidak diubah tanpa izin, dan ketersediaan menjamin bahwa data dapat diakses kapan saja oleh pihak yang berwenang.

Secara keseluruhan, kriptografi modern tidak hanya melindungi data dan komunikasi, tetapi juga memainkan peran penting dalam membangun kepercayaan dalam transaksi digital, terutama di era di mana informasi sangat berharga dan rentan terhadap ancaman. Dengan pemahaman yang baik tentang kriptografi dan prinsip-prinsip keamanannya, kita dapat lebih siap menghadapi tantangan keamanan informasi di masa depan.


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

