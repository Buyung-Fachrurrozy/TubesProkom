import tkinter as tk
from tkinter import messagebox, PhotoImage
import csv
from openpyxl import Workbook
import os
from PIL import Image, ImageTk, ImageDraw
os.environ["TCL_LIBRARY"] = r"C:\Program Files\Python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Program Files\Python313\tcl\tk8.6"

# Data menu makan dan minum dengan menu yang diperluas
menu_makan = {
    "GADO-GADO": 12000,
    "LOTEK": 12000,
    "KETOPRAK": 12000,
    "MAGELANGAN": 13000,
    "NASI GORENG": 11000,
    "BIAWAK GORENG": 75000,
    "SATE": 15000,
    "KARE": 10000,
    "SOTO": 10000,
    "BUBUR AYAM": 10000,
    "LELE": 12000,
    "KAKAP": 14000,
    "NILA": 14000,
    "AYAM": 13000,
    "TUMPANG": 10000,
    "TAHU TEK": 13000,
    "LONTONG KUPANG": 13000,
    "TIMLO": 10000,
    "BAKSO": 17000,
    "BANDENG": 13000
}

menu_minum = {
    "ES TEH": 3000,
    "ES JERUK": 4000,
    "ES KOPI": 4000,
    "ES SUSU": 4000,
    "ES NUTRISARI": 4000,
    "POP ICE": 4000,
    "MOJITO": 10000,
    "WAKA WAKA": 90000,
    "ES KOPYOR": 12000,
    "ES BUAH": 12000,
    "ES OYEN": 12000,
    "ES DAWET": 5000,
    "ENERGEN": 4000,
    "SODA GEMBIRA": 8000,
    "ES SIRUP": 4000,
    "SUSU SEGAR": 7000,
    "LEGEN": 15000,
    "ES DURIAN": 15000,
    "KOLAK": 10000,
    "PISANG IJO": 10000
}

# Dictionary untuk menyimpan entry fields
entry_fields = {}
# Menyimpan pesanan
pesanan = []

def validate_number(P):
    if P == "":
        return True
    try:
        int(P)
        return True
    except ValueError:
        return False

def buka_window_menu(menu_data, title, bg_image_path):
    def proses_pesanan():
        ada_pesanan = False
        for menu, entry in entry_fields.items():
            value = entry.get().strip()
            if value:
                try:
                    jumlah = int(value)
                    if jumlah > 0:
                        harga = menu_data[menu]
                        total = harga * jumlah
                        pesanan.append((menu, harga, jumlah, total))
                        ada_pesanan = True
                except ValueError:
                    messagebox.showerror("Error", f"Input tidak valid untuk {menu}")
                    return
        
        if ada_pesanan:
            messagebox.showinfo("Sukses", "Pesanan telah ditambahkan!")
            window_menu.destroy()
            tampilkan_pesanan()
        else:
            messagebox.showwarning("Peringatan", "Masukkan jumlah pesanan minimal satu menu!")


    # Membuat window baru dengan scrollbar
    window_menu = tk.Toplevel(window)
    window_menu.title(title)
    window_menu.attributes('-fullscreen', True)

    # Membuat canvas
    canvas = tk.Canvas(window_menu)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    
    # Menambahkan background
    bg_image_menu = Image.open("3.png")
    bg_image_menu = bg_image_menu.resize((canvas.winfo_screenwidth(), window_menu.winfo_screenheight()))
    bg_photo_menu = ImageTk.PhotoImage(bg_image_menu)

    # Membuat label untuk background
    bg_label_menu = tk.Label(canvas, image=bg_photo_menu)
    bg_label_menu.image = bg_photo_menu
    bg_label_menu.place(x=0, y=0, relwidth=1, relheight=1)

    # Menambahkan scrollbar
    scrollbar = tk.Scrollbar(window_menu, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Mengkonfigurasi canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Membuat frame dalam canvas
    frame_menu = tk.Frame(canvas) 
    canvas.create_window((0,0), window=frame_menu, anchor="nw")
    
    # Menambahkan background
    bg_image_menu = Image.open("6.png")
    bg_image_menu = bg_image_menu.resize((frame_menu.winfo_screenwidth(), frame_menu.winfo_screenheight()))
    bg_photo_menu = ImageTk.PhotoImage(bg_image_menu)

    # Membuat label untuk background
    bg_label_menu = tk.Label(frame_menu, image=bg_photo_menu)
    bg_label_menu.image = bg_photo_menu
    bg_label_menu.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_menu.lower()

    # Frame untuk entry dan tombol
    entry_frame = tk.Frame(frame_menu) #belakang menu
    entry_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=(50,0))
    
    # Menambahkan background
    bg_image_menu = Image.open("6.png")
    bg_image_menu = bg_image_menu.resize((entry_frame.winfo_screenwidth(), entry_frame.winfo_screenheight()))
    bg_photo_menu = ImageTk.PhotoImage(bg_image_menu)

    # Membuat label untuk background
    bg_label_menu = tk.Label(entry_frame, image=bg_photo_menu)
    bg_label_menu.image = bg_photo_menu
    bg_label_menu.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_menu.lower()
    
    # Konfigurasi grid entry_frame
    entry_frame.grid_columnconfigure(1, weight=1)
    
    # Validasi command vcmd
    vcmd = (window_menu.register(validate_number), '%P')
    
    # Membuat entry fields untuk setiap menu
    entry_fields.clear()
    for idx, (menu, harga) in enumerate(sorted(menu_data.items())):
        # Label menu
        label = tk.Label(entry_frame, text=f"{menu} - Rp{harga:,}", font=("Arial", 12), anchor="w", fg="#256b4a", bg="#fafaf0")
        label.grid(row=idx, column=0, sticky="w", pady=2)
    
        # Entry field
        entry = tk.Entry(entry_frame, width=10, font=("Arial", 12), validate='key', validatecommand=vcmd)
        entry.grid(row=idx, column=1, sticky="e", pady=2, padx=5)
        entry_fields[menu] = entry
    
        # Tombol Gambar
        btn_gambar = tk.Button(entry_frame, text="Lihat Gambar", font=("Arial", 10), command=lambda m=menu: tampilkan_gambar(m), bg="#256b4a", fg="#fafaf0")
        btn_gambar.grid(row=idx, column=2, pady=2)
        
    # Membuat Frame untuk Canvas Gambar
    frame_canvas_gambar = tk.Frame(frame_menu)
    frame_canvas_gambar.pack(padx=(60,0), pady=100)
    
    #Membuat Canvas untuk Menampilkan Gambar
    canvas_gambar = tk.Canvas(frame_canvas_gambar, width=350, height=350, highlightthickness=0, bg="#256b4a")
    canvas_gambar.pack(side=tk.RIGHT)
    
    #Variabel untuk Menyimpan Foto Gambar
    foto_gambar = None
    
    def tampilkan_gambar(menu):
        global foto_gambar
        try:
            # Lokasi file gambar
            image_path = r"D:\TubesProkom\images\{}.png".format(menu.lower().replace(' ', '_'))
            
            # Muat Gambar
            img = Image.open(image_path)
            
            # Resize Gambar Jika Perlu
            img = img.resize((350, 350))
            
            # Konversi ke Photoimage untuk Tkinter
            foto_gambar = ImageTk.PhotoImage(img)
    
            # Hapus Apapun yang Ada di Canvas Sebelumnya
            canvas_gambar.delete(tk.ALL)
            
            # Hitung posisi untuk menempatkan gambar di tengah canvas
            x_position = (canvas_gambar.winfo_width() // 2)
            y_position = (canvas_gambar.winfo_height() // 2)
           
            # Tampilkan Gambar di Canvas
            canvas_gambar.create_image(x_position, y_position, image=foto_gambar, anchor="center")
           
            # Simpan Referensi untuk Menghindari Garbages Collection
            canvas_gambar.image=foto_gambar
           
        except FileNotFoundError:
            canvas.create_text(100, 50, text="gambar tidak ditemukan!", font=('Arial', 12))
        
    # Frame untuk tombol
    button_frame = tk.Frame(frame_menu, bg="#fafaf0")
    button_frame.pack(pady=10, padx=(56,10))
    
    # Tombol Proses Pesanan
    btn_proses = tk.Button(button_frame, text="Proses Pesanan", font=("Arial", 12), 
                          command=proses_pesanan, bg="#256b4a",fg="#fafaf0")
    btn_proses.pack(side=tk.LEFT, padx=5)
    
    # Tombol Reset Input
    btn_reset = tk.Button(button_frame, text="Reset Input", font=("Arial", 12),
                         command=lambda: [entry.delete(0, tk.END) for entry in entry_fields.values()],
                         bg="#256b4a", fg="#fafaf0")
    btn_reset.pack(side=tk.LEFT, padx=5)

    # Tombol Simpan ke CSV
    btn_save_csv = tk.Button(frame_bottom, text="Simpan ke CSV", font=("Arial", 12), 
                         command=simpan_ke_csv, bg="#fafaf0", fg="#256b4a")
    btn_save_csv.pack(side=tk.LEFT, padx=5)


def hitung_total_pesanan():
    return sum(total for _, _, _, total in pesanan)

def buka_window_pembayaran():
    if not pesanan:
        messagebox.showwarning("Peringatan", "Belum ada pesanan untuk dibayar!")
        return
    
    def proses_pembayaran(metode):
        total = hitung_total_pesanan()
        
        if metode == "QRIS":
            messagebox.showinfo("Pembayaran QRIS", 
                              f"Silakan scan QR code untuk membayar\nTotal: Rp{total:,}")
        elif metode == "Transfer Bank":
            messagebox.showinfo("Pembayaran Transfer", 
                              "Silakan transfer ke:\nBank BNI: 1333475027\n"
                              f"a.n. Restoran Senang Gembira\nTotal: Rp{total:,}")
        elif metode == "Cash":
            messagebox.showinfo("Pembayaran Cash", 
                              f"Silahkan menuju ke kasir, total yang harus dibayar: Rp{total:,}")
        
        if messagebox.askyesno("Konfirmasi", "Apakah pembayaran sudah selesai?"):
            window_payment.destroy()
            reset_pesanan()
            messagebox.showinfo("Sukses", "Terima kasih atas kunjungan Anda!")

    # Membuat window pembayaran
    window_payment = tk.Toplevel(window)
    window_payment.title("Pembayaran")
    window_payment.attributes('-fullscreen', True)
    
    # Menambahkan background
    bg_image_payment = Image.open("5.png")
    bg_image_payment = bg_image_payment.resize((window_payment.winfo_screenwidth(), window_payment.winfo_screenheight()))
    bg_photo_payment = ImageTk.PhotoImage(bg_image_payment)

    # Membuat label untuk background
    bg_label_payment = tk.Label(window_payment, image=bg_photo_payment)
    bg_label_payment.image = bg_photo_payment
    bg_label_payment.place(x=0, y=0, relwidth=1, relheight=1)

    # Menampilkan total
    total = hitung_total_pesanan()
    tk.Label(window_payment, text=f"Total Pembayaran: Rp{total:,}", 
             font=("Arial", 14), bg="#256b4a", fg="#fafaf0").pack(pady=(120,40))
    
    # Membuat Canvas
    canvas = tk.Canvas(window_payment, width=100, height=200, bg="#fafaf0")
    canvas.pack(fill=tk.BOTH, expand=True, padx=400, pady=(0,10))

    # Menambahkan scrollbar vertikal
    scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Mengkonfigurasi canvas untuk scroll
    canvas.configure(yscrollcommand=scrollbar.set)

    # Membuat frame di dalam canvas untuk menampung daftar pesanan
    frame_list = tk.Frame(canvas, bg="#fafaf0")
    canvas.create_window((0, 0), window=frame_list, anchor="nw")

    # Menampilkan daftar pesanan
    tk.Label(frame_list, text="Detail Pesanan:", font=("Arial", 15, "bold"), bg="#fafaf0").pack(anchor="w", pady=(5,5))
    for item, harga, jumlah, total in pesanan:
        tk.Label(frame_list, text=f"• {item} ({jumlah} x Rp{harga:,}) = Rp{total:,}", 
                 font=("Arial", 12), bg="#fafaf0").pack(anchor="w")
        
    # Update ukuran frame dan scrollregion
    frame_list.update_idletasks() 
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Frame untuk metode pembayaran
    payment_frame = tk.Frame(window_payment, bg="#256b4a")
    payment_frame.pack(pady=(50,12))
    
    # Label metode pembayaran
    tk.Label(payment_frame, text="Pilih Metode Pembayaran:", bg="#256b4a", fg="#fafaf0",
             font=("Arial", 12, "bold")).pack(pady=(5,5))
    
    # Buttons untuk metode pembayaran dengan warna berbeda
    payment_methods = [
        ("QRIS", "QRIS", "#fafaf0"),
        ("Transfer Bank", "Transfer Bank", "#fafaf0"),
        ("Cash/Tunai", "Cash", "#fafaf0")
    ]
    
    for text, value, color in payment_methods:
        tk.Button(payment_frame, 
                 text=text,
                 font=("Arial", 12),fg="#256b4a",
                 command=lambda v=value: proses_pembayaran(v),
                 bg=color,
                 width=20,
                 height=2
                 ).pack(pady=2)

def tampilkan_pesanan():
    for widget in frame_pesanan.winfo_children():
        widget.destroy()
    
    total_harga = 0
    if pesanan:
        # Membuat frame dengan scrollbar untuk daftar pesanan
        canvas_pesanan = tk.Canvas(frame_pesanan, bg="#fafaf0")
        scrollbar_pesanan = tk.Scrollbar(frame_pesanan, orient="vertical",bg="#fafaf0", command=canvas_pesanan.yview)
        frame_list = tk.Frame(canvas_pesanan, bg="#fafaf0")

        canvas_pesanan.configure(yscrollcommand=scrollbar_pesanan.set)
        
        # Pack scrollbar dan canvas
        scrollbar_pesanan.pack(side="right", fill="y")
        canvas_pesanan.pack(side="left", fill="both", expand=True)
        
        # Membuat window di canvas
        canvas_pesanan.create_window((0,0), window=frame_list, anchor="nw")
        
        # Label header
        tk.Label(frame_list, text="Daftar Pesanan:", font=("Arial", 14, "bold"), bg="#fafaf0").pack(anchor="w", pady=(0,10))
        
        for idx, (item, harga, jumlah, total) in enumerate(pesanan):
            tk.Label(
                frame_list, 
                text=f"{idx+1}. {item} ({jumlah} x Rp{harga:,}) = Rp{total:,}", 
                font=("Arial", 12), bg="#fafaf0"
            ).pack(anchor="w")
            total_harga += total
            
        tk.Label(
            frame_list, 
            text=f"\nTotal Semua Pesanan: Rp{total_harga:,}", 
            font=("Arial", 14, "bold"), bg="#fafaf0"
        ).pack(pady=10)
        
        # Update scrollregion setelah menambahkan semua item
        frame_list.update_idletasks()
        canvas_pesanan.configure(scrollregion=canvas_pesanan.bbox("all"))
    else:
        tk.Label(frame_pesanan, text="Belum ada pesanan.", font=("Arial", 12),bg="#256b4a", fg="#fafaf0").pack()
        

def simpan_ke_csv():
    if not pesanan:
        messagebox.showwarning("Peringatan", "Belum ada pesanan untuk disimpan!")
        return

    # File CSV
    csv_file_path = "D:/TubesProkom/pesanan_restoran.csv"

    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Menulis header
        writer.writerow(["Menu", "Harga per Item", "Jumlah", "Total"])
        # Menulis data pesanan
        for item, harga, jumlah, total in pesanan:
            writer.writerow([item, harga, jumlah, total])
        
        # Menambahkan total keseluruhan
        writer.writerow([])
        writer.writerow(["Total Semua Pesanan", "", "", hitung_total_pesanan()])

    # File Excel
    excel_file_path = "pesanan_restoran.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Pesanan"

    # Menulis header
    ws.append(["Menu", "Harga per Item", "Jumlah", "Total"])
    # Menulis data pesanan
    for item, harga, jumlah, total in pesanan:
        ws.append([item, harga, jumlah, total])

    # Menambahkan total keseluruhan
    ws.append([])
    ws.append(["Total Semua Pesanan", "", "", hitung_total_pesanan()])

    # Menyimpan file Excel
    wb.save(excel_file_path)

    messagebox.showinfo(
        "Sukses",
        f"Pesanan berhasil disimpan ke file:\n- '{csv_file_path}'\n- '{excel_file_path}'"
    )


def reset_pesanan():
    global pesanan
    if messagebox.askyesno("Konfirmasi Reset", "Apakah Anda yakin ingin mereset semua pesanan?"):
        pesanan = []
        tampilkan_pesanan()

# Membuat jendela utama
window = tk.Tk()
window.title("Restaurant Order System")
window.attributes('-fullscreen', True)

# Mendapatkan Ukuran Layar
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Membuat Background
bg_image = Image.open("2.png")
bg_image = bg_image.resize((screen_width, screen_height))  
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame untuk tombol menu
frame_buttons = tk.Frame(window,bg="#256b4a")
frame_buttons.pack(pady=(200,0))

# Tombol Menu Makan
btn_makan = tk.Button(frame_buttons, text="Menu Makan", font=("Arial", 14), 
                      command=lambda: buka_window_menu(menu_makan, "Menu Makan"), 
                      width=20, bg="#fafaf0", fg="#256b4a")
btn_makan.pack(side=tk.LEFT, padx=5, anchor="nw")

# Tombol Menu Minum
btn_minum = tk.Button(frame_buttons, text="Menu Minum", font=("Arial", 14), 
                      command=lambda: buka_window_menu(menu_minum, "Menu Minum"), 
                      width=20, bg="#fafaf0", fg="#256b4a")
btn_minum.pack(side=tk.RIGHT, padx=5, anchor="nw")

# Frame Daftar Pesanan
frame_pesanan = tk.Frame(window, pady=10, bg="#fafaf0")
frame_pesanan.pack(after=frame_buttons, padx=100, pady=20, expand=True)
frame_pesanan.config(bg="#256b4a")
tampilkan_pesanan()

# Frame untuk tombol bawah
frame_bottom = tk.Frame(window, bg="#256b4a")
frame_bottom.pack(pady=10)

# Tombol Reset Pesanan
btn_reset = tk.Button(frame_bottom, text="Reset Pesanan", font=("Arial", 12), 
                      command=reset_pesanan, bg="#fafaf0", fg="#256b4a")
btn_reset.pack(side=tk.LEFT, padx=5)

# Tombol Pembayaran
btn_payment = tk.Button(frame_bottom, text="Pembayaran", font=("Arial", 12),
                       command=buka_window_pembayaran, bg="#fafaf0", fg="#256b4a")
btn_payment.pack(side=tk.LEFT, padx=5)

# Tombol Keluar
btn_keluar = tk.Button(window, text="Keluar", font=("Arial", 12), command=window.quit, bg="#fafaf0", fg="#256b4a").pack(pady=10)

# Menjalankan aplikasi
window.mainloop()