import csv
import datetime
import os
import pyfiglet
import time
from tabulate import tabulate

MENU_FILE = "menu.csv"
USER_FILE = "user.csv"
ORDER_FILE = "orders.csv"
RIWAYAT_FILE = "riwayat_transaksi.csv"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("BRODER COFFEE"))

def read_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def animasi_teks(teks, delay=0.01):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print()

def login():
    os.system("cls" if os.name == "nt" else "clear")
    animasi_teks(pyfiglet.figlet_format("BRODER COFFEE"))
    animasi_teks("Selamat datang di Broder Coffee", delay=0.05)
    animasi_teks("Silakan login untuk melanjutkan...", delay=0.05)
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("BRODER COFFEE"))
    animasi_teks("=== Login ===")
    users = read_csv(USER_FILE)
    username = input("Username: ")
    password = input("Password: ")
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\n✅ Login berhasil sebagai {user['role'].capitalize()}.\n")
            return user["role"]
    print("\n❌ Username atau password salah.\n")
    return None

# === ADMIN: CRUD MENU ===
def crud_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("BRODER COFFEE"))
    while True:
        menu = read_csv(MENU_FILE)
        print("\n=== CRUD MENU ===")
        print("1. Lihat Menu\n2. Tambah Menu\n3. Edit Menu\n4. Hapus Menu\n5. Kembali")
        pilihan = input("Pilih: ")

        if pilihan == '1':
            clear_screen()
            print("Daftar Menu:")
            tabel_menu = [[item['id'], item['nama'], f"Rp{item['harga']}"] for item in menu]
            print(tabulate(tabel_menu, headers=["ID", "Nama", "Harga"], tablefmt="fancy_grid"))
            input("Tekan Enter untuk kembali...")
            clear_screen()
        elif pilihan == '2':
            clear_screen()
            nama = input("Nama menu: ")
            harga = input("Harga: ")
            new_id = str(len(menu) + 1)
            menu.append({"id": new_id, "nama": nama, "harga": harga})
            write_csv(MENU_FILE, menu, ["id", "nama", "harga"])
            print("✅ Menu berhasil ditambahkan.")
            input("Tekan Enter untuk kembali...")
            clear_screen()
        elif pilihan == '3':
            clear_screen()
            print("Daftar Menu:")
            tabel_menu = [[item['id'], item['nama'], f"Rp{item['harga']}"] for item in menu]
            print(tabulate(tabel_menu, headers=["ID", "Nama", "Harga"], tablefmt="fancy_grid"))
            id_edit = input("ID menu yang akan diedit: ")
            for item in menu:
                if item["id"] == id_edit:
                    item["nama"] = input("Nama baru: ")
                    item["harga"] = input("Harga baru: ")
                    break
            write_csv(MENU_FILE, menu, ["id", "nama", "harga"])
            print("✅ Menu berhasil diedit.")
            input("Tekan Enter untuk kembali...")
            clear_screen()
        elif pilihan == '4':
            clear_screen()
            print("Daftar Menu:")
            tabel_menu = [[item['id'], item['nama'], f"Rp{item['harga']}"] for item in menu]
            print(tabulate(tabel_menu, headers=["ID", "Nama", "Harga"], tablefmt="fancy_grid"))
            id_hapus = input("ID menu yang akan dihapus: ")
            menu = [item for item in menu if item["id"] != id_hapus]
            write_csv(MENU_FILE, menu, ["id", "nama", "harga"])
            print("✅ Menu berhasil dihapus.")
            input("Tekan Enter untuk kembali...")
            clear_screen()
        elif pilihan == '5':
            break

# === ADMIN: CRUD PENGGUNA ===
def crud_pengguna():
    while True:
        clear_screen()
        print("\n=== CRUD Pengguna ===")
        print("1. Lihat Pengguna\n2. Tambah Pengguna\n3. Edit Pengguna\n4. Hapus Pengguna\n5. Kembali")
        pilihan = input("Pilih: ")
        users = read_csv(USER_FILE)

        if pilihan == '1':
            clear_screen()
            if users:
                table = [[u["username"], u["role"]] for u in users]
                print(tabulate(table, headers=["Username", "Role"], tablefmt="fancy_grid"))
            else:
                print("❌ Tidak ada pengguna.")
            input("Tekan Enter untuk kembali...")
            clear_screen()

        elif pilihan == '2':
            clear_screen()
            uname = input("Username: ")
            pwd = input("Password: ")
            role = input("Role (admin/kasir/user): ")
            users.append({"username": uname, "password": pwd, "role": role})
            write_csv(USER_FILE, users, ["username", "password", "role"])
            print("✅ Pengguna berhasil ditambahkan.")
            input("Tekan Enter untuk kembali...")
            clear_screen()

        elif pilihan == '3':
            clear_screen()
            table = [[u["username"], u["role"]] for u in users]
            print(tabulate(table, headers=["Username", "Role"], tablefmt="fancy_grid"))
            uname = input("Username yang akan diedit: ")
            for user in users:
                if user["username"] == uname:
                    user["password"] = input("Password baru: ")
                    user["role"] = input("Role baru: ")
                    break
            else:
                print("❌ Username tidak ditemukan.")
            write_csv(USER_FILE, users, ["username", "password", "role"])
            print("✅ Pengguna berhasil diedit.")
            input("Tekan Enter untuk kembali...")
            clear_screen()

        elif pilihan == '4':
            clear_screen()
            table = [[u["username"], u["role"]] for u in users]
            print(tabulate(table, headers=["Username", "Role"], tablefmt="fancy_grid"))
            uname = input("Username yang akan dihapus: ")
            new_users = [u for u in users if u["username"] != uname]
            if len(new_users) < len(users):
                write_csv(USER_FILE, new_users, ["username", "password", "role"])
                print("✅ Pengguna berhasil dihapus.")
            else:
                print("❌ Username tidak ditemukan.")
            input("Tekan Enter untuk kembali...")
            clear_screen()
        elif pilihan == '5':
            break

        else:
            print("❌ Pilihan tidak valid.")

