''' TRY - EXCEPT '''

print("=== KALKULATOR SEDERHANA ===")

try:
	angka1 = int(input("Angka pertama: "))
	angka2 = int(input("Angka kedua: "))
	hasil = angka1 / angka2
	print("Hasil:", hasil)
except ZeroDivisionError: # Menangani error spesifik
	print("Tidak bisa dibagi 0")
except ValueError:
	print("Input bukan angka")
except: # Menangani jika tidak ada error spesifik
	print("Terjadi kesalahan di input pengguna")

print("=== PROGRAM SELESAI ===")

''' TRY - EXCEPT - ELSE - FINALLY '''

try:
	angka = int(input("Masukan angka: "))
except ValueError:
	print("Input bukan angka")
else: # Di eksekusi jika tidak error
	if angka > 0:
		print("Angka positif")
	else:
		print("Angka negatif")
finally: # Dieksekusi walaupun error
	print("Program selesai")