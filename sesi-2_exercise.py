nama = "Clairine"
usia = 15
tinggi = 170
print("Nama:", nama)
print("Usia:", usia)
print("Tinggi:", tinggi)

teks = "Python"
angka_bulat = 42
angka_desimal = 3.14
is_active = True
print(type(teks))
print(type(angka_bulat))
print(type(angka_desimal))
print(type(is_active))

nama_depan = "Ani"
nama_belakang = "Sari"
nama_lengkap = f"{nama_depan} {nama_belakang}"
print(nama_lengkap)

angka = 15
if angka % 2 == 0:
    print("Angka ini genap")
else:
    print("Angka ini ganjil")

#  For loop
print("For loop:")
for i in range(1, 6):
    print(i)

#  While loop
print("While loop:")
angka = 1
while angka <= 5:
    print(angka)
    angka += 1