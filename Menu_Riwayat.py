import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from PIL import Image, ImageTk

os.environ["TCL_LIBRARY"] = r"C:\Program Files\Python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Program Files\Python313\tcl\tk8.6"

def muat_data():
    try:
        with open('riwayatpesanan.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "File riwayatpesanan.json tidak ditemukan!")
        return {'pesanan': []}
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Format file JSON tidak valid!")
        return {'pesanan': []}

def tampilkan_data():
    try:
        data = muat_data()
        
        print("Struktur Data JSON:", json.dumps(data, indent=2))
        
        for i in tree.get_children():
            tree.delete(i)
        
        pesanan_list = data.get('pesanan', []) if isinstance(data, dict) else data
        
        for pesanan in pesanan_list:
            waktu = pesanan.get('tanggal', pesanan.get('waktu_pemesanan', 'Waktu Tidak Diketahui'))
            detail_pesanan = pesanan.get('detail_pesanan', 
                                         pesanan.get('pesanan_makanan', []) + 
                                         pesanan.get('pesanan_minuman', []))
            metode_pembayaran = pesanan.get('metode_pembayaran', 'Metode Tidak Diketahui')
            status = pesanan.get('status', 'Belum Selesai')  # Default status
            
            for detail in detail_pesanan:
                menu = detail.get('menu', 'Menu Tidak Diketahui')
                jumlah = detail.get('jumlah', 0)
                total_harga = detail.get('total_harga', detail.get('harga_per_item', 0) * jumlah)
                
                tree.insert('', 'end', values=(
                    menu, 
                    jumlah, 
                    f"Rp{total_harga:,}", 
                    metode_pembayaran,
                    waktu,
                    status  # Menambahkan status ke dalam tampilan
                ))
    except Exception as e:
        import traceback
        print("Error Detail:", traceback.format_exc())
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def ubah_status():
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih pesanan yang ingin diubah statusnya!")
            return
        
        values = tree.item(selected_item, 'values')
        nama_menu, jumlah, harga, cara_pembayaran, waktu, status_sekarang = values
        
        # Toggle status
        status_baru = "Selesai" if status_sekarang == "Belum Selesai" else "Belum Selesai"
        
        data = muat_data()
        status_diubah = False
        
        for pesanan in data.get('pesanan', []):
            waktu_pemesanan = pesanan.get('tanggal') or pesanan.get('waktu_pemesanan')
            
            if waktu_pemesanan == waktu:
                pesanan['status'] = status_baru
                status_diubah = True
                break
        
        if status_diubah:
            with open('riwayatpesanan.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            
            # Update tampilan
            tree.set(selected_item, 5, status_baru)
            messagebox.showinfo("Sukses", f"Status pesanan berhasil diubah menjadi {status_baru}!")
        else:
            messagebox.showwarning("Peringatan", "Pesanan tidak ditemukan!")
            
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()

def hapus_data():
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return
        
        values = tree.item(selected_item, 'values')
        nama_menu, jumlah, harga, cara_pembayaran, waktu, status = values

        harga = harga.replace('Rp', '').replace(',', '')
        
        data = muat_data()
        data_dihapus = False
        
        pesanan_list = data.get('pesanan', []).copy()
        
        for pesanan in pesanan_list:
            waktu_pemesanan = pesanan.get('tanggal') or pesanan.get('waktu_pemesanan')
            
            if waktu_pemesanan == waktu:
                detail_list = pesanan.get('detail_pesanan', []).copy()
                
                for detail in detail_list:
                    if (detail.get('menu') == nama_menu and 
                        str(detail.get('jumlah')) == jumlah and 
                        str(int(detail.get('total_harga', 0))) == str(int(harga))):
                        
                        pesanan['detail_pesanan'].remove(detail)
                        data_dihapus = True
                        break
                
                if not pesanan.get('detail_pesanan'):
                    data['pesanan'].remove(pesanan)
        
        if data_dihapus:
            with open('riwayatpesanan.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            tree.delete(selected_item)
            messagebox.showinfo("Sukses", "Riwayat pesanan berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Data tidak ditemukan untuk dihapus!")
    
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()

root = tk.Tk()
root.title("Riwayat Pesanan")
root.attributes('-fullscreen', True)

bg_image_menu = Image.open("E:/Tugas Tugas Kuliah/KODINGAN/PYTHON/TUBES/7.png")
bg_image_menu = bg_image_menu.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg_photo_menu = ImageTk.PhotoImage(bg_image_menu)

bg_label_menu = tk.Label(root, image=bg_photo_menu)
bg_label_menu.image = bg_photo_menu
bg_label_menu.place(x=0, y=0, relwidth=1, relheight=1)

kolom = ("Nama Menu", "Jumlah", "Harga", "Cara Pembayaran", "Waktu Pemesanan", "Status")
tree = ttk.Treeview(root, columns=kolom, show='headings', height=10)

tree.column("Nama Menu", width=150, anchor='center')
tree.column("Jumlah", width=70, anchor='center')
tree.column("Harga", width=100, anchor='center')
tree.column("Cara Pembayaran", width=150, anchor='center')
tree.column("Waktu Pemesanan", width=200, anchor='center')
tree.column("Status", width=100, anchor='center')  # Kolom baru untuk status

for col in kolom:
    tree.heading(col, text=col)

tree.pack(pady=(250, 10))

tombol_muat = tk.Button(root, text="Muat Data", font=("Arial, 15"), bg="#fafaf0", fg="#256b4a", command=tampilkan_data)
tombol_muat.pack(pady=5)

tombol_status = tk.Button(root, text="Ubah Status", font=("Arial, 15"), bg="#fafaf0", fg="#256b4a", command=ubah_status)
tombol_status.pack(pady=5)

tombol_hapus = tk.Button(root, text="Hapus Data", font=("Arial, 15"), bg="#fafaf0", fg="#256b4a", command=hapus_data)
tombol_hapus.pack(pady=5)

btn_keluar = tk.Button(root, text="Keluar", font=("Arial", 15), command=root.quit, bg="#fafaf0", fg="#256b4a").pack(pady=5)

root.mainloop()