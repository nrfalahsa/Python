''' LIST (ARRAY) '''

# index dimulai dari 0

# List kosong
empty_arr = []

# List dengan angka
arr_num = [1, 2, 3, 4, 5]

# List dengan string
arr_str = ["Alice", "bob", "Charlie"]

# List campuran
arr_mix = ["Alice", 25, "Bob", 30]
print(arr_mix)

# Mengakses list dengan indeks
print(arr_mix[2]) # Bob (indeks 2)


''' MANIPULASI LIST '''

buah = ["Jeruk", "Apel", "Pisang", "Mangga", "Pir", "Delima"]

# Mengubah nilai indeks
buah[1] = "Jambu" # Apel menjadi Jambu
print(buah[1])	  # Jambu

# Menambah nilai di akhir 
buah.append("Anggur")
print(buah) # ['Jeruk', 'Jambu', 'Pisang', 'Mangga', 'Anggur']

# Menambah nilai dengan menentukan indeks
buah.insert(2, "Salak") # Menggeser indeks Pisang dan belakangnya
print(buah) # ['Jeruk', 'Jambu', 'Salak', 'Pisang', 'Mangga', 'Anggur']

# Menghapus berdasarkan nilai
buah.remove("Pir")
print(buah) # ['Jeruk', 'Jambu', 'Salak', 'Pisang', 'Mangga', 'Delima', 'Anggur']

# Menghapus paling akhir
buah.pop()
print(buah) # ['Jeruk', 'Jambu', 'Salak', 'Pisang', 'Mangga', 'Delima']

# Menghapus berdasarkan indeks
del buah[3]
print(buah) # ['Jeruk', 'Jambu', 'Salak', 'Mangga', 'Delima']

# Mengetahui panjang list
print(len(buah)) # 5 (dimulai dari 1)

# Menggabungkan list
satu = [1, 2, 3 , 4, 5]
dua = [6, 7, 8, 9, 10]

gabungan = satu + dua
print(gabungan)


''' LOOP DI LIST '''

banyak_planet = ["Merkurius", "Venus", "Bumi", "Mars"]
for planet in banyak_planet:
	print(planet)

	# Atau

for i in range(0, len(banyak_planet)):
	print(banyak_planet[i])


''' MENCARI NILAI DI LIST '''

if "Bumi" in banyak_planet:
	print("Ada Bumi")
else:
	print("Tidak ada Bumi")


''' TUPLE '''

# Tidak bisa diubah setelah dibuat
poin = (5, 10)
print(poin[0]) # Sama seperti list

# Untuk data yang tidak berubah
tanggal_lahir = (22, 4, 2008) # Tanggal, bulan, tahun
print("Tanggal lahir:", tanggal_lahir)

# Iterasi di tuple
for i in tanggal_lahir:
	print(i)

# Iterasi di tuple dengan indeks
for i in range(len(tanggal_lahir)):
	print(tanggal_lahir[i])


''' DICTIONARY (KAMUS) '''

siswa = {
	"nama": "Alice",
	"umur": 17,
	"Kelas": "12 Mipa"
}

print(siswa)

print(siswa["nama"]) # Alice

# Mengubah niai
siswa["umur"] = 16
print(siswa)

# Menghapus key-value
del siswa["Kelas"]
print(siswa)

# Mengiterasi keys
for key in siswa:
	print(key, siswa[key])

# Mengiterasi key-value pairs
for key, value in siswa.items():
	print(key, value)


''' SET (Himpunan) '''

# Tidak berurutan dan tidak bisa duplikat

sayur = {"timun", "kangkung", "kol"}

# Menambah elemen
sayur.add("wortel")
sayur.add("wortel") # akan diabaikan
print(sayur)

# Menghapus elemen
sayur.remove("kangkung")
print(sayur)

# Menampilkan elemen
for e in sayur:
	print(e)