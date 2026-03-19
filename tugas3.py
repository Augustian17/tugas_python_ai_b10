# Tugas 3 - Coding: Python Basics
# 1 - Deklarasi Variabel dan Tipe Data

nama = "Augustian Gautama"
umur = 18
tinggi = 173.8
mahasiswa = True
jago = ["berenang", "bowling", "golf", "yapping"]

print(f"nama       : {nama}        (tipe: {type(nama).__name__})")
print(f"umur       : {umur}           (tipe: {type(umur).__name__})")
print(f"tinggi     : {tinggi}        (tipe: {type(tinggi).__name__})")
print(f"mahasiswa? : {mahasiswa}         (tipe: {type(mahasiswa).__name__})")
print(f"jago apa   : {jago}  (tipe: {type(jago).__name__})")


# 2 - Manipulasi String

nama = "Augustian Gautama"
filler = " Paling keren"
kalimat = nama + filler + "!"  # Penggabungan string

print(f"Gabungan string  : {kalimat}")
print(f"Panjang string   : {len(kalimat)} karakter")
print(f"Huruf besar      : {kalimat.upper()}")
print(f"Huruf kecil      : {kalimat.lower()}")
print(f"Nama dibalik     : {nama[::-1]}")
print(f"Ganti kata       : {kalimat.replace('Paling keren', 'Paling jago')}")


# 3 - Operasi Matematika Sederhana

angka1 = 25
angka2 = 7

print(f"Angka 1          : {angka1}")
print(f"Angka 2          : {angka2}")
print(f"Penjumlahan (+)  : {angka1 + angka2}")
print(f"Pengurangan (-)  : {angka1 - angka2}")
print(f"Perkalian   (*)  : {angka1 * angka2}")
print(f"Pembagian   (/)  : {angka1 / angka2:.2f}")
print(f"Bagi bulat  (//) : {angka1 // angka2}")
print(f"Sisa bagi   (%)  : {angka1 % angka2}")


# 4 - List dan Akses Elemen

buah = ["apel", "mangga", "jeruk", "pisang", "anggur"]

print(f"List awal        : {buah}")
print(f"Elemen pertama   : {buah[0]}")
print(f"Elemen terakhir  : {buah[-1]}")
print(f"Elemen ke-3      : {buah[2]}")

buah.append("durian")
print(f"\nSetelah append('durian')  : {buah}")

buah.remove("jeruk")
print(f"Setelah remove('jeruk')   : {buah}")

item_dihapus = buah.pop()
print(f"Setelah pop()             : {buah}")
print(f"Item yang dihapus (pop)   : {item_dihapus}")

print(f"Jumlah item sekarang      : {len(buah)}")


# 5 - Penggunaan Input dari User

nama_user = input("Masukkan nama Anda  : ")
umur_user = input("Masukkan umur Anda  : ")

print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
print(f"Senang berkenalan denganmu, {nama_user}! 👋")

