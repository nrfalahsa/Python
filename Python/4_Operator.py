# Operator Aritmatika
a = 10
b = 3

print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.333...

print(a // b) # 3 (Pembagian bulat (tanpa desimal))
print(a % b) # 1 (sisa 1 ketika 10 dibagi 3)
print(b**2) # 9 (3^2)

# Operator Assignment (Penugasan)
x = 21
print("x awal: ", x)

x += 4 # Sama dengan: x = x + 4
print("x setelah += 4: ", x) # 25

x = 21
x -= 5 # Sama dengan: x = x - 5
print("x setelah -= 5: ", x) # 16

x = 21
x *= 2 # Sama dengan: x = x * 2
print("x setelah *= 2: ", x) # 42

x = 21
x /= 7 # Sama dengan: x = x / 7
print("x setelah /= 7: ", x) # 3.0

x = 21
x //= 4 # Sama dengan: x = x // 4
print("x setelah //= 4: ", x) # 5

x = 21
x %= 6 # Sama dengan: x = x % 6
print("x setelah %= 6: ", x) # 3

# Operator Perbandingan

print(a > b)  # Lebih dari: True
print(a < b)  # Kurang dari: False
print(a >= b) # Lebih dari sama dengan: True
print(a <= b) # Kurang dari sama dengan: False
print(a == b) # Sama dengan: False
print(a != b) # Tidak sama dengan: True

nama1 = "Alice"
nama2 = "Bob"
nama3 = "Alice"

print(nama1 == nama2) # False
print(nama1 == nama3) # True
print(nama1 != nama2) # True

# Operator Logika
x = 15
print(x > 10 and x < 20) # True (Kedua kondisi benar)
print(x > 10 or x < 10)  # True (Salah satu kondisi benar)
print(not(x > 10))       # False (Kebalikan dari True)
print(not(x < 10))       # True (Kebalikan dari False)

# Operator String
str1 = "Hello"
str2 = "World"

print(str1 + " " + str2) # Hello World (Penggabungan string)
print(str1 * 3)          # HelloHelloHello (Pengulangan string)
print("lo" in str1)      # True (Pengecekan substring)
print("z" in str1)       # False (Pengecekan substring)
print("lo" not in str1)  # False (Pengecekan substring)
print("z" not in str1)   # True (Pengecekan substring)
