''' IF '''

# angka = int(input("Masukan angka: "))

# if angka > 0:
#     print("Angka positif")

# if angka < 0:
#     print("Angka negatif")

# if angka == 0:
#     print("Angka nol")


''' IF ELSE '''

# nilai = int(input("Masukan nilai: "))

# if nilai >= 60:
#     print("Anda lulus")
# else:
#     print("Anda tidak lulus")


''' ELIF '''

# if nilai >= 90:
#     print("Grade A")
# elif nilai >= 80:
#     print("Grade B")
# elif nilai >= 70:
#     print("Grade C")
# elif nilai >= 60:
#     print("Grade D")
# else:
#     print("Grade D")

# umur = int(input("Masukan umur: "))
# sim = input("Apakah punya sim? (ya/tidak): ").lower()

# if umur >= 17 and sim == "ya":
#     print("Boleh mengendarai motor")
# else:
#     print("Tidak boleh mengendarai motor")

''' NESTED IF '''

# username = input("Masukan username: ")
# password = input("Masukan password: ")

# if username == "admin":
#     if password == "12345":
#         print("Login berhasil")
#         print("Selamat datang Admin")
#     else:
#         print("Password salah")
# else:
#     print("Username tidak ditemukan")

''' MATCH CASE '''

# hari = input("Masukan nama hari: ").lower()

# match hari:
#     case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
#         print("Hari kerja")
#     case "sabtu" | "minggu" :
#         print("Hari libur")
#     case _:
#         print("Nama hari tidak valid")

''' TERNARY OPERATOR '''

data = int(input("Masukan angka: "))
hasil = "Positif" if data > 0 else "Non-positif"
print("Angka tersebut: ", hasil)