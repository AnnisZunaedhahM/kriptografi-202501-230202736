# Laporan Praktikum Kriptografi
Minggu ke-:13 
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Annis Zunaedhah Muthoharoh]  
NIM: [230202736]  
Kelas: [5  IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1.Menjelaskan peran hash function dalam blockchain.
2.Melakukan simulasi sederhana Proof of Work (PoW).
3.Menganalisis keamanan cryptocurrency berbasis kriptografi.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

### Ringkasan TinyChain – Proof of Work (PoW)

Proof of Work (PoW) adalah cara yang digunakan dalam blockchain untuk menjaga keamanan dan keabsahan data. Dalam PoW, peserta jaringan harus melakukan perhitungan matematis yang rumit sebagai bukti bahwa mereka sudah melakukan "pekerjaan." Proses ini penting untuk memvalidasi transaksi dan mencegah berbagai serangan di dalam jaringan.

Dalam penerapan PoW, konsep modular aritmetika sangat berperan, di mana fungsi hash dibuat untuk menghasilkan hasil yang sulit diprediksi. Hal ini membuat peserta perlu menginvestasikan daya komputasi untuk dapat bersaing dalam proses penambangan, yang pada gilirannya meningkatkan keamanan jaringan.

Namun, PoW juga memiliki tantangan, seperti penggunaan energi yang sangat tinggi dan risiko sentralisasi, di mana peserta yang memiliki sumber daya lebih mendominasi jaringan. Masalah ini mendorong pengembang untuk mencari alternatif lain, seperti Proof of Stake (PoS), yang bisa lebih efisien namun tetap menjaga keamanan jaringan.

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
- Pertanyaan 

1.Mengapa fungsi hash sangat penting dalam blockchain?
jawab
 Pentingnya Fungsi Hash dalam Blockchain

Fungsi hash sangat penting dalam blockchain karena beberapa alasan utama:

1. Keamanan Data: Fungsi hash mengubah data menjadi string karakter tetap (hash) yang unik. Setiap perubahan kecil pada data akan menghasilkan hash yang sangat berbeda. Ini memastikan bahwa data dalam blockchain tidak dapat dimanipulasi tanpa terdeteksi, sehingga menjaga keamanan informasi yang tersimpan.

2. Integritas Data: Dengan menggunakan fungsi hash, setiap blok dalam blockchain berisi hash dari blok sebelumnya. Ini menciptakan rantai yang terhubung, di mana perubahan pada satu blok akan mempengaruhi semua blok berikutnya. Jika seseorang mencoba mengubah informasi di satu blok, hash yang dihasilkan akan berbeda, dan jaringan dapat dengan mudah mendeteksi perubahan tersebut.

3.*Efisiensi dan Kecepatan: Fungsi hash dapat menghitung hasil dengan cepat, memungkinkan validasi transaksi dan blok baru secara efisien. Ini membuat proses penambangan dan verifikasi transaksi menjadi lebih cepat, sehingga transaksi dapat diproses dengan lebih efektif dalam jaringan blockchain.

Dengan semua manfaat ini, fungsi hash menjadi fondasi penting dalam menjaga keamanan, integritas, dan efisiensi sistem blockchain.

2.Bagaimana Proof of Work mencegah double spending?
jawab
Cara Proof of Work Mencegah Double Spending

Proof of Work (PoW) mencegah double spending—situasi di mana seseorang berusaha menghabiskan uang yang sama lebih dari sekali—melalui beberapa mekanisme kunci:

1. Verifikasi Transaksi: Dalam sistem PoW, setiap transaksi yang diajukan harus divalidasi oleh para penambang sebelum ditambahkan ke blockchain. Para penambang menggunakan daya komputasi mereka untuk memecahkan perhitungan matematis yang kompleks, dan hanya setelah transaksi divalidasi dan blok baru ditambahkan, transaksi tersebut dianggap sah. Proses ini memastikan bahwa transaksi yang sama tidak dapat diproses lebih dari sekali.

2. Rantai Blok yang Terhubung: Setiap blok dalam blockchain berisi hash dari blok sebelumnya. Ini menciptakan suatu rantai yang terhubung, di mana setiap blok membutuhkan semua informasi dari blok sebelumnya untuk dapat divalidasi. Jika seseorang mencoba untuk mengubah transaksi dalam satu blok untuk menghabiskan uang yang sama, seluruh rantai blok yang mengikuti berubah, dan perubahan tersebut akan terdeteksi oleh jaringan.

3. onsensus Jaringan Dalam blockchain yang menggunakan PoW, semua peserta (atau node) harus mencapai konsensus mengenai keadaan jaringan. Jika satu peserta mencoba menghabiskan uang yang sama di dua transaksi berbeda, jaringan akan lebih cenderung menerima transaksi yang pertama kali divalidasi, sementara yang kedua akan ditolak. Proses konsensus ini membuatnya sulit bagi penipu untuk melakukan double spending tanpa pengawasan dari jaringan yang lebih besar.

Dengan kombinasi verifikasi transaksi, integritas rantai blok, dan mekanisme konsensus, Proof of Work secara efektif mencegah double spending dan memastikan keandalan sistem blockchain.

3.Apa kelemahan dari PoW dalam hal efisiensi energi?
jawab

 Kelemahan Proof of Work dalam Hal Efisiensi Energi

Proof of Work (PoW) memiliki beberapa kelemahan terkait efisiensi energi, antara lain:

1. Konsumsi Energi yang Tinggi: Proses penambangan dalam sistem PoW membutuhkan daya komputasi yang besar, yang pada gilirannya memerlukan konsumsi energi yang sangat tinggi. Penambang bersaing untuk memecahkan perhitungan matematis yang kompleks, dan ini sering kali melibatkan penggunaan perangkat keras khusus yang menghabiskan banyak listrik.

2. Dampak Lingkungan: Tingginya penggunaan energi dalam PoW berkontribusi pada peningkatan emisi karbon, terutama jika energi yang digunakan berasal dari sumber yang tidak terbarukan. Ini menimbulkan kekhawatiran lingkungan, karena penambangan mata uang kripto dapat menyebabkan kerusakan ekosistem dan meningkatkan jejak karbon secara keseluruhan.

3. Biaya Operasional: Selain dampak lingkungan, biaya operasional yang tinggi juga menjadi kelemahan. Penambang harus mengeluarkan biaya yang signifikan untuk listrik dan perangkat keras, yang dapat menghambat partisipasi pengguna baru dalam jaringan. Hal ini juga dapat mengarah pada sentralisasi, di mana hanya entitas dengan sumber daya yang cukup yang mampu berinvestasi dalam kompetisi penambangan.

4. Keterbatasan Skalabilitas: Dengan tingginya konsumsi energi, PoW juga menghadapi tantangan dalam skalabilitas. Ketika lebih banyak transaksi dilakukan, semakin banyak penambang yang terlibat, dan kebutuhan energi dapat meningkat, yang dapat memperlambat waktu pemrosesan transaksi dan membuat jaringan kurang efisien.

Kelemahan-kelemahan ini mendorong pencarian alternatif lain, seperti Proof of Stake (PoS), yang lebih efisien dalam penggunaan energi sambil tetap menjaga keamanan jaringan.
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

### TinyChain – Proof of Work (PoW)

Proof of Work (PoW) adalah mekanisme konsensus yang digunakan dalam TinyChain untuk memastikan keamanan dan integritas data dalam jaringan blockchain. Dalam sistem ini, peserta jaringan, atau penambang, harus melakukan perhitungan matematis yang kompleks sebagai bukti bahwa mereka telah menyelesaikan "pekerjaan." Proses ini tidak hanya berfungsi untuk memvalidasi transaksi, tetapi juga mencegah serangan dengan membuatnya biaya tinggi untuk memanipulasi data, sehingga menjaga keaslian informasi yang tersimpan.

Salah satu keunggulan PoW adalah kemampuannya untuk menciptakan proses verifikasi yang transparan dan dapat diandalkan. Setiap blok baru yang ditambahkan ke blockchain berisi hash dari blok sebelumnya, membentuk rantai yang terhubung. Jika ada yang mencoba mengubah informasi dalam satu blok, perubahan itu akan merusak rantai dan tampak jelas bagi semua peserta jaringan. Ini meningkatkan ketahanan terhadap penipuan, termasuk upaya double spending, di mana seseorang mencoba menghabiskan cryptocurrency yang sama lebih dari sekali.

Namun, mekanisme PoW juga memiliki kelemahan, terutama dalam hal efisiensi energi. Proses penambangan memerlukan konsumsi daya yang tinggi, yang berpotensi berdampak negatif pada lingkungan. Biaya operasional yang besar ini dapat menghambat partisipasi pengguna baru, menciptakan risiko sentralisasi, dan menghadirkan tantangan dalam skalabilitas jaringan. Oleh karena itu, meskipun PoW efektif menjaga keamanan, tantangan ini mendorong eksplorasi solusi alternatif yang lebih efisien, seperti Proof of Stake (PoS), untuk masa depan TinyChain.
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
Author: Nama:annis zunaedhah muthoharoh <email : anniszunaedah@gmail.com>
Date:   2025-12-08

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
