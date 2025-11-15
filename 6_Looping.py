''' FOR LOOP'''

# Mencetak angka 0 sampai 4
for i in range(5):
	print(i)

# Mencetak angka 1 sampai 5
for i in range(1, 6):
	print(i)

# Mencetak "Hello" sebanyak 3 kali
for i in range(3):
	print("Hello")

# Menghitung mundur
for i in range(6, 0, -1):
	print(i)

nama = "Python"
for huruf in nama:
	print(huruf)

for huruf_2 in nama:
	print("-", huruf_2)


''' WHILE LOOP '''

# Mencetak angka 1 sampai 5
angka = 1
while angka <= 5:
	print(angka)
	angka += 1

# Mengulang sampai benar
password = ""
while password != "12345":
	password = input("Masukan password: ")
	if password != "12345":
		print("Password salah, coba lagi!")

print("Password benar!")


''' BREAK AND CONTINUE '''

# Break
secret_number = 8
while True:
	number = int(input("Masukan angka: "))
	if number == secret_number:
		print("Angka benar!")
		break # Menghentikan loop
	else:
		print("Angka salah, coba lagi!")

# Continue
for i in range(10):
	if i % 2 == 0:
		continue # Melanjutkan ke loop selanjutnya
	print(i, "angka ganjil")


''' LOOP ElSE '''

# for loop
kata = input("Masukan kata: ")
cari = input("Masukan huruf yang dicari: ")

for huruf in kata:
	if huruf == cari:
		print("Huruf", cari, "ditemukan!")
		break
else:
	print("Huruf", cari, "tidak ditemukan!")

# while loop
password_true = "py123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
	percobaan += 1
	password = input("Masukan password: ")
	if password == password_true:
		print("Login berhasil!")
		break
	else:
		print("Password salah! sisa", max_percobaan - percobaan, "kali percobaan")
else:
	print("Terlalu banyak percobaan gagal. Akses ditolak!")


''' NESTED LOOP '''

# Tabel perkalian
for i in range(1, 10):
	for j in range(1, 10):
		hasil = i * j
		print(i, "x", j, "=", hasil)
	print("==========")