def penjumlahan():
	print("=== PROGRAM PENJUMLAHAN ===")
	try:
		angka1 = int(input("Masukan angka pertama: "))
		angka2 = int(input("Masukan angka kedua: "))
	except ValueError:
		print("Input bukan angka!")
	hasil = angka1 + angka2
	print("Hasil penjumlahan: ", hasil)
	input("Enter untuk lanjut")

def pengurangan():
	print("=== PROGRAM PENGURANGAN ===")
	try:
		angka1 = int(input("Masukan angka pertama: "))
		angka2 = int(input("Masukan angka kedua: "))
	except ValueError:
		print("Input bukan angka!")
	hasil = angka1 - angka2
	print("Hasil pengurangan: ", hasil)
	input("Enter untuk lanjut")

def perkalian():
	print("=== PROGRAM PERKALIAN ===")
	try:
		angka1 = int(input("Masukan angka pertama: "))
		angka2 = int(input("Masukan angka kedua: "))
	except ValueError:
		print("Input bukan angka!")
	hasil = angka1 * angka2
	print("Hasil perkalian: ", hasil)
	input("Enter untuk lanjut")

def pembagian():
	print("=== PROGRAM PEMBAGIAN ===")
	try:
		angka1 = int(input("Masukan angka pertama: "))
		angka2 = int(input("Masukan angka kedua: "))
	except ValueError:
		print("Input bukan angka!")
	hasil = angka1 / angka2
	print("Hasil pembagian: ", hasil)
	input("Enter untuk lanjut")

def app_menu():
	while True:
		try:
			print("=== PROGRAM KALKULATOR SEDERHANA ===")
			print("1. Penjumlahan")
			print("2. Pengurangan")
			print("3. Perkalian")
			print("4. Pembagian")
			print("5. Keluar")
			print("====================================")

			pilihan = int(input("Masukan pilihan: "))

			if pilihan == 1:
				penjumlahan()
			elif pilihan == 2:
				pengurangan()
			elif pilihan == 3:
				perkalian()
			elif pilihan == 4:
				pembagian()
			elif pilihan == 5:
				print("=== PROGRAM SELESAI ===")
				break
			else:
				print("Masukan pilihan yang valid!")
		except ValueError:
			print("Input bukan angka!")
		except:
			print("\n=== PROGRAM SELESAI ===")
			break

app_menu()
