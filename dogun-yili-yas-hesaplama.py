import time
def yilaGoreYas(yil):
    if yil>2020:
        print("Hata! 2020 yılındayız!")
    else:
        yas=2020-yil
        print(yas)
dogumYili=int(input("Dogum yılınız Nedir? "))
yilaGoreYas(dogumYili)

def yasaGoreYil(yas):
    if yas<=0:
        print("Hata! ")
    else:
        yil=2020-yas
        print(yil)
yasaGore= int(input("Yaşınız Nedir? "))
yasaGoreYil(yasaGore)
print(time.gmtime())