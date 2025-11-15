''' FILE I/O '''

"""
Mode:
	1. r --> Read (Baca) --> Membaca file yang sudah ada
	2. w --> Write (Tulis) --> Menulis file baru atau menimpa file lama
	3. a --> Append (Tambah) --> Menambah data di akhir file
	4. x --> Create (Buat) --> Membuat file baru, eror jika sudah ada
"""

print("=== SIMPAN DATA NILAI ===")

file = open("./File/nilai_siswa.txt", "w")

while True:
	nama = input("Nama siswa (enter untuk selesai): ")
	if nama == "":
		break

	nilai = input("Nilai: ")

	# Tulis ke file
	file.write(nama + ", " + nilai + "\n")
	print("Data", nama, "berhasil disimpan!")

file.close()
print("Semua data berhasil disimpan ke nilai_siswa.txt")

# With open --> otomatis close file
print("=== MENAMPILKAN DATA NILAI ===")

try:
	with open("./File/nilai_siswa.txt", "r") as file:
		for line in file:
			data = line.strip().split(", ")
			print(data[0], ":", data[1])
except FileNotFoundError:
	print("File tidak ditemukan")

print("=== PROGRAM SELESAI ===")

