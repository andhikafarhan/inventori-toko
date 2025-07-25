# -*- coding: utf-8 -*-
"""inventori_toko.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SRN44PCRwmm9L7Oo9JgAZkCYVASSafo7
"""

# =====================================
# Aplikasi Inventori Toko Sederhana
# Versi CLI tanpa penyimpanan file
# =====================================

# List untuk menyimpan data barang (sementara, tidak disimpan ke file)
inventori = []

# Fungsi: Menampilkan menu utama
def tampilkan_menu():
    print("\n=== MENU INVENTORI TOKO ===")
    print("1. Tambah Barang")
    print("2. Lihat Semua Barang")
    print("3. Cari Barang")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

# Fungsi: Menambahkan data barang baru ke list inventori
def tambah_barang():
    kode = input("Masukkan kode barang: ").strip()
    nama = input("Masukkan nama barang: ").strip()
    try:
        stok = int(input("Masukkan jumlah stok: "))  # input stok harus angka
        barang = {"kode": kode, "nama": nama, "stok": stok}  # simpan dalam dictionary
        inventori.append(barang)  # tambahkan ke list
        print("Barang berhasil ditambahkan!")
    except ValueError:
        print("Stok harus berupa angka!")  # jika input bukan angka

# Fungsi: Menampilkan semua barang di inventori
def tampilkan_semua():
    if not inventori:
        print("Inventori kosong.")
    else:
        print("\n--- Daftar Barang ---")
        for barang in inventori:
            print(f"{barang['kode']} - {barang['nama']} ({barang['stok']})")


# Fungsi: Mencari barang berdasarkan kode atau nama
def cari_barang():
    kata_kunci = input("Masukkan nama/kode barang: ").lower()
    ditemukan = False
    for barang in inventori:
        # cek apakah kata kunci ada di kode atau di nama
        if kata_kunci in barang["kode"].lower() or kata_kunci in barang["nama"].lower():
            print(f"{barang['kode']} - {barang['nama']} ({barang['stok']})")
            ditemukan = True
    if not ditemukan:
        print("Barang tidak ditemukan.")

# Fungsi: Mengubah jumlah stok barang berdasarkan kode
def update_stok():
    kode = input("Masukkan kode barang yang ingin di-update: ").strip()
    for barang in inventori:
        if barang["kode"] == kode:
            try:
                baru = int(input("Masukkan jumlah stok baru: "))
                barang["stok"] = baru
                print("Stok berhasil diupdate!")
                return
            except ValueError:
                print("Input tidak valid. Stok harus angka.")
                return
    print("Barang tidak ditemukan.")

# Fungsi: Menghapus barang berdasarkan kode
def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ").strip()
    for barang in inventori:
        if barang["kode"] == kode:
            inventori.remove(barang)
            print("Barang berhasil dihapus!")
            return
    print("Barang tidak ditemukan.")


# ----- Loop utama -----
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_barang()
        elif pilihan == "4":
            update_stok()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            print("Terima kasih! Keluar program.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()
