import os
import pyfiglet
import time
import csv
from tabulate import tabulate
from getpass import getpass

menu = "Menu.csv"
riwayat_file = "riwayat_transaksi.csv"
users = {
    "admin": "admin123",
    "kasir": "kasir123"
}

def animasi_teks(teks, delay=0.05):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print()

def login():
    print("\n=== Login ===")
    username = input("Username: ")
    password = getpass("Password: ")
    if username in users and users[username] == password:
        print(f"\n✅ Selamat datang, {username}!")
        Menu()
    else:
        print("❌ Login gagal. Username atau password salah.")
        login()

def Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    animasi_teks("\nSilahkan Pilih Menu")
    animasi_teks("1. Daftar Menu")
    animasi_teks("2. Pesan")
    animasi_teks("3. Cari Menu Berdasarkan Harga")
    animasi_teks("4. Cari Menu Berdasarkan Nama")
    animasi_teks("5. Urutkan Menu Berdasarkan Harga")
    animasi_teks("6. Urutkan Menu Berdasarkan Nama")
    animasi_teks("7. Lihat Riwayat Transaksi")
    animasi_teks("8. Filter Riwayat Transaksi Berdasarkan Tanggal")
    animasi_teks("9. Keluar")
    pilihan = input("Masukkan Pilihan (1-9): ")
    if pilihan == "1":
        baca_menu_dari_csv("Menu.csv")
        # tampilkan_menu()
    elif pilihan == "2":
        pesan()
    elif pilihan == "3":
        pencarian_menu_berdasarkan_harga()
    elif pilihan == "4":
        pencarian_menu_berdasarkan_nama()
    elif pilihan == "5":
        pengurutan_menu_berdasarkan_harga()
    elif pilihan == "6":
        pengurutan_menu_berdasarkan_nama()
    elif pilihan == "7":
        lihat_riwayat_transaksi()
    elif pilihan == "8":
        filter_riwayat_berdasarkan_tanggal()
    elif pilihan == "9":
        animasi_teks("Terima kasih telah menggunakan Broder Coffee!")
        exit()
    else:
        animasi_teks("Pilihan tidak valid. Silahkan pilih lagi.")
        Menu()

def baca_menu_dari_csv(nama_file="Menu.csv"):
    os.system('cls' if os.name == 'nt' else 'clear')
    global menu
    try:
        with open(nama_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            menu = [{"nama": row["nama"], "harga": int(row["harga"])} for row in reader]
            print("✅ Data menu berhasil dimuat dari file.")
    except FileNotFoundError:
        print("❌ File tidak ditemukan.")

def tampilkan_menu():
    if not menu:
        print("❌ Tidak ada data menu.")
        return
    tabel = [[i+1, item['nama'], f"Rp{item['harga']:,}"] for i, item in enumerate(menu)]
    print(tabulate(tabel, headers=["No", "Nama Menu", "Harga"], tablefmt="fancy_grid"))

def merge_sort_menu(data, ascending=True, key='harga'):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort_menu(data[:mid], ascending, key)
    right = merge_sort_menu(data[mid:], ascending, key)
    return merge(left, right, ascending, key)

def merge(left, right, ascending=True, key='harga'):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        a = left[i][key].lower() if isinstance(left[i][key], str) else left[i][key]
        b = right[j][key].lower() if isinstance(right[j][key], str) else right[j][key]
        if (a <= b and ascending) or (a > b and not ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def pencarian_menu_berdasarkan_harga():
    if not menu:
        print("❌ Menu kosong.")
        return
    try:
        min_harga = int(input("Masukkan harga minimum: "))
        max_harga = int(input("Masukkan harga maksimum: "))
        urutan = input("Urutkan (asc/desc): ").lower()
        ascending = urutan == "asc"
        menu_terurut = merge_sort_menu(menu, ascending)
        hasil = [item for item in menu_terurut if min_harga <= item['harga'] <= max_harga]
        if not hasil:
            print("❌ Tidak ada menu dalam range harga tersebut.")
        else:
            tabel = [[i+1, item['nama'], f"Rp{item['harga']:,}"] for i, item in enumerate(hasil)]
            print(tabulate(tabel, headers=["No", "Nama Menu", "Harga"], tablefmt="fancy_grid"))
    except ValueError:
        print("❌ Input harus berupa angka.")

def pencarian_menu_berdasarkan_nama():
    if not menu:
        print("❌ Menu kosong.")
        return
    keyword = input("Masukkan Nama Menu: ").lower()
    hasil = [item for item in menu if keyword in item['nama'].lower()]
    if not hasil:
        print("❌ Menu tidak ditemukan.")
    else:
        tabel = [[i+1, item['nama'], f"Rp{item['harga']:,}"] for i, item in enumerate(hasil)]
        print(tabulate(tabel, headers=["No", "Nama Menu", "Harga"], tablefmt="fancy_grid"))

def pengurutan_menu_berdasarkan_harga():
    urutan = input("Urutkan berdasarkan harga (asc/desc): ").lower()
    ascending = urutan == "asc"
    hasil = merge_sort_menu(menu, ascending, key='harga')
    tabel = [[i+1, item['nama'], f"Rp{item['harga']:,}"] for i, item in enumerate(hasil)]
    print(tabulate(tabel, headers=["No", "Nama Menu", "Harga"], tablefmt="fancy_grid"))

def pengurutan_menu_berdasarkan_nama():
    urutan = input("Urutkan berdasarkan nama (asc/desc): ").lower()
    ascending = urutan == "asc"
    hasil = merge_sort_menu(menu, ascending, key='nama')
    tabel = [[i+1, item['nama'], f"Rp{item['harga']:,}"] for i, item in enumerate(hasil)]
    print(tabulate(tabel, headers=["No", "Nama Menu", "Harga"], tablefmt="fancy_grid"))

def pesan():
    if not menu:
        print("❌ Menu kosong.")
        return
    tampilkan_menu()
    pesanan = []
    while True:
        try:
            nomor = int(input("Masukkan nomor menu (0 untuk selesai): "))
            if nomor == 0:
                break
            if 1 <= nomor <= len(menu):
                jumlah = int(input("Jumlah porsi: "))
                item = menu[nomor - 1]
                total = item['harga'] * jumlah
                pesanan.append({"nama": item['nama'], "jumlah": jumlah, "harga": item['harga'], "total": total})
            else:
                print("❌ Nomor tidak valid.")
        except ValueError:
            print("❌ Input harus angka.")
    if pesanan:
        total_harga = 0
        print("\n=== Struk ===")
        struk = []
        for i, item in enumerate(pesanan):
            struk.append([i+1, item['nama'], item['jumlah'], f"Rp{item['harga']:,}", f"Rp{item['total']:,}"])
            total_harga += item['total']
        print(tabulate(struk, headers=["No", "Menu", "Qty", "Harga", "Total"], tablefmt="fancy_grid"))
        print(f"\nTotal Bayar: Rp{total_harga:,}")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(riwayat_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for item in pesanan:
                writer.writerow([item['nama'], item['jumlah'], item['harga'], item['total'], timestamp])
        with open("struk_terakhir.txt", mode='w', encoding='utf-8') as struk_file:
            struk_file.write("=== STRUK PEMBELIAN ===\n")
            for item in struk:
                struk_file.write(f"{item[1]} x{item[2]} = {item[4]}\n")
            struk_file.write(f"\nTotal Bayar: Rp{total_harga:,}\nWaktu: {timestamp}\n")
        print("✅ Struk dicetak ke file 'struk_terakhir.txt'")

def lihat_riwayat_transaksi():
    try:
        with open(riwayat_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            if not data:
                print("📭 Riwayat transaksi kosong.")
                return
            tabel = [[i+1] + row for i, row in enumerate(data)]
            print(tabulate(tabel, headers=["No", "Nama", "Qty", "Harga", "Total", "Waktu"], tablefmt="fancy_grid"))
    except FileNotFoundError:
        print("📭 File riwayat belum ada.")

def filter_riwayat_berdasarkan_tanggal():
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    try:
        with open(riwayat_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader if row and tanggal in row[5]]
            if not data:
                print("❌ Tidak ada transaksi pada tanggal tersebut.")
            else:
                tabel = [[i+1] + row for i, row in enumerate(data)]
                print(tabulate(tabel, headers=["No", "Nama", "Qty", "Harga", "Total", "Waktu"], tablefmt="fancy_grid"))
    except FileNotFoundError:
        print("📭 File riwayat belum ada.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    judul = pyfiglet.figlet_format("BRODER COFFEE")
    for baris in judul.splitlines():
        animasi_teks(baris, delay=0.01)
    animasi_teks("Selamat Datang di BRODER COFFEE", delay=0.04)
    login()

main()
