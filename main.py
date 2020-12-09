from geometry.bangundatar import BangunDatar
from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga

print('Menggunakan Object Oriented Programming')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(20, 2)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari kelas BangunDatar')
b1 = BangunDatar()
print(b1.info())
print(b1.hitung_luas())

#Polymorphism: kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_datar = [p1, s1]

print('\nPolymorphism')
for bangun_datar in daftar_bangun_datar:
    print(bangun_datar.info())

