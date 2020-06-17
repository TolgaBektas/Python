#rasgele 4 işlemden birini soracak
#2 tane sayı vericek random bu işlemin sonucunu isteyecek doğruysa doğru yanlışsa yanlış yazacak
import random
import time
islemler=["Toplama","Çıkarma","Çarpma","Bölme"]
giris="""
#---------------------------------------------#
#---------------------------------------------#
#----------4 İşlemli Matematik Oyununa--------#
#-----------------Hoş Geldin------------------#
#---------------------------------------------#
#-----4 İşlemden Herhangi Biri çıkacak--------#
#----Ve Çıkan 2 Sayı İle İşlemi Yapacaksın----#
#---------Doğru Bilirsen Kazanırsın-----------#
#------------Ve Puan Kazanırsın---------------#
#-----------Virgüllü sonuç yoktur!------------#
#---------------------------------------------#
#---------------------------------------------#
"""

score=0
print(giris)
time.sleep(4)
while True:
    time.sleep(1.5)
    print("#---------------------------------------------#")
    randomIslem=random.choice(islemler)
    print("Verilen Sayılar ile Yapman Gereken İşlem:",randomIslem)
    time.sleep(3.5)
    print("Şimdi 2 sayı vereceğim ve",randomIslem,"yapacaksın")
    time.sleep(3)
    randSayi1=random.randint(1,100)
    randSayi2=random.randint(1,100)
    print("Sayıların:",randSayi1,"ve",randSayi2)
    time.sleep(2.5)
    print("Sayıları gördün işleme başla bakalım")
    time.sleep(1)
    sonuc=int(input("Sonuç nedir?: "))
    if randomIslem=="Toplama":
        randSonuc=int(randSayi1+randSayi2)        
        if sonuc==randSonuc:
            print("Doğru bildin!")
            time.sleep(1)
            score=score+1
            print("İyi Gidiyorsun!")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)
        else:
            print("Yanlış Bildin!")
            time.sleep(1)
            score=score-1
            print("Kötü Gidiyorsun")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)

    elif randomIslem=="Çıkarma":
        randSonuc=int(randSayi1-randSayi2)
        if sonuc==randSonuc:
            print("Doğru bildin!")
            time.sleep(1)
            score=score+1
            print("İyi Gidiyorsun!")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)
        else:
            print("Yanlış Bildin!")
            time.sleep(1)
            score=score-1
            print("Kötü Gidiyorsun")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)

    elif randomIslem=="Çarpma":
        randSonuc=int(randSayi1*randSayi2)
        if sonuc==randSonuc:
            print("Doğru bildin!")
            time.sleep(1)
            score=score+1
            print("İyi Gidiyorsun!")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)
        else:
            print("Yanlış Bildin!")
            time.sleep(1)
            score=score-1
            print("Kötü Gidiyorsun")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)
            
    elif randomIslem=="Bölme":        
        randSonuc=int(randSayi1/randSayi2)
        if sonuc==randSonuc:
            print("Doğru bildin!")
            time.sleep(1)
            score=score+1
            print("İyi Gidiyorsun!")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)
        else:
            print("Yanlış Bildin!")
            time.sleep(1)
            score=score-1
            print("Kötü Gidiyorsun")
            time.sleep(1)
            print("Skorun:",score)
            time.sleep(1)

   

    cikis=input("Devam etmek istiyor musun? (e/h)")
    if cikis=="e":
        time.sleep(1)
        continue
    else:
        break