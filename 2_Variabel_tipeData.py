"""
Penamaan Variabel:

- Tidak boleh dimulai dengan angka
- Tidak boleh pakai tanda minus (-)
- Tidak boleh pakai keyword python (contoh: if)
- Tidak boleh ada spasi
"""

# Assignment dasar
nama_depan = "Nur"
nama_belakang = "Falah"
nama_lengkap = nama_depan + " " + nama_belakang
umur = 19
tinggi = 165.0
is_developer = True

# Multiple assignment
x = y = z = 8                       # Semua bernilai 8
a, b, c = 3, 4, 5                   # a = 3, b = 4, c = 5
id, username = 1024, "nrfalahsa"    # id = 1024, username = "nrfalahsa"

# Mengubah nilai variabel
skor = 90
skor = 100 

# Menggunakan variabel dalam print
print(skor)                         # 100
print("Nama saya ", nama_lengkap)   # Nama saya Nur Falah

# Input ke variabel
sisi_persegi = input("Masukan panjang sisi: ")  # Input menghasilkan string
luas_persegi = int(sisi_persegi)**3 # s^3       # int() --> mengubah string menjadi integer
print("Luas persegi: ", luas_persegi)



"""
Tipe Data:

- Integer (int)  --> Bilangan bulat
- Float          --> Bilangan desimal
- String (str)   --> Teks
- Boolean (bool) --> True/False
"""

''' INTEGER '''

# integer positif dan negatif
tahun = 2006
saldo = -50000
nol = 0

# Bilangan besar (python bisa simpan angka besar)
populasi_dunia = 7800000000
angka_besar = 123456789012345678901234567890


''' FLOAT '''

# Bilangan dengan koma
tinggi = 165.0
berat = 50.5
pi = 3.14159

# Notasi scientific
speed_of_light = 3e8    # 3 x 10^8 = 300.000.000 m/s
very_small = 1e-6       # 1 x 10^-6 = 0.000001


''' STRING '''

# Single quotes
provinsi = 'Yogyakarta'

# Double quotes
kota = "Jogja"

# Triple quotes (Multi-line)
kalimat = """Memahami konsep UI/UX dan
menerapkan pendekatan Design Thinking 
untuk menganalisis dan merancang ulang
antarmuka aplikasi Threads.
"""

# Kosong
empty_string = ""
another_empty = ''


''' BOOLEAN '''

# Hanya True/False
is_student = True
is_married = False


''' Mengecek Tipe Data '''

print(type(tahun))      # <class 'int'>
print(type(pi))         # <class 'float'>
print(type(provinsi))   # <class 'str'>
print(type(is_student)) # <class 'bool'>


''' Konversi Tipe Data '''

total = "100"
hasil = 150
int_total = int(total)
float_total = float(total)
str_hasil = str(hasil)
bool_hasil = bool(hasil) 
# hasil = n --> True; 
# hasil = 0 --> False; 
# hasil = -n --> True; 
# hasil = '' --> False; 
# hasil = 'abc'
