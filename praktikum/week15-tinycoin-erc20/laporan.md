# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: [ Proyek Kelompok – TinyCoin ERC20]  
Nama: [Annis Zunedhah Muthoharoh]  
NIM: [230202736]  
Kelas: [5 IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1.Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2.Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3.Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

### Ringkasan Proyek Kelompok – TinyCoin ERC20

TinyCoin ERC20 adalah token yang dibangun di atas standar ERC20 di jaringan Ethereum, yang memungkinkan pembuatan dan pengelolaan aset digital secara efisien. Standar ERC20 menyediakan sekumpulan aturan dan protokol yang memudahkan pengembangan token, termasuk fungsi dasar seperti transfer, persetujuan, dan penghitungan saldo. Dengan menggunakan standar ini, pengembang dapat menjamin interaksi yang konsisten dan interoperabilitas antara token yang berbeda di dalam ekosistem Ethereum.

Salah satu keunggulan dari TinyCoin adalah desentralisasi dan keamanan yang ditawarkan oleh blockchain Ethereum. Dengan memanfaatkan teknologi blockchain, setiap transaksi dan kepemilikan token tercatat secara permanen dan transparan, sehingga sulit untuk dimanipulasi. Hal ini memberikan kepercayaan lebih bagi pengguna dalam bertransaksi, karena mereka dapat memverifikasi setiap langkah tanpa memerlukan pihak ketiga. Di samping itu, TinyCoin dapat memanfaatkan smart contracts untuk mengotomatisasi berbagai proses, seperti distribusi token dan eksekusi kesepakatan tanpa campur tangan manusia.

Namun, pengembangan TinyCoin juga menghadapi tantangan, termasuk isu skalabilitas dan biaya transaksi yang sering terjadi di jaringan Ethereum. Ketika banyak pengguna bertransaksi secara bersamaan, jaringan dapat mengalami kemacetan, yang menyebabkan biaya transaksi meningkat. Oleh karena itu, penting bagi tim pengembang untuk melakukan perencanaan yang baik dan mempertimbangkan solusi alternatif, seperti penggunaan layer kedua atau protokol lain untuk meningkatkan efisiensi. Dengan memahami tantangan dan manfaat ini, TinyCoin dapat berpotensi menjadi kontribusi yang signifikan dalam ekosistem cryptocurrency.

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
1.Apa fungsi utama ERC20 dalam ekosistem blockchain?
jwab
 Fungsi Utama ERC20 dalam Ekosistem Blockchain

ERC20 memiliki beberapa fungsi utama dalam ekosistem blockchain, khususnya di jaringan Ethereum:

1. Standar Interoperabilitas: ERC20 menetapkan standar yang konsisten untuk token yang dibangun di atas blockchain Ethereum. Ini memungkinkan berbagai token untuk saling berinteraksi tanpa memerlukan penyesuaian tambahan. Dengan adanya standar ini, berbagai aplikasi dan dompet cryptocurrency dapat dengan mudah mendukung token ERC20, sehingga memudahkan pengguna dalam bertransaksi.

2. Pengaturan Fungsi Dasar: ERC20 menyediakan sekumpulan fungsi dasar yang harus dimiliki oleh setiap token, seperti transfer token, memeriksa saldo, dan pemberian persetujuan untuk pihak ketiga untuk mengakses sebagian token. Fungsi-fungsi ini menciptakan kejelasan dan kepastian dalam interaksi antara token dan pengguna, memastikan bahwa transaksi dapat dilakukan dengan aman dan efisien.

3. Mendukung Desentralisasi: Dengan memanfaatkan ERC20, pengembang dapat menciptakan token tanpa perlu mengembangkan infrastruktur dari nol. Ini mendukung desentralisasi, karena siapa pun dapat membuat dan meluncurkan token mereka sendiri. Hal ini mendorong inovasi dan pertumbuhan dalam ekosistem blockchain, memungkinkan proyek baru untuk muncul dengan lebih mudah dan cepat.

Dengan fungsi-fungsi ini, ERC20 memainkan peran penting dalam memperkuat ekosistem Ethereum dan memfasilitasi pengembangan berbagai proyek crypto yang inovatif.

2.Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20?
jawab
Mekanisme Transfer Token dalam Kontrak ERC20

Mekanisme transfer token dalam kontrak ERC20 bekerja melalui serangkaian fungsi yang sudah ditetapkan dalam standar ERC20. Berikut adalah langkah-langkah umum dari proses transfer token:

1. Fungsi Transfer: Pengguna pertama-tama memanggil fungsi `transfer(address recipient, uint256 amount)` yang terdapat dalam kontrak token. Di sini, `recipient` adalah alamat dompet penerima, dan `amount` adalah jumlah token yang ingin ditransfer.

2. Validasi Saldos: Ketika fungsi `transfer` dipanggil, kontrak akan memeriksa apakah pengirim memiliki cukup saldo untuk melakukan transfer. Jika saldo pengirim tidak mencukupi, transaksi akan gagal, dan token tidak akan ditransfer.

3. Pengurangan dan Penambahan Saldo: Jika saldo mencukupi, kontrak kemudian akan mengurangi jumlah token dari saldo pengirim dan menambahkannya ke saldo penerima. Ini dilakukan dengan memodifikasi variabel yang menyimpan saldo masing-masing alamat.

4. Pengemisión Event: Setelah transaksi selesai, kontrak memancarkan event bernama `Transfer`, yang memberikan informasi tentang alamat pengirim, alamat penerima, dan jumlah token yang ditransfer. Event ini penting karena memungkinkan aplikasi eksternal seperti dompet atau platform perdagangan untuk mendeteksi dan merespons transaksi yang telah terjadi.

5. Transaksi Tercatat di Blockchain: Terakhir, semua aktivitas ini dicatat dalam blockchain, sehingga menjadi transparan dan tidak dapat diubah. Setiap langkah dalam proses transfer dapat diverifikasi oleh pengguna lain, menjaga kepercayaan dalam ekosistem.

Dengan mekanisme ini, transfer token dalam kontrak ERC20 berjalan secara aman dan transparan, memungkinkan pengguna untuk bertransaksi dengan mudah di jaringan Ethereum.

3.Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya?
jawab
Risiko Utama dalam Implementasi Smart Contract dan Cara Mitigasinya

1. Kesalahan Coding: Salah satu risiko utama dalam smart contract adalah kesalahan dalam penulisan kode. Bug atau celah dalam logika kontrak dapat menyebabkan kerugian finansial yang signifikan. Untuk mengurangi risiko ini, penting bagi pengembang untuk melakukan pengujian menyeluruh menggunakan teknik seperti unit testing dan integrasi, serta simulasi berbagai skenario untuk memastikan bahwa kode berjalan sesuai yang diharapkan. Selain itu, audit oleh pihak ketiga yang berpengalaman juga dapat membantu menemukan dan memperbaiki masalah sebelum kontrak diluncurkan.

2. Serangan Keamanan: Smart contract rentan terhadap berbagai jenis serangan seperti reentrancy, overflow, atau underflow, di mana penyerang dapat mengeksploitasi kerentanan untuk mencuri aset. Untuk mitigasi, pengembang dapat menggunakan praktik keamanan terbaik, seperti menerapkan library yang sudah teruji (misalnya, OpenZeppelin) yang menyediakan fungsi aman. Menggunakan mekanisme kontrol akses yang ketat, serta membatasi penggunaan sumber daya, juga dapat memberikan lapisan perlindungan tambahan.

3. Tidak Dapat Diubah: Setelah smart contract diluncurkan di blockchain, sulit untuk mengubah atau memperbarui kontrak tersebut. Jika terjadi kesalahan atau ada kebutuhan untuk memperbarui fungsionalitas, kontrak yang tidak dapat diubah dapat menyebabkan masalah serius. Untuk mengatasi hal ini, pengembang bisa menggunakan pola desain yang memungkinkan pembaruan, seperti proxy contracts yang mendukung upgradeability. Selain itu, penting untuk menyertakan solusi fallback yang memastikan bahwa jika terjadi kesalahan, pengguna tetap dapat mengakses aset mereka dengan aman.

Dengan memahami risiko-risiko ini dan menerapkan langkah mitigasi yang tepat, organisasi dapat meningkatkan keamanan dan keandalan smart contract yang mereka implementasikan.

)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

