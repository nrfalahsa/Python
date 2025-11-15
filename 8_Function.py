''' FUNCTION '''

def helloworld():
	print("Hello World")

helloworld()

# Function dengan parameter
def greeting(nama):
	print("Hai!", nama)
	print("Senang bertemu dengan anda")

# Memanggil function dengan argumen
greeting("Alice")

def luas_persegi_panjang(panjang, lebar):
	luas = panjang * lebar
	print("Luas persegi panjang:", luas)

luas_persegi_panjang(8, 3)

# Function dengan return value
def volume_bola(radius):
	pi = 3.14159
	volume = 4 / 3 * pi * radius**3
	return volume;

volumeBola = volume_bola(2)
print("Volume bola:", volumeBola, "cm^3")

# Default parameter
def tema(app, mode = "gelap"):
	result = f"{app} menggunakan mode {mode}"
	return result

print(tema("threads", "terang"))
print(tema("tiktok"))

def perkenalan(nama, umur, kota):
	print("nama:", nama)
	print("umur:", umur)
	print("asal:", kota)

# Potitional arguments (urutan harus sesuai)
perkenalan("Alice", 19, "Jakarta")

# Keyword arguments (urutan bebas)
perkenalan(umur = 18, kota = "Jogja", nama = "Falah")

# Kombinasi potitional dengan keyword arguments
perkenalan("Alice", kota = "Jakarta", umur = 19)

# Lokal variabel --> variabel yang ada di dalam function tidak bisa digunakan diluar

# Global variabel
nama_global = "Alice"

def nama():
	global nama_global # Untuk mengubah data variabel globel
	nama_global = "Nami" 

nama()
print(nama_global)

# Parameter dinamis
def cetak_list(*list):
	for item in list:
		print(item)

cetak_list(1, 2, 3, 4, 5)

def cetak_dict(**dict):
	for key, value in dict.items():
		print(f"{key}: {value}")

cetak_dict(nama = "Alice", umur = 19, kota = "Jakarta")