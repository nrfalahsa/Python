def tebak_angka():
	import random
	angka = random.randint(1, 10)
	maksimal_percobaan = 3
	total_percobaan = 0

	while total_percobaan < maksimal_percobaan:
		try:
			total_percobaan +=1
			tebakan = int(input("Masukan tebakan: "))

			if tebakan > angka:
				print("Tebakan terlalu besar")
			elif tebakan < angka:
				print("Tebakan terlalu kecil")
			else:
				print("Selamat tebakan benar!")
				input("Enter untuk lanjut")
				break

		except ValueError:
				total_percobaan -=1
				print("Tebakan bukan angka!")
	else:
		print("Kesempatan percobaan sudah habis!")
		print("Kamu kalah!!")
		input("Enter untuk lanjut")
					
def app_menu():
	while True:
		try:
			print("===== TEBAK ANGKA =====")
			print("1. Tebak Angka")
			print("2. Keluar")
			print("=======================")

			pilihan = int(input("Masukan pilihan: "))

			if pilihan == 1:
				tebak_angka()
			elif pilihan == 2:
				print("=== PROGRAM SELESAI ===")
				break
			else:
				print("Masukan pilihan yang valid!")

		except ValueError:
			print("Pilihan bukan angka!")
		except:
			print("\n=== PROGRAM SELESAI ===")
			break

app_menu()


