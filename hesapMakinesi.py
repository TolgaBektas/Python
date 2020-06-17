# -*- coding: utf-8 -*-
toplama=0
cikarma=0
bolumu=0
carpimi=0
liste=[]
print("Öncelikle Merhaba!")
print("Benim Adım Hesap Makinesi")
print("Senin İçin Sayılar ile 4 işlem yapabilirim!")
cevap=input("Yapalım mı? (Y/N)")
if (cevap=="Y"):
   print("O zaman başlayalım!")
   adet=int(input("Kaç adet sayı ile işlem yapalım? "))
   if adet<=1:
       print("Tek bir sayıyla ne yapabilirim ki ?")
       quit()
   print(adet,"Tane Sayı Gireceksin!")
   sayi=0

   while sayi< adet:
       liste.append(input("Sayıyı gir: "))
       sayi+=1
else:
    print("Keyfin bilir paşam...")
islem=input("İşleminiz Nedir? (+ - * /)")

#-------------------------------TOPLAMA İŞLEMİ-------------------------------
if islem=="+":
    index=0
    sayiTas=1
    while sayiTas<= adet:
        toplama=toplama+int(liste[index])
        index=index+1
        sayiTas=sayiTas+1
    print("Toplamı= ",toplama)

#-------------------------------ÇIKARMA İŞLEMİ-------------------------------
elif islem=="-":
    index=1
    sayiTas=1
    cikarma=liste[0]
    int(cikarma)
    while sayiTas<= adet:
        cikarma=cikarma-int(liste[index])
        index=index+1
        sayiTas=sayiTas+1
    print("Farkı= ",cikarma)

#--------------------------------BÖLME İŞLEMİ--------------------------------
elif islem=="/":
    index=0
    sayiTas=1
    while sayiTas<= adet:
        bolumu=bolumu/int(liste[index])
        index=index+1
        sayiTas=sayiTas+1
    print("Bölümü= ",bolumu)

#-------------------------------ÇARPMA İŞLEMİ--------------------------------
elif islem=="*":
    index=0
    sayiTas=1
    while sayiTas<= adet:
       carpimi=carpimi*int(liste[index])
       index=index+1
       sayiTas=sayiTas+1
    print("Çarpımı= ",carpimi)
else:
    print("4 tane işlem var başka yok bende :(")