# === KASIR: TRANSAKSI DAN RIWAYAT ===
def pesan_menu():
    clear_screen()
    menu = read_csv(MENU_FILE)
    pesanan = []
    if not menu:
        print("❌ Menu kosong.")
        return

    while True:
        tabel_menu = [[item['id'], item['nama'], f"Rp{item['harga']}"] for item in menu]
        print(tabulate(tabel_menu, headers=["ID", "Nama", "Harga"], tablefmt="fancy_grid"))
        pilih = input("Pilih ID menu ('selesai' untuk akhir): ").strip().lower()
        if pilih == "selesai":
            break
        item = next((m for m in menu if m["id"] == pilih), None)
        if item:
            jumlah = input("Jumlah: ")
            if jumlah.isdigit():
                pesanan.append({
                    "nama": item["nama"],
                    "harga": int(item["harga"]),
                    "jumlah": int(jumlah)
                })
                print(f"✅ {item['nama']} x{jumlah} berhasil ditambahkan.")
                time.sleep(1)
                clear_screen()
            else:
                print("❌ Jumlah harus angka.")
        else:
            print("❌ Menu tidak ditemukan.")

    if pesanan:
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(RIWAYAT_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for item in pesanan:
                writer.writerow([waktu, item["nama"], item["jumlah"], item["jumlah"] * item["harga"]])
        print("✅ Pesanan berhasil disimpan.\n")
        time.sleep(2)

def lihat_riwayat():
    clear_screen()
    try:
        with open(RIWAYAT_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.append([row[0], row[1], row[2], f"Rp{row[3]}"])
            
            if data:
                print("=== Riwayat Transaksi ===")
                print(tabulate(data, headers=["Nama", "Menu", "Jumlah", "Total"], tablefmt="fancy_grid"))
            else:
                print("❌ Belum ada riwayat transaksi.\n")
    except FileNotFoundError:
        print("❌ Belum ada riwayat transaksi.\n")

    input("\nTekan Enter untuk kembali...")

def cari_menu():
    clear_screen()
    tabel_menu = [[item['id'], item['nama'], f"Rp{item['harga']}"] for item in menu]
    print(tabulate(tabel_menu, headers=["ID", "Nama", "Harga"], tablefmt="fancy_grid"))
    menu = read_csv("menu.csv")
    if not menu:
        print("❌ Menu kosong.")
        return
    menu.sort(key=lambda x: x["nama"].lower())

    keyword = input("Cari menu: ").lower()
    low = 0
    high = len(menu) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        nama_menu = menu[mid]["nama"].lower()

        if keyword == nama_menu:
            print(f"{menu[mid]['nama']} - Rp{menu[mid]['harga']}")
            found = True
            break
        elif keyword < nama_menu:
            high = mid - 1
        else:
            low = mid + 1

    if not found:
        print("❌ Tidak ditemukan.")
        time.sleep(2)

def quick_sort(arr, key, ascending=True):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    if ascending:
        left = [x for x in arr[1:] if int(x[key]) < int(pivot[key])]
        right = [x for x in arr[1:] if int(x[key]) >= int(pivot[key])]
    else:
        left = [x for x in arr[1:] if int(x[key]) > int(pivot[key])]
        right = [x for x in arr[1:] if int(x[key]) <= int(pivot[key])]

    return quick_sort(left, key, ascending) + [pivot] + quick_sort(right, key, ascending)

def urutkan_menu():
    clear_screen()
    menu = read_csv(MENU_FILE)
    if not menu:
        print("❌ Menu kosong.")
        return
    print("1. Termurah ke Termahal\n2. Termahal ke Termurah")
    pilihan = input("Pilih: ")
    ascending = pilihan == "1"
    sorted_menu = sorted(menu, key=lambda x: int(x["harga"]), reverse=not ascending)
    for item in sorted_menu:
        print(f"{item['nama']} - Rp{item['harga']}")

# === MENU UTAMA ===
def main_menu():
    role = None
    while not role:
        role = login()

    while True:
        if role == "admin":
            clear_screen()
            print("\n=== Menu Admin ===")
            print("1. CRUD Menu\n2. CRUD Pengguna\n3. Logout")
            pilihan = input("Pilih: ")
            if pilihan == "1":
                crud_menu()
            elif pilihan == "2":
                crud_pengguna()
            elif pilihan == "3":
                break
        elif role == "kasir":
            clear_screen()
            print("\n=== Menu Kasir ===")
            print("1. Pesan Menu\n2. Lihat Riwayat\n3. Logout")
            pilihan = input("Pilih: ")
            if pilihan == "1":
                pesan_menu()
            elif pilihan == "2":
                lihat_riwayat()
            elif pilihan == "3":
                break
        elif role == "user":
            clear_screen()
            print("\n=== Menu User ===")
            print("1. Cari Menu\n2. Urutkan Menu\n3. Logout")
            pilihan = input("Pilih: ")
            if pilihan == "1":
                cari_menu()
            elif pilihan == "2":
                urutkan_menu()
            elif pilihan == "3":
                break

# === JALANKAN PROGRAM ===
if __name__ == "__main__":
    main_menu()
