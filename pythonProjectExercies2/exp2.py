

def sayiOkunusu(sayi):

     birler = ["", "bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
     onlar = ["", "on" , "yirmi","otuz", "kirk","elli","altmis","yetmis","seksen","doksan"]

     birler_basamak = sayi%10
     onlar_basamak = sayi//10

     print("okunusu: ", onlar[onlar_basamak],birler[birler_basamak])

def sayiAtama():

   ab = int(input("bir sayı giriniz: "))

   if 10<= ab <=99:
       sayi = ab
       sayiOkunusu(sayi)
   else:
       print("tekrar deneyiniz")
       sayiAtama()

sayiAtama()





