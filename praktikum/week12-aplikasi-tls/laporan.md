# Laporan Praktikum Kriptografi
Minggu ke-: 12
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Annis zunaedhah Muthoharoh]  
NIM: [230202736]  
Kelas: [5 IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1.Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2.Menjelaskan enkripsi dalam transaksi e-commerce.
3.Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

### Aplikasi TLS dalam E-Commerce

Transport Layer Security (TLS) adalah protokol kriptografi yang dirancang untuk menyediakan keamanan komunikasi melalui jaringan komputer. Dalam konteks e-commerce, TLS mengamankan data yang ditransmisikan antara pelanggan dan server, melindungi informasi sensitif seperti nomor kartu kredit, data pribadi, dan kredensial pengguna. Protokol ini menggunakan enkripsi untuk memastikan bahwa data yang dikirimkan tidak dapat dibaca oleh pihak ketiga, dan sekaligus autentikasi untuk memastikan bahwa pengguna terhubung dengan server yang benar.

Proses kerja TLS melibatkan negosiasi jalur komunikasi yang aman, yang dimulai dengan handshake TLS. Selama proses ini, klien dan server bertukar informasi, termasuk sertifikat digital yang digunakan untuk memverifikasi identitas masing-masing pihak. Setelah verifikasi, kunci sesi dihasilkan untuk melakukan enkripsi data yang akan dikirim. Dengan demikian, TLS tidak hanya menjamin kerahasiaan dan integritas data, tetapi juga membangun kepercayaan antara pelaku e-commerce dan pelanggan, yang sangat penting untuk keberhasilan transaksi online.

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
1.Apa perbedaan utama antara HTTP dan HTTPS?
jawab
### Perbedaan Utama antara HTTP dan HTTPS

1. Keamanan:
   - HTTP (Hypertext Transfer Protocol) adalah protokol dasar untuk mengakses informasi di web, tetapi ia tidak menyediakan lapisan keamanan, sehingga data yang ditransmisikan melalui HTTP dapat dengan mudah disadap atau dimanipulasi oleh pihak ketiga.
   - HTTPS (HTTP Secure), di sisi lain, merupakan versi aman dari HTTP yang menggunakan enkripsi melalui protokol TLS (Transport Layer Security) atau SSL (Secure Sockets Layer). Enkripsi ini melindungi data yang ditransmisikan, membuatnya sulit bagi penyerang untuk mengintersepsi atau mengakses informasi sensitif.

2. Port yang Digunakan:
   - HTTP menggunakan port 80 secara default untuk komunikasi, sedangkan HTTPS menggunakan port 443. Perubahan ini mencerminkan perbedaan dalam cara kedua protokol beroperasi dan keamanan yang terkait dengan komunikasi data.

3. URL dan Identifikasi:
   - URL yang menggunakan HTTP diawali dengan `http://`, sedangkan URL untuk HTTPS diawali dengan `https://`. Selain itu, banyak browser juga menunjukkan indikator visual, seperti ikon gembok, untuk menandakan bahwa koneksi HTTPS aman, memberikan kepercayaan lebih kepada pengguna mengenai keamanan saat bertransaksi.

### Kesimpulan

Secara keseluruhan, perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanan, penggunaan port, dan cara mereka diidentifikasi di browser. HTTPS menawarkan perlindungan yang lebih baik untuk data dan identitas pengguna, yang sangat penting dalam konteks transaksi online dan komunikasi yang melibatkan informasi sensitif.

2.Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
jawab
### Pentingnya Sertifikat Digital dalam Komunikasi TLS

1. Autentikasi Identitas:
   - Sertifikat digital memainkan peranan krusial dalam memastikan bahwa pihak yang terlibat dalam komunikasi TLS adalah siapa yang mereka klaim. Ketika pengguna menghubungi server, sertifikat digital yang diterbitkan oleh Certificate Authority (CA) tepercaya digunakan untuk memverifikasi identitas server. Ini mencegah penyerang melakukan serangan man-in-the-middle (MITM) dengan menyamar sebagai server yang sah, sehingga memberikan jaminan bahwa data ditransmisikan ke tujuan yang benar.

2. Enkripsi dan Keamanan Data:
   - Dengan sertifikat digital, informasi yang ditransmisikan selama sesi TLS dapat dienkripsi secara efektif. Sertifikat ini mengandung kunci publik server, yang digunakan oleh klien untuk mengenkripsi data yang akan dikirim. Hanya server yang memiliki kunci privat yang sesuai yang dapat mendekripsi informasi tersebut. Ini memastikan kerahasiaan data, melindungi informasi sensitif pengguna, seperti data pribadi, nomor kartu kredit, dan kredensial login, dari penyadapan oleh pihak ketiga.

3. Integritas Data:
   - Sertifikat digital juga memastikan bahwa data yang ditransmisikan tidak diubah atau dimanipulasi selama proses komunikasi. Dengan menggunakan tanda tangan digital dan metode kriptografi lainnya, penerima dapat memverifikasi bahwa data yang diterima adalah utuh dan berasal dari pengirim yang sah. Ini memberikan tingkat perlindungan tambahan yang penting dalam dunia yang semakin terhubung dan rentan terhadap serangan siber.

### Kesimpulan

Secara keseluruhan, sertifikat digital merupakan komponen penting dalam komunikasi TLS, memberikan autentikasi, enkripsi, dan integritas data yang diperlukan untuk menjaga keamanan dan kepercayaan dalam interaksi online. Dengan demikian, mereka memainkan peran kunci dalam membangun kepercayaan di seluruh ekosistem internet, khususnya dalam aplikasi e-commerce dan layanan online yang sensitif.

3.Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?

jawab
### Peran Kriptografi dalam Privasi dan Tantangan Hukum serta Etika

1. Dukungan untuk Privasi:
   - Kriptografi berfungsi sebagai mekanisme keamanan yang kuat untuk melindungi informasi pribadi dan komunikasi digital. Dengan menggunakan teknik enkripsi, data sensitif seperti pesan, informasi keuangan, dan identitas pengguna dapat dilindungi dari pihak ketiga yang tidak sah. Enkripsi end-to-end memastikan bahwa hanya pengirim dan penerima yang dapat mengakses konten pesan, sehingga menjaga privasi individu dalam interaksi online. Ini sangat penting dalam konteks berbagai layanan digital, dari aplikasi perpesanan hingga transaksi bank, di mana keamanan dan privasi data adalah prioritas utama.

2. Tantangan Hukum:
   - Meskipun kriptografi mendukung privasi, ia juga menimbulkan tantangan hukum. Pemerintah dan lembaga penegak hukum sering kali menghadapi kesulitan dalam mengakses informasi yang terenkripsi saat menyelidiki kejahatan, terorisme, atau aktivitas ilegal lainnya. Ini menciptakan ketegangan antara perlindungan privasi individu dan kebutuhan untuk menjaga keamanan publik. Beberapa negara bahkan telah mengambil langkah-langkah untuk mendorong atau memaksa perusahaan teknologi untuk menyediakan "backdoor" dalam sistem enkripsi, sehingga memungkinkan akses yang lebih besar ke data yang aman.

3. antangan Etika:
   - Dari segi etika, penggunaan kriptografi menimbulkan pertanyaan tentang batasan antara privasi individu dan transparansi. Sementara kriptografi dapat melindungi data pribadi, ia juga bisa disalahgunakan oleh individu atau kelompok untuk tujuan yang tidak etis, seperti melakukan aktivitas kriminal. Diskusi etis berputar di sekitar sejauh mana privasi harus dilindungi, dan apakah ada justifikasi moral untuk memberikan pengecualian dalam hal akses ke data terenkripsi untuk kepentingan keamanan nasional atau publik.

### Kesimpulan

Dengan kata lain, kriptografi memainkan peran penting dalam melindungi privasi dalam komunikasi digital, namun juga menghadirkan tantangan signifikan di bidang hukum dan etika. Menciptakan keseimbangan yang tepat antara perlindungan privasi dan kebutuhan untuk keamanan publik tetap menjadi isu kompleks yang memerlukan dialog berkelanjutan antara pemangku kepentingan, termasuk pemerintah, organisasi, dan masyarakat umum.

### Kesimpulan

Kriptografi memainkan peran vital dalam mendukung privasi komunikasi digital dengan menyediakan mekanisme enkripsi yang melindungi data sensitif dari akses tidak sah. Dengan menggunakan teknik seperti enkripsi end-to-end, individu dapat menjaga kerahasiaan informasi pribadi mereka dalam berbagai konteks, dari transaksi keuangan hingga komunikasi sehari-hari. Perlindungan ini sangat penting di era digital yang semakin rentan terhadap kejahatan siber dan penyalahgunaan data, membangun kepercayaan di antara pengguna terhadap layanan online.

Namun, penggunaan kriptografi juga menghadapi tantangan hukum dan etika yang signifikan. Pemerintah dan lembaga penegak hukum sering kali berada di persimpangan antara menjaga keamanan publik dan menghormati privasi individu, yang memicu perdebatan tentang perlunya akses ke data yang terenkripsi untuk tujuan penyelidikan. Selain itu, aspek etis muncul ketika membahas kemungkinan penyalahgunaan kriptografi untuk aktivitas ilegal. Dengan demikian, menemukan keseimbangan yang tepat antara perlindungan privasi dan kepentingan keamanan tetap menjadi tantangan kompleks dalam konteks teknologi modern.
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