### Kesimpulan Proyek Kelompok – TinyCoin ERC20

Proyek TinyCoin ERC20 merupakan sebuah inisiatif yang menggunakan standar ERC20 di jaringan Ethereum untuk menciptakan token digital yang dapat digunakan dalam berbagai aplikasi. Dengan mengikuti standar ini, TinyCoin mendukung interoperabilitas dengan berbagai dompet dan aplikasi decentralized, sehingga memudahkan pengguna dalam melakukan transaksi. Keberadaan TinyCoin dapat menjadi kontribusi penting dalam ekosistem cryptocurrency, membantu memperluas adopsi dan penggunaan token di kalangan pengguna.

Salah satu keunggulan utama dari TinyCoin adalah keamanan yang difasilitasi oleh teknologi blockchain. Setiap transaksi dan kepemilikan token tercatat secara transparan dan permanen, sehingga memperkaya kepercayaan pengguna terhadap sistem. Selain itu, penggunaan smart contracts untuk mengotomatisasi proses, seperti distribusi token, membantu mengurangi kemungkinan kesalahan manusia dan meningkatkan efisiensi dalam manajemen token.

Namun, pengembangan TinyCoin juga menghadapi tantangan yang perlu diatasi. Salah satunya adalah isu skalabilitas yang sering dialami oleh jaringan Ethereum, di mana biaya transaksi dapat meningkat ketika jumlah pengguna dan transaksi meningkat. Maka dari itu, sangat penting bagi tim pengembang untuk merencanakan solusi yang tepat agar TinyCoin dapat menangani beban transaksi yang tinggi tanpa mengorbankan biaya bagi pengguna.

Secara keseluruhan, proyek TinyCoin ERC20 menawarkan peluang besar untuk mengembangkan ekosistem token yang aman dan efisien. Dengan memperhatikan tantangan yang ada dan berfokus pada praktik terbaik dalam pengembangan, TinyCoin dapat membantu menciptakan pengalaman yang lebih baik bagi pengguna, serta berkontribusi pada inovasi teknologi blockchain di masa depan. Proyek ini menunjukkan potensi besar yang dimiliki token digital dalam memfasilitasi transaksi dan interaksi di dunia cryptocurrency.

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
