# KELAS A, KELOMPOK 4, RESTO WENAAK
# Anggota Team:
1. I0324011, Ida Fatkhur Rohmah, IdaFatkhur
2. I0324039, Buyung Fachrurrozy Amrullah, Buyung-Fachrurrozy
3. I0324022, Rafeyfa Asyla Suryawan, Rafeyfa-Asyla

# Deskripsi Aplikasi Restoran Wenaak
Aplikasi Restoran Wenaak dapat diakses oleh pelanggan dan koki. Restoran menawarkan beragam pilihan makanan dan minuman yang dapat dipilih sesuai preferensi pelanggan. Melalui aplikasi ini, pelanggan dapat dengan mudah melihat, memilih, dan memesan menu berdasarkan kategori yang tersedia dan jumlah porsi yang diinginkan. Selain itu, aplikasi ini menyediakan berbagai metode pembayaran yang fleksibel dan praktis, memungkinkan pelanggan menyelesaikan transaksi dengan cepat dan nyaman. Bagi koki restoran, aplikasi ini berguna untuk melihat semua pesanan yang sudah ditambahkan oleh pelanggan sebelumnya. 

# Fitur-Fitur Aplikasi RESTORAN WENAAK
1. Login pengguna (pelanggan atau koki).
2. Jika Pelanggan, ditampilkan menu makanan dan minuman.
3. Gambar menu dan penambahan jumlah menu sesuai yang diinginkan pelanggan.
4. Daftar pesanan berupa menu yang dipilih dan total harganya.
5. Proses pembayaran, bisa dilakukan dengan QRIS, Transfer Bank, dan Tunai/Cash.
6. Data  pesanan pelanggan akan masuk ke dalam riwayat pesanan.
10. Jika Koki, akan ditampilkan riwayat pesanan berupa username, password, tanggal pemesanan, dan daftar pesanan milik Pelanggan.

# Library yang digunakan:
* tkinter
* openpyxl
* os
* JSON
* PIL
* datetime

# SiteMap Resto Wenaak
![SiteMap Resto Wenaak](https://github.com/user-attachments/assets/9e5b00d3-83b7-4339-bb20-cc686643dc13)

# Flowchart Resto Wenaak
![Flowchart Resto Wenaak](https://github.com/user-attachments/assets/f7115e91-4781-4c7c-8019-a129447a5cbf)

* Penjelasan:

Flowchart aplikasi Resto Wenaak menggambarkan alur kerja yang dimulai dari proses login hingga penyelesaian transaksi, baik bagi pelanggan maupun koki. Program diawali dengan login, di mana pengguna dapat memilih untuk masuk sebagai pelanggan atau koki. Jika pengguna memilih login sebagai pelanggan, mereka akan diberikan opsi untuk Sign Up atau login. Proses Sign Up akan menyimpan data username dan password ke dalam database, memungkinkan pelanggan untuk melanjutkan login.

Setelah berhasil login, pelanggan akan disajikan dengan pilihan menu makanan dan minuman yang dilengkapi dengan deskripsi, harga, dan gambar menu. Pelanggan dapat memilih menu makanan dan minuman sesuai dengan jumlah porsi yang diinginkan. Apabila pelanggan tidak memilih menu apapun, program akan menampilkan pesan "belum ada pesanan yang ditambahkan," yang mengharuskan pelanggan untuk memilih menu atau keluar dari aplikasi.

Setelah pelanggan menentukan pilihan menu, program akan menampilkan daftar pesanan beserta total harga. Pelanggan dapat melanjutkan ke proses pembayaran atau kembali memilih menu tambahan. Untuk pembayaran, aplikasi menyediakan beberapa metode, seperti transfer bank, QRIS, atau pembayaran tunai. Jika memilih QRIS, aplikasi akan menampilkan QR Code restoran. Apabila memilih transfer bank, nomor rekening restoran akan ditampilkan untuk transaksi. Jika pelanggan memilih pembayaran tunai, mereka diarahkan untuk menyelesaikan pembayaran di kasir. Semua data pesanan pelanggan, termasuk metode pembayaran, akan otomatis tersimpan ke dalam database setelah pelanggan mengonfirmasi pembayaran.

Apabila pengguna login sebagai koki, aplikasi akan menampilkan riwayat pesanan yang sudah dilakukan oleh pelanggan. Informasi ini mencakup data username, daftar pesanan, metode pembayaran, serta tanggal transaksi. Fitur ini membantu koki untuk memantau dan mengelola pesanan yang telah tercatat sebelumnya. 






