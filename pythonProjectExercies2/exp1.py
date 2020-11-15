
def bolunenSayiBulma():

    min_sayi = int(input("min sayi: "))
    max_sayi = int(input("max sayi: "))
    bolunecek_sayi = int(input("bolenecek sayi: "))

    sayi = []
    for i in range(min_sayi,max_sayi+1):
        if i % bolunecek_sayi == 0:
            sayi.append(i)
    print(len(sayi))


bolunenSayiBulma()

