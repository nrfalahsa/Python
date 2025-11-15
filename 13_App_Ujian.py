def ambil_soal():
	soal_asli = []
	with open("./File/soal.txt") as file:
		for line in file:
			soal_asli.append(line.strip())
	return soal_asli

def ujian():
	import random

	soal_asli = ambil_soal()
	random.shuffle(soal_asli)

	opsi = ["A", "B", "C", "D"]

	for i in range (0, 10):
		data_soal = soal_asli[i].split("|")
		pertanyaan = data_soal[0]

		semua_jawaban = data_soal[1].split(",")
		jawaban_benar = semua_jawaban[0]
		random.shuffle(semua_jawaban)

		print(pertanyaan)

		for j in range(len(semua_jawaban)):
			print(opsi[j], ".", semua_jawaban[j])

		user_answer = input("Masukan jawaban: ").upper()
		user_answer_index = opsi.index(user_answer)

		if semua_jawaban[user_answer_index] == jawaban_benar:
			print("Benar")
		else:
			print("salah")

ujian()