class Ogrenci:
    def __init__(self, ad, soyad, sinif):
        self.ad = ad
        self.soyad = soyad
        self.sinif = sinif


ogr1 = Ogrenci("es", "bzkl", 1)

print("Adi : ", ogr1.ad)
print("Soyadi : ", ogr1.soyad)
print("Sinifi :", ogr1.sinif)


class Soru:

    net=0
    puan=0

    dogru_sayisi = int(input("Dogru sayisi: "))
    yanlis_sayisi = int(input("Yanlis sayisi: "))

    def netsayisi(self):
        self.yanlis_sayisi += self.yanlis_sayisi / 4
        net = self.dogru_sayisi - self.yanlis_sayisi
        return net

    def hesapla(self):
        puan = self.netsayisi() * 10
        print("Puan: ", puan)


obj = Soru()
obj.hesapla()
