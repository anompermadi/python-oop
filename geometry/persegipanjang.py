from geometry.bangundatar import BangunDatar


class PersegiPanjang(BangunDatar):
    def __init__(self, p, l):
        #fungsi yang dipanggil pertama kali saat object dibuat
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah object dari persegi panjang dengan panjang {self.p} dan lebar {self.l}'

    def hitung_luas(self):
        return self.p * self.l