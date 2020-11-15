

class Insan():
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return " Adi: {} \n Soyadi: {} \n Yasi: {} \n Ulke: {} \n Sehir: {} \n Yetenek: {}"\
            .format(self.ad,self.soyad,self.yas,self.ulke,self.sehir,self.yetenekler)

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


kisi1 = Insan("es","bzkl","24","tr","ist")
kisi1.yetenek_ekle("Python")
print(kisi1.kisi_bilgileri())