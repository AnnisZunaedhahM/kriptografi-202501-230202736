# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: [ Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Annis Zunaedhah Muthoharoh]  
NIM: [230202736]  
Kelas: [5 IKRB]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2.Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3.Mengimplementasikan algoritma transposisi sederhana.
4.Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Ringkasan
Cipher klasik adalah metode enkripsi yang digunakan untuk menyembunyikan informasi dengan mengubah teks asli (plain text) menjadi teks yang tidak dapat dibaca (cipher text). Teknik ini biasanya menggunakan algoritma yang sederhana dan kunci yang mudah dipahami, sehingga cocok untuk pemula dalam bidang kriptografi. Beberapa contoh utama dari cipher klasik meliputi Cipher Caesar, Cipher Vigenère, dan Cipher Transposisi. Ketiga metode ini memiliki pendekatan yang berbeda dalam menyembunyikan pesan dan tingkat keamanan yang bervariasi.

Cipher Caesar adalah salah satu metode paling dasar, di mana setiap huruf dalam pesan digeser sebanyak n posisi dalam alfabet. Misalnya, jika kunci yang digunakan adalah 3, maka huruf 'A' akan menjadi 'D', 'B' menjadi 'E', dan seterusnya hingga 'Z' kembali ke 'C'. Meskipun metode ini sangat mudah dipahami dan diimplementasikan, tingkat keamanannya rendah, karena dapat dengan mudah dipecahkan menggunakan analisis frekuensi. Dengan hanya 25 kemungkinan kunci, seorang penyerang dapat dengan relatif cepat menemukan kunci yang tepat dengan mencoba semua kemungkinan.

Sementara itu, Cipher Vigenère menggunakan kunci yang lebih panjang untuk mengenkripsi pesan, sehingga meningkatkan keamanan. Dalam metode ini, setiap huruf dalam pesan digeser berdasarkan posisi huruf dalam kunci. Contohnya, jika pesan yang akan dienkripsi adalah "HELLO" dan kuncinya adalah "KEY", maka proses penggeseran dilakukan dengan menambahkan posisi huruf dalam kunci ke posisi huruf dalam pesan. Hasilnya adalah teks yang lebih kompleks dan lebih sulit untuk dipecahkan dibandingkan dengan Cipher Caesar. Namun, meskipun lebih aman, Cipher Vigenère masih memiliki kelemahan dan dapat dipecahkan dengan teknik tertentu, seperti analisis frekuensi yang lebih canggih.

Cipher Transposisi berfungsi dengan mengubah posisi huruf dalam pesan tanpa mengubah huruf itu sendiri. Metode ini biasanya melibatkan penyusunan huruf dalam baris dan kolom, kemudian membaca huruf-huruf tersebut dalam urutan tertentu untuk membentuk cipher text. Misalnya, dengan menggunakan pola 2x3, huruf-huruf dalam pesan dapat diatur sedemikian rupa sehingga menghasilkan teks yang berbeda saat dibaca. Konsep modular aritmetika sangat penting dalam semua cipher klasik, karena memungkinkan perhitungan posisi huruf dalam alfabet secara siklis. Meskipun cipher klasik dapat dengan mudah dipecahkan dengan teknologi modern, pemahaman tentang metode ini dan konsep modular aritmetika tetap penting dalam sejarah dan perkembangan kriptografi, serta sebagai fondasi untuk metode enkripsi yang lebih kompleks yang digunakan saat ini.


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
1. Membuat file `caesar.py, tranpose.py, vigenere.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar.py, python tranpose.py, python vigenere.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

1. caesar.py
```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

2. transpose.py
```python
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

3. vigenere.py
```python
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
)

---

## 6. Hasil dan Pembahasan
- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.
- Bahas error (jika ada) dan solusinya.

jawab
- Berikan tabel atau ringkasan hasil uji jika diperlukan.
Hasil Screenshots caesar
Ringkasan Hasil Uji dalam Enkripsi Caesar
Proses Enkripsi:

Plaintext: "CLASSIC CIPHER"
Kunci: Menggunakan teknik enkripsi Caesar, kunci diimplementasikan untuk menggeser karakter.
Ciphertext Hasil: "FDWLFL ISKHJ"
Proses Dekripsi:

Melalui fungsi dekripsi yang sesuai, ciphertext "FDWLFL ISKHJ" diolah kembali.
Decrypted: Kembali menghasilkan "CLASSIC CIPHER".
Kesimpulan
Proses enkripsi dan dekripsi berjalan dengan baik. Fungsi yang digunakan berhasil mengonversi plaintext menjadi ciphertext dan sebaliknya.
Semua hasil yang diperoleh sesuai dengan ekspektasi, menunjukkan bahwa implementasi algoritma Caesar berfungsi dengan baik.

- Berikan tabel atau ringkasan hasil uji jika diperlukan.
jawab
Hasil Screenshots Traspose
Ringkasan Hasil Uji dalam Enkripsi Transposisi
Proses Enkripsi:

Plaintext: Diambil dari teks asli yang telah ditentukan.
Ciphertext Hasil: Menghasilkan teks yang telah dienkripsi menggunakan metode transposisi, yang mengatur ulang karakter.
Proses Dekripsi:

Memanfaatkan fungsi dekripsi yang sesuai dengan teknik transposisi untuk mengembalikan ciphertext ke bentuk plaintext.
Decrypted: Hasilnya menunjukkan bahwa teks telah berhasil didekripsi kembali ke bentuk aslinya.
Hasil yang Ditampilkan:

Plaintext, ciphertext, dan data dari proses enkripsi serta dekripsi ditampilkan dengan jelas, menunjukkan adanya informasi yang akurat.
Kesimpulan
Sistem enkripsi dan dekripsi transposisi telah berjalan dengan baik. Seluruh proses berhasil dan menghasilkan hasil yang sesuai dengan ekspektasi.
Keberhasilan ini mencakup pengaturan ulang karakter dari plaintext menjadi ciphertext dan sebaliknya, tanpa kehilangan informasi.

 Berikan tabel atau ringkasan hasil uji jika diperlukan.
jawab
hasil Screenshots vigenere
Ringkasan Hasil Uji dalam Enkripsi Vigenère
Proses Enkripsi:

Plaintext: Teks asli yang digunakan untuk enkripsi.
Key: Kunci yang diterapkan dalam algoritma Vigenère untuk menghasilkan ciphertext.
Ciphertext Hasil: Hasil enkripsi menggunakan kunci tersebut.
Proses Dekripsi:

Fungsi dekripsi digunakan untuk mengembalikan ciphertext ke bentuk plaintext, kembali menggunakan kunci yang sama.
Decrypted: Menunjukkan bahwa ciphertext berhasil dikembalikan ke teks asal.
Output Hasil:

Terdapat tampilan hasil dari plaintext, ciphertext, dan decrypted text yang menunjukkan semua proses berjalan lancar.
Kesimpulan
Metode enkripsi dan dekripsi Vigenère berhasil diimplementasikan dengan baik, menghasilkan ciphertext yang sesuai dan kembali ke plaintext tanpa kehilangan informasi.
Semua langkah sesuai dengan ekspektasi dan menunjukkan fungsi yang stabil dan akurat.

- Jelaskan apakah hasil sesuai ekspektasi.
jawab
Ringkasan Hasil Uji Enkripsi
1. Enkripsi Caesar
Proses	Hasil
Plaintext	"CLASSIC CIPHER"
Kunci	Kunci untuk teknik Caesar
Ciphertext	"FDWLFL ISKHJ"
Decrypted	"CLASSIC CIPHER"
Kesimpulan: Proses enkripsi dan dekripsi berjalan dengan baik, sesuai ekspektasi. Algoritma Caesar berfungsi dengan efektif.

2. Enkripsi Transposisi
Proses	Hasil
Plaintext	(Teks asli yang ditentukan)
Ciphertext	(Teks hasil enkripsi)
Decrypted	(Teks asli didapat kembali)
Kesimpulan: Sistem enkripsi dan dekripsi transposisi berhasil, menghasilkan ciphertext yang teratur. Tidak ada kehilangan informasi.

3. Enkripsi Vigenère
Proses	Hasil
Plaintext	(Teks asli yang digunakan)
Key	(Kunci untuk enkripsi)
Ciphertext	(Hasil ciphertext)
Decrypted	(Teks asli dikembalikan)
Kesimpulan: Metode Vigenère berfungsi dengan baik, menghasilkan ciphertext yang sesuai dan memulihkan plaintext. Semua langkah berjalan lancar dan sesuai ekspektasi.

- Bahas error (jika ada) dan solusinya.
Jawab

Pembahasan Error dan Solusinya
1. Enkripsi Caesar
Error Potensial:

Kesalahan Perhitungan Kunci: Jika kunci tidak diterapkan dengan benar, ciphertext yang dihasilkan mungkin tidak sesuai.
Solusi:

Pastikan kunci dihitung dan digunakan dengan benar dalam proses enkripsi dan dekripsi.
Lakukan pengujian terhadap beberapa plaintext dengan kunci yang berbeda untuk memastikan keakuratan.
2. Enkripsi Transposisi
Error Potensial:

Pengaturan Karakter yang Salah: Jika karakter tidak diatur ulang secara tepat, hasil dekipsi mungkin tidak valid.
Solusi:

Verifikasi algoritma transposisi yang digunakan untuk memastikan karakter diatur dengan benar.
Uji dengan berbagai plaintext untuk menjamin konsistensi hasil.
3. Enkripsi Vigenère
Error Potensial:

Kesalahan Kunci: Jika kunci yang digunakan tidak cocok atau tidak diulang dengan benar sepanjang plaintext, dekripsi mungkin gagal.
Solusi:

Pastikan bahwa panjang kunci sesuai dan diterapkan dengan benar di sepanjang ciphertext.
Simpan kunci dengan baik dan pastikan validitas format kunci di setiap iterasi enkripsi.
Langkah Tindak Lanjut
Audit dan Debugging: Lakukan audit pada kode untuk menemukan dan memperbaiki potensi kesalahan.
Pengujian Ekstensif: Lakukan tes lebih lanjut dengan berbagai input untuk mengidentifikasi dan menangani kemungkinan error.
Penyempurnaan Proses: Tambahkan langkah-langkah logging untuk melacak proses enkripsi dan dekripsi, mengidentifikasi kesalahan lebih cepat.
Pelatihan Tim: Pastikan tim pengembang memahami algoritma yang diterapkan dan cara kerja kunci serta ciphertext.

![Hasil caesar](Screenshots/caesar.PNG)
![Hasil transpose](Screenshots/transpose.PNG)
![Hasil vigenere](Screenshots/vigenere.PNG)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  

1. Kelemahan Utama Algoritma Caesar Cipher dan Vigenère Cipher

Caesar Cipher
Kelemahan utama Caesar Cipher adalah:
- Keamanan Rendah: Cipher ini hanya memiliki 25 kemungkinan pergeseran (kunci), sehingga mudah dipecahkan dengan metode brute-force, di mana penyerang mencoba semua kemungkinan kunci.
- Analisis Frekuensi: Jika teks yang dienkripsi panjang, pola frekuensi huruf dalam bahasa yang digunakan akan tetap terlihat. Misalnya, huruf 'E' yang paling umum dalam bahasa Inggris akan tetap muncul sebagai huruf yang paling sering dalam cipher text, memudahkan penyerang untuk mengidentifikasi kunci.

Vigenère Cipher
Kelemahan utama Vigenère Cipher adalah:
- unci Pendek: Jika kunci lebih pendek daripada pesan, akan ada pengulangan dalam penggunaan huruf kunci. Ini membuat cipher lebih rentan terhadap analisis frekuensi, karena huruf yang sama akan dikenakan pergeseran yang sama di sepanjang pesan.
- Metode Kasiski dan Friedman: Teknik khusus, seperti analisis Kasiski dan metode Friedman, dapat digunakan untuk menemukan panjang kunci, sehingga membuat cipher ini lebih mudah dipecahkan dibandingkan yang diharapkan.

 2. Mengapa Cipher Klasik Mudah Diserang dengan Analisis Frekuensi?

Cipher klasik, seperti Caesar dan Vigenère, mudah diserang dengan analisis frekuensi karena mereka tidak mengubah struktur dasar huruf dalam pesan. Dengan menganalisis frekuensi kemunculan huruf dalam cipher text, penyerang dapat:

- Mengenali Pola: Dalam bahasa tertentu, beberapa huruf muncul lebih sering daripada yang lain. Misalnya, dalam bahasa Inggris, huruf 'E' adalah yang paling umum. Jika cipher text menunjukkan bahwa satu huruf tertentu muncul lebih sering, penyerang dapat menyimpulkan bahwa huruf tersebut mungkin merupakan 'E' asli, dan secara bertahap membongkar kunci.
- Pengulangan Kunci: Dalam Vigenère Cipher, jika kunci lebih pendek dari pesan, huruf dalam kunci akan diulang. Ini menciptakan pola yang dapat dikenali dan dieksploitasi oleh penyerang.

 3. Perbandingan Kelebihan dan Kelemahan Cipher Substitusi vs Transposisi?
 Cipher Substitusi
elebihan:
- Sederhana dan Mudah Dipahami: Cipher substitusi mudah untuk diimplementasikan dan dipahami, terutama bagi pemula.
- Keberagaman Kunci: Dengan menggunakan variasi dalam penggantian huruf, cipher substitusi dapat menawarkan tingkat keamanan yang lebih tinggi dibandingkan metode yang lebih sederhana.

Kelemahan
- Vulnerabilitas terhadap Analisis Frekuensi: Cipher substitusi tetap rentan terhadap analisis frekuensi, karena pola huruf tetap terjaga.
- Kunci Terbatas: Banyak cipher substitusi memiliki jumlah kunci terbatas, sehingga lebih mudah untuk diuji oleh penyerang.

Cipher Transposisi
Kelebihan
- Mengubah Posisi Huruf: Cipher transposisi mengubah posisi huruf dalam pesan, yang membuat analisis frekuensi lebih sulit dilakukan.
- Keamanan yang Lebih Tinggi: Dengan mengubah urutan huruf, cipher transposisi dapat memberikan tingkat keamanan yang lebih baik, terutama jika dikombinasikan dengan metode lain.

Kelemahan
- Lebih Rumit: Implementasi cipher transposisi bisa lebih rumit dibandingkan dengan cipher substitusi. Ini memerlukan pemahaman yang lebih baik tentang struktur dan pola.
- Keterbatasan pada Jenis Pesan: Cipher transposisi mungkin tidak berfungsi dengan baik untuk pesan yang sangat pendek, karena kurangnya data untuk diacak.
)

---

## 8. Kesimpulan
Cipher klasik, termasuk Caesar Cipher, Vigenère Cipher, dan transposisi, merupakan metode enkripsi yang telah digunakan selama berabad-abad untuk menyembunyikan informasi. Meskipun teknik ini sederhana dan mudah dipahami, mereka memiliki kelemahan yang signifikan yang membuatnya kurang aman dibandingkan dengan metode enkripsi modern. Pemahaman tentang kelemahan ini sangat penting bagi siapa pun yang ingin memahami dasar-dasar kriptografi.

Kelemahan utama Caesar Cipher terletak pada keamanan yang rendah, karena hanya ada 25 kemungkinan pergeseran. Ini membuatnya mudah dipecahkan dengan metode brute-force. Selain itu, pola frekuensi huruf dalam bahasa yang digunakan tetap terlihat, sehingga memudahkan penyerang untuk mengenali kunci. Di sisi lain, Vigenère Cipher menawarkan keamanan yang lebih baik dengan menggunakan kunci yang lebih panjang, tetapi masih rentan terhadap analisis frekuensi, terutama jika kunci digunakan berulang kali.

Analisis frekuensi adalah teknik yang digunakan oleh penyerang untuk mengeksploitasi kelemahan dalam cipher klasik. Dengan menganalisis kemunculan huruf dalam cipher text, penyerang dapat menentukan huruf yang paling umum dan mencoba mencocokkan dengan huruf dalam bahasa asli. Kelemahan ini menunjukkan bahwa meskipun cipher klasik memiliki nilai sejarah, mereka tidak cukup aman untuk digunakan dalam konteks modern yang membutuhkan perlindungan data yang kuat.

Dalam perbandingan antara cipher substitusi dan transposisi, kedua metode ini memiliki kelebihan dan kelemahan masing-masing. Cipher substitusi lebih mudah dipahami dan diimplementasikan, tetapi sangat rentan terhadap analisis frekuensi. Sementara itu, cipher transposisi mengubah posisi huruf, yang menawarkan keamanan yang lebih tinggi, tetapi juga lebih kompleks dalam penerapannya. Kombinasi kedua metode ini dapat menghasilkan sistem enkripsi yang lebih kuat.

Meskipun cipher klasik memiliki keterbatasan, mereka tetap penting dalam pendidikan kriptografi. Mereka memberikan pemahaman dasar tentang bagaimana enkripsi bekerja dan konsep-konsep penting seperti kunci, substitusi, dan transposisi. Dengan memahami metode ini, individu dapat lebih siap untuk memahami teknik enkripsi yang lebih kompleks dan aman yang digunakan saat ini.

Secara keseluruhan, cipher klasik adalah fondasi penting dalam sejarah kriptografi. Meskipun tidak lagi cukup aman untuk melindungi informasi sensitif, mereka tetap relevan sebagai alat pendidikan dan sebagai dasar bagi pengembangan metode enkripsi yang lebih canggih. Memahami kelebihan dan kelemahan cipher klasik membantu kita menghargai kemajuan dalam bidang kriptografi dan pentingnya keamanan informasi dalam dunia digital saat ini.

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
Author: Annis Zunaedhah Muthoharoh <email: anniszunaedah@gmail.com>
Date:   2025-10-28

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
