nama = "Falah"
umur = 19

# Menggabungkan variabel
pesan = "Nama saya " + nama + ", umur " + str(umur) # tipe data umur harus dikonversi menjadi str
print(pesan)

# Mengetahui panjang string (termasuk spasi)
print(len(pesan))

# Mengakses karakter
print(nama[0]) # F (karakter pertama)
print(nama[1]) # a (karakter kedua)
print(nama[2]) # l (Karakter ketiga)

print(nama[-1]) # h (karakter terakhir)
print(nama[-2]) # a (karakter kedua dari belakang)
print(nama[-3]) # l (karakter ketiga dari belakang)

# String Slicing
print(nama[0:3]) # Fal (index 0, 1, 2)
print(nama[1:4]) # ala (index 1, 2, 3)
print(nama[2:5]) # ls (index 2, 3, 4)

print(nama[:3]) # Fal (dari awal sampai index 2)
print(nama[2:]) # lah (dari index 2 sampai akhir)
print(nama[:])  # Falah (seluruhnya)

# String Methods (Fungsi String)
print(pesan.upper()) # NAMA SAYA FALAH, UMUR 19 (Semua menjadi huruf besar)
print(pesan.lower()) # nama saya falah, umur 19 (Semua menjadi huruf kecil)
print(pesan.title()) # Nama Saya Falah, Umur 19 (Semua awal kata menjadi huruf besar)
print(pesan.capitalize()) # Nama saya falah, umur 19 (Awal kalimat menjadi huruf besar)
print(pesan.strip()) # Nama saya Falah, umur 19 (Menghapus karakter kosong (seperti spasi) di awal dan akhir)
print(pesan.replace("Falah", "Halaf")) # Nama saya Halaf, umur 19 (Menimpa karakter)
print(pesan.count("Nama")) # 1 (Menghitung jumlah munculnya karakter)
print(pesan.find("saya")) # 5 (Mencari indeks awal karakter)

# Escape Charactes
kalimat = "Baris pertama\nBaris kedua"
print(kalimat)
# Baris pertama
# Baris kedua

data = "Nama:\tAlice\nUmur:\t25"
print(data) # Nama:   Alice
            # Umur:   25

path = "C:\\Users\\Alice\\Documents"
print(path) # C:\Users\Alice\Documents

kalimat1 = "Dia berkata \"Hello\" kepada saya"
print(kalimat1) # Dia berkata "Hello" kepada saya

kalimat2 = 'I\'m learning Python'
print(kalimat2) # I'm learning Python

# String Interpolation
profil = f"Hallo, nama saya {nama}, umur {umur}"
print(profil) # Hallo, nama saya Falah, umur 19

harga = 100000
jumlah = 3

total = f"Total: Rp {harga * jumlah:,}"
print(total) # Total: Rp 300,000

sapaan = f"Hallo {nama.upper()}!"
print(sapaan) # Hallo FALAH!