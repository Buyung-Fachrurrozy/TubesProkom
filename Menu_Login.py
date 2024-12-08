import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
from PIL import Image, ImageTk, ImageDraw

os.environ["TCL_LIBRARY"] = r"C:\Program Files\Python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Program Files\Python313\tcl\tk8.6"

customer_data_file = "dataloginpelanggan.json"
orders_data_file = "riwayatpesanan.json"


def sistem_JSON(username=None, password=None):

    # Membuat file JSON jika belum ada
    if not os.path.exists(customer_data_file):
        with open(customer_data_file, 'w') as file:
            json.dump({}, file)

    if not os.path.exists(orders_data_file):
        with open(orders_data_file, 'w') as file:
            json.dump([], file)

    # Validasi login jika username dan password diberikan
    if username and password:
        with open(customer_data_file, 'r') as file:
            data = json.load(file)
        return data.get(username) == password

    # Jangan memunculkan pop-up pada pemanggilan awal
    return True


def show_customer_login():
    print("show_customer_login called")
    # Jendela login pelanggan
    window_customer_login = tk.Toplevel()
    window_customer_login.title("Login Pelanggan")
    window_customer_login.geometry("300x200")# Ukuran standar popup
    window_customer_login.configure(bg="#256b4a")

    frame = tk.Frame(window_customer_login, padx=20, pady=20, bg="#256b4a")
    frame.pack()

    tk.Label(frame, text="Username", bg="#256b4a", fg="#fafaf0").grid(row=0, column=0, sticky="w", pady=5)
    entry_username = tk.Entry(frame)
    entry_username.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Password", bg="#256b4a", fg="#fafaf0").grid(row=1, column=0, sticky="w", pady=5)
    entry_password = tk.Entry(frame, show='*')
    entry_password.grid(row=1, column=1, pady=5)

    def login_customer():
        username = entry_username.get()
        password = entry_password.get()
        if username.strip() and password.strip():  # Validasi input
            with open(customer_data_file, 'r') as file:
                data = json.load(file)
            if username in data and data[username] == password:
                messagebox.showinfo("Sukses", "Login berhasil!", parent=window_customer_login)
                window_customer_login.destroy()
                root.destroy()
                import tubes_prokomHUAAAAAAAAAAAAAAAAA
            else:
                messagebox.showerror("Error", "Username atau Password salah!", parent=window_customer_login)
        else:
            messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!", parent=window_customer_login)

    tk.Button(frame, text="Login", bg="#fafaf0", fg="#256b4a", command=login_customer, width=15).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(frame, text="Sign Up", bg="#fafaf0", fg="#256b4a", command=show_sign_up, width=15).grid(row=3, column=0, columnspan=2, pady=10)

    window_customer_login.transient(root)  # Jendela mengikuti root
    window_customer_login.grab_set()  # Fokus pada jendela ini


def show_sign_up():
    print("show_sign_up called")
    window_sign_up = tk.Toplevel()
    window_sign_up.title("Sign Up")
    window_sign_up.geometry("300x200")# Ukuran standar popup
    window_sign_up.configure(bg="#256b4a")

    frame = tk.Frame(window_sign_up, padx=20, pady=20, bg="#256b4a")
    frame.pack()

    tk.Label(frame, text="Username", bg="#256b4a", fg="#fafaf0").grid(row=0, column=0, sticky="w", pady=5)
    entry_sign_up_username = tk.Entry(frame)
    entry_sign_up_username.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Password", bg="#256b4a", fg="#fafaf0").grid(row=1, column=0, sticky="w", pady=5)
    entry_sign_up_password = tk.Entry(frame, show='*')
    entry_sign_up_password.grid(row=1, column=1, pady=5)

    def perform_signup():
        username = entry_sign_up_username.get()
        password = entry_sign_up_password.get()
        if username and password:
            with open(customer_data_file, 'r+') as file:
                data = json.load(file)
                if username in data:
                    messagebox.showwarning("Peringatan", "Username sudah terdaftar!", parent=window_sign_up)
                else:
                    data[username] = password
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    messagebox.showinfo("Sukses", "Pendaftaran berhasil!", parent=window_sign_up)
                    window_sign_up.destroy()
        else:
            messagebox.showwarning("Peringatan", "Username dan Password tidak boleh kosong!", parent=window_sign_up)

    tk.Button(frame, text="Sign Up", bg="#fafaf0", fg="#256b4a", command=perform_signup, width=15).grid(row=2, column=0, columnspan=2, pady=10)

    window_sign_up.transient(root)  # Jendela mengikuti root
    window_sign_up.grab_set()  # Fokus pada jendela ini


def chef_login():
    def verify_chef():
        username = entry_chef_username.get()
        password = entry_chef_password.get()

        if username == "kokikeren" and password == "prokomseru":
            messagebox.showinfo("Sukses", "Login berhasil sebagai koki!")
            root.destroy()  # Tutup jendela login
            import muatdata
            #subprocess.run(["python", "muatdata.py", "--show-orders"])  # Jalankan tubes_prokom untuk menampilkan pesanan
        else:
            messagebox.showerror("Error", "Username atau Password salah!")

    # Jendela login koki
    window_chef_login = tk.Toplevel()
    window_chef_login.title("Login Koki")

    frame = tk.Frame(window_chef_login, padx=20, pady=20, bg="#256b4a")
    frame.pack()

    tk.Label(frame, text="Username Koki", bg="#256b4a", fg="#fafaf0").grid(row=0, column=0, sticky="w", pady=5)
    entry_chef_username = tk.Entry(frame)
    entry_chef_username.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Password Koki", bg="#256b4a", fg="#fafaf0").grid(row=1, column=0, sticky="w", pady=5)
    entry_chef_password = tk.Entry(frame, show='*')
    entry_chef_password.grid(row=1, column=1, pady=5)

    tk.Button(frame, text="Login", bg="#fafaf0", fg="#256b4a", command=verify_chef, width=15).grid(row=2, columnspan=2, pady=10)

def show_orders():
    # Membuka file riwayat pesanan
    with open("riwayatpesanan.json", 'r') as file:
        orders = json.load(file)

    # Membuat jendela baru untuk menampilkan pesanan
    orders_window = tk.Toplevel()
    orders_window.title("Riwayat Pesanan")

    frame = tk.Frame(orders_window, padx=20, pady=20)
    frame.pack()

    tk.Label(frame, text="Daftar Pesanan:", font=("Arial", 12, "bold")).pack()

    # Menampilkan setiap pesanan dari file
    if orders:
        for i, order in enumerate(orders, start=1):
            tk.Label(frame, text=f"Pesanan #{i}", font=("Arial", 10, "bold")).pack(anchor="w")
            tk.Label(frame, text=f"- Makanan: {order['Makanan']}").pack(anchor="w")
            tk.Label(frame, text=f"- Jumlah Makanan: {order['Jumlah Makanan']}").pack(anchor="w")
            tk.Label(frame, text=f"- Minuman: {order['Minuman']}").pack(anchor="w")
            tk.Label(frame, text=f"- Jumlah Minuman: {order['Jumlah Minuman']}").pack(anchor="w")
            tk.Label(frame, text="").pack()  # Separator antar pesanan
    else:
        tk.Label(frame, text="Belum ada pesanan.").pack(anchor="w")

    tk.Button(frame, text="Tutup", command=orders_window.destroy).pack(pady=10)


# Fungsi untuk toggle fullscreen
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

# Fungsi untuk keluar dari fullscreen dengan ESC
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# GUI Utama
root = tk.Tk()
root.title("Restoran Wenakk")

# Menambahkan background
bg_image_menu = Image.open("1.png")
bg_image_menu = bg_image_menu.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg_photo_menu = ImageTk.PhotoImage(bg_image_menu)

# Membuat label untuk background
bg_label_menu = tk.Label(root, image=bg_photo_menu)
bg_label_menu.image = bg_photo_menu
bg_label_menu.place(x=0, y=0, relwidth=1, relheight=1)
bg_label_menu.lower()

# Mengatur fullscreen
root.attributes("-fullscreen", True)
root.bind("<F11>", toggle_fullscreen)  # Toggle fullscreen dengan F11
root.bind("<Escape>", exit_fullscreen)  # Keluar dari fullscreen dengan ESC

# Menggunakan grid untuk menempatkan elemen secara proporsional
main_frame = tk.Frame(root, padx=10, pady=10, bg="#256b4a")
main_frame.pack(pady=(400,200))

tk.Button(main_frame, text="Login Pelanggan", font="Arial, 15", bg="#fafaf0", fg="#256b4a", relief="flat", command=show_customer_login, width=20, height=2).grid(row=1, column=0, padx=10, pady=10)
tk.Button(main_frame, text="Login Koki", font="Arial, 15", bg="#fafaf0", fg="#256b4a", relief="flat",command=chef_login, width=20, height=2).grid(row=1, column=1, padx=10, pady=10)

root.mainloop()