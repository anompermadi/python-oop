from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga

print('Use Object Oriented Programming')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(20, 2)
print(s1.info())
print(s1.hitung_luas())