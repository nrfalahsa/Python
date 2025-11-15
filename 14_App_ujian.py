def baca_soal():
	try:
		soal_asli = []
		with open("./File/soal.txt", "r") as soal:
			for line in soal:
				soal_asli.append(line.strip())

		import random
		random.shuffle(soal_asli)
	except FileNotFoundError:
		print("File tidak ditemukan!")

	soal_dict = {}
	opsi = ["A", "B", "C", "D"]
	benar = 0
	salah = 0

	for i in range(len(soal_asli)):
		try:
			split_soal = soal_asli[i].split("|")
			pertanyaan = split_soal[0]
			semua_jawaban = split_soal[1].split(",")
			jawaban_benar = semua_jawaban[0]
			random.shuffle(semua_jawaban)

			soal_dict[i + 1] = {}
			soal_dict[i + 1]["pertanyaan"] = pertanyaan
			soal_dict[i + 1]["jawaban_benar"] = jawaban_benar
			soal_dict[i + 1]["semua_jawaban"] = semua_jawaban
		except:
			print("Terjadi error")

	for i in range(0, 10):
		soal = soal_dict[i+1]
		pertanyaan = soal["pertanyaan"]
		jawaban_benar = soal["jawaban_benar"]

		print(f"No {i + 1}.", pertanyaan)

		for j in range(len(opsi)):
			semua_jawaban = soal["semua_jawaban"][j]
			print(opsi[j], ".", semua_jawaban)

		jawaban_pengguna = input("Pilihan: ").upper()

		index_pengguna = opsi.index(jawaban_pengguna)
		
		if soal["semua_jawaban"][index_pengguna] == jawaban_benar:
			benar += 1
			print("Jawaban Benar!!")
		else:
			salah += 1
			print("Jawaban Salah!!")
	nilai = benar/(benar+salah)*100
	print(nilai, "%")
baca_soal()