def sinav_notlari():
    vize1 = float(input("vize1: "))
    vize2 = float(input("vize2: "))
    final = float(input("final: "))

    v1 = (vize1 * 30) / 100
    v2 = (vize2 * 30) / 100
    fnl = (final * 40) / 100

    toplam_not = v1 + v2 + fnl

    if toplam_not >= 90:
        print("AA")
    elif toplam_not >= 85:
        print("BA")
    elif toplam_not >= 80:
        print("BB")
    elif toplam_not >= 75:
        print("CB")
    elif toplam_not >= 70:
        print("CC")
    elif toplam_not >= 65:
        print("DC")
    elif toplam_not >= 60:
        print("DD")
    elif toplam_not >= 55:
        print("FD")
    elif toplam_not < 55:
        print("FF")


sinav_notlari()
