# Laporan Praktikum Kriptografi                                   
Minggu ke-: 01
Topik: CIA_intro.md 
Nama: annis zunaedhah muthoharoh
NIM:  230202736 
Kelas: [5 IKRB]  


SOAL:1 .Sejarah Kriptografi & Prinsip CIA Confidentiality
Langkah 1 — Ringkasan Sejarah Kriptografi
Kriptografi adalah ilmu menyamarkan pesan agar tidak dapat dibaca oleh pihak yang tidak berwenang. Perjalanan ilmu ini dapat dikelompokkan menjadi tiga era utama yang menunjukkan evolusi dari mekanisme fisik sederhana hingga algoritma matematika kompleks.
1. Era Kriptografi Klasik (Manual dan Fisik)
Pada era ini, enkripsi dilakukan tanpa bantuan mesin elektronik dan berfokus pada teknik substitusi (penggantian) atau transposisi (pengacakan posisi).
•	Caesar Cipher: Diciptakan oleh Julius Caesar. Ini adalah contoh sederhana dari sandi substitusi, di mana setiap huruf pada pesan diganti dengan huruf lain yang memiliki pergeseran posisi tetap pada alfabet.
•	Vigenère Cipher: Sandi yang lebih kuat daripada Caesar karena menggunakan kunci berupa kata (polyalphabetic). Penggantian huruf dilakukan berdasarkan huruf kunci, membuat frekuensi huruf sulit dianalisis dan lebih sulit dipecahkan.
2. Perkembangan Kriptografi Modern (Komputer dan Matematika)
Era ini dimulai ketika kriptografi dipublikasikan secara terbuka dan mulai memanfaatkan kekuatan komputer serta teori matematika yang rumit.
•	Kriptografi Kunci Simetris (Symmetric-Key): Menggunakan satu kunci yang sama untuk proses enkripsi (mengubah pesan asli menjadi sandi) dan dekripsi (mengembalikan sandi menjadi pesan asli).
o	Contoh: AES (Advanced Encryption Standard): Algoritma enkripsi simetris paling umum dan kuat yang digunakan saat ini untuk melindungi data in transit dan at rest.
•	Kriptografi Kunci Asimetris/Publik (Asymmetric/Public-Key): Menggunakan dua kunci yang berbeda dan saling berpasangan—Kunci Publik (disebarluaskan) untuk enkripsi, dan Kunci Privat (dirahasiakan) untuk dekripsi.
o	Contoh: RSA: Merupakan salah satu algoritma kunci publik tertua dan banyak digunakan untuk digital signature (tanda tangan digital) dan pertukaran kunci yang aman.
3. Evolusi menuju Kriptografi Kontemporer (Era Desentralisasi)
Kriptografi terus berevolusi, melampaui sekadar mengamankan komunikasi menjadi fondasi untuk sistem keuangan dan otentikasi baru.
•	Blockchain dan Cryptocurrency: Teknologi seperti Bitcoin dan Ethereum tidak akan ada tanpa kriptografi. Mereka menggunakan Fungsi Hash Kriptografi untuk menjamin integritas data dalam blok dan Kriptografi Kunci Publik untuk membuktikan kepemilikan aset tanpa perlu perantara (bank).
•	Kriptografi Pasca-Quantum: Saat ini, fokus penelitian beralih pada pengembangan algoritma baru yang tahan terhadap serangan dari komputer kuantum, yang secara teoritis mampu memecahkan sandi RSA dan ECC dalam hitungan detik

Soal 2 — Prinsip CIA Triad
CIA Triad (Confidentiality, Integrity, Availability) adalah tiga pilar fundamental yang membentuk kerangka kerja keamanan informasi. Untuk menganggap sebuah sistem aman, ketiga prinsip ini harus dipertahankan.
1. Confidentiality (Kerahasiaan)
Prinsip ini bertujuan untuk melindungi informasi dari akses yang tidak berhak atau pengungkapan kepada pihak yang tidak memiliki izin.
•	Analoginya: Sebuah surat tersegel di dalam amplop.
•	Tujuannya: Menjaga privasi data. Data sensitif (misalnya: kata sandi, catatan medis, strategi bisnis) harus tetap rahasia.
•	Mekanisme: Enkripsi (kriptografi), Penggunaan Password yang kuat, dan Otorisasi (membatasi akses berdasarkan peran pengguna).
2. Integrity (Integritas)
Prinsip ini bertujuan untuk memastikan bahwa informasi adalah akurat, lengkap, dan belum diubah oleh pihak yang tidak berhak selama penyimpanan, pemrosesan, atau transmisi.
•	Analoginya: Sebuah dokumen yang memiliki segel atau tanda tangan digital asli.
•	Tujuannya: Menjamin keutuhan data. Penerima harus yakin bahwa pesan yang diterima sama persis dengan pesan yang dikirim oleh sumber yang sah.
•	Mekanisme: Fungsi Hash (menciptakan "sidik jari" data untuk mendeteksi perubahan sekecil apa pun) dan Tanda Tangan Digital.
3. Availability (Ketersediaan)
Prinsip ini bertujuan untuk memastikan bahwa sistem dan sumber daya informasi dapat diakses dan digunakan oleh pengguna yang sah kapan pun mereka membutuhkannya.
•	Analoginya: Pintu bank yang selalu terbuka pada jam operasional.
•	Tujuannya: Menjamin keberlanjutan layanan. Kegagalan sistem atau serangan siber yang menyebabkan sistem down melanggar prinsip Ketersediaan.
•	Mekanisme: Hardware yang andal, Network bandwidth yang memadai, dan Rencana Pemulihan Bencana (Disaster Recovery Plan).

Jawaban Soal Quiz
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
Pendekatan Kunci
Kriptografi Klasik: Mengandalkan metode simetris, di mana kunci yang sama digunakan untuk enkripsi dan dekripsi. Contohnya termasuk metode Caesar dan Vigenère. Masalah utama adalah pengiriman kunci yang aman.
Kriptografi Modern: Menggunakan metode asimetris (kunci publik dan kunci privat). Ini memungkinkan pertukaran kunci yang aman tanpa memerlukan saluran komunikasi yang aman.
Keamanan
Kriptografi Klasik: Keamanan bergantung pada kerumitan algoritma dan panjang kunci. Banyak metode klasik telah dipecahkan dengan kemajuan dalam analisis matematika dan komputasi.
Kriptografi Modern: Mengandalkan prinsip matematika yang lebih kompleks seperti teori bilangan dan masalah matematis yang sulit, sehingga lebih sulit untuk dipecahkan bahkan dengan teknologi komputer yang canggih.
Penggunaan
Kriptografi Klasik: Terutama digunakan dalam situasi di mana komunikasi aman dapat dilakukan, seperti surat-menyurat rahasia.
Kriptografi Modern: Digunakan dalam berbagai aplikasi, termasuk transaksi keuangan online, komunikasi aman di internet, dan sistem identifikasi digital.Quiz Singkat
Jawaban Quiz
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
Claude Shannon dianggap sebagai bapak kriptografi modern. Karyanya pada tahun 1940-an, terutama dalam makalahnya yang berjudul "Communication Theory of Secrecy Systems," memperkenalkan konsep-konsep matematis yang menjadi dasar bagi keamanan komunikasi. Ia mengembangkan teori informasi yang menjelaskan cara mengukur dan mengelola informasi serta ketidakpastian dalam proses komunikasi. Shannon juga memperkenalkan ide tentang penggunaan kunci untuk enkripsi, yang menjadi dasar penting bagi banyak algoritma kriptografi modern.
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
Beberapa algoritma kunci publik yang populer digunakan saat ini adalah:
•	RSA (Rivest-Shamir-Adleman):
o	Dikenal sebagai salah satu algoritma kriptografi paling awal yang menggunakan kunci publik. RSA memungkinkan untuk enkripsi data dan pembuatan tanda tangan digital. Keamanannya didasarkan pada kesulitan memfaktorkan bilangan besar.
•	DSA (Digital Signature Algorithm):
o	Digunakan khusus untuk menghasilkan tanda tangan digital. DSA adalah bagian dari standar digital signature yang ditetapkan oleh NIST. Keamanannya berfokus pada masalah logaritma diskrit.
•	ECC (Elliptic Curve Cryptography):
o	Meningkatkan efisiensi kriptografi dengan menggunakan kurva eliptik. ECC menawarkan tingkat keamanan yang setara dengan RSA tetapi dengan ukuran kunci yang jauh lebih kecil, menjadikannya lebih efisien dalam penggunaan bandwidth dan kecepatan.
•	Diffie-Hellman:
o	Meskipun tidak secara langsung digunakan untuk enkripsi, ini adalah protokol yang memungkinkan dua pihak untuk berbagi kunci rahasia melalui saluran yang tidak aman. Ini merupakan dasar untuk banyak sistem kunci publik saat ini.
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
Perbedaan utama antara kriptografi klasik dan modern dapat dijelaskan sebagai berikut:
•	Metode Enkripsi:
o	Kriptografi Klasik: Menggunakan metode yang relatif sederhana, seperti substitusi dan transposisi. Contohnya, Caesar Cipher hanya menggeser huruf dalam alfabet, sedangkan Vigenère Cipher menggunakan kunci untuk menghasilkan teks yang lebih kompleks. Metode ini mudah dipecahkan dengan analisis frekuensi, di mana pola huruf dapat diidentifikasi.
o	Kriptografi Modern: Menggunakan algoritma yang jauh lebih kompleks dan matematis. Contoh algoritma modern seperti AES (Advanced Encryption Standard) menggunakan blok enkripsi yang rumit dan kunci yang panjang, membuatnya jauh lebih sulit untuk dipecahkan.
•	Kunci:
o	Kriptografi Klasik: Mengandalkan satu kunci rahasia untuk enkripsi dan dekripsi (symmetric key). Jika kunci tersebut bocor, seluruh sistem dapat dikompromikan.
o	Kriptografi Modern: Memperkenalkan konsep kunci publik (public key) dan kunci privat (private key). Dalam sistem ini, kunci publik dapat dibagikan secara terbuka, sementara kunci privat disimpan rahasia. Ini memungkinkan komunikasi aman tanpa perlu berbagi kunci rahasia secara langsung.
•	Keamanan:
o	Kriptografi Klasik: Keamanan tergantung pada kerahasiaan kunci dan metode yang digunakan. Banyak teknik klasik dapat dengan mudah dipecahkan dengan analisis statistik dan teknik kracking.
o	Kriptografi Modern: Dirancang untuk tahan terhadap berbagai serangan, termasuk serangan brute-force dan serangan berbasis analisis matematis. Keamanan algoritma modern sering kali dapat diuji dan dievaluasi secara matematis, sehingga lebih dapat diandalkan.
•	Aplikasi:
o	Kriptografi Klasik: Digunakan lebih untuk komunikasi militer dan diplomatik.
o	Kriptografi Modern: Diterapkan di berbagai bidang, termasuk keamanan internet, transaksi keuangan, dan perlindungan data pribadi.
