print("hello")
#****BAZI MATEMATİK OPERATÖRLERİ*****
a1=5
b1=4
a1,b1=b1,a1 # kısa ve kolay yer değiştirme
a=4**2# 4 üzeri 2 yani üst alma
print(a)
kupKokAlma = 8 ** (1/3)#KÜP KÖKÜNÜ ALIR
print(kupKokAlma)
kokAlma=16**0.5 # sadece kökünü alır
print(kokAlma)
a1//b1 # dersek virgülli kısmı almaz 
abs(a1)# mutlak değer
a1**b1 # 5 üssü 4 yapar
pow(a1,b1)#üsteki ile aynı mantık
"""
çoklu yorum satırı

"""

"""
*****STRİNG ÖZELLİKLERİ******
"""
strYazi="Merhaba Zalim Dünya"
print(strYazi)
print(strYazi[0])# index numarası ile karakter 

# stringlerde index numarası ile değişiklik yapılmaz !!!!
#--------AYNI İŞLEMLER LİSTEDE DE GEÇERLİDİR--------------------------
print(strYazi[-1])#sondan başlar index numarası ile karakter 
print(strYazi[8:13])# 8. indexden başlar 12. index dahil alır !!!13. index alınmaz!!!!
print(strYazi[:13])# başlangıç indexi verilmez ise en baştan başlar
print(strYazi[8:])# verilen başlangıç indexinden son indexe kadar alır
print(strYazi[::2]) # 2şer 2şer atlayarak gider
print(strYazi[::-1])# tersten yazar 
print(strYazi[::-2])# tersten yazar 2şer 2 şer

isim="Tolga"
isim=isim+" Mert" # burda birleştirme ekleme yapar
print (isim)
print(len(strYazi))# string değerlerin kaç karakterden oluştuğunu ölçer

x="Merhaba"
y="Zalim"
z="Dünya"
print(x+y+z) #toplar yan yana yazar ama boşluk kendiliğinden eklenmez
print(y*3)#Zalim i 3 kere yazar


#-------string teki özel karakterler---------
#\n ve \t
print("Tolga\nBektaş")# bi alt satıra atar
print("Tolga\tBektaş")# tab tuşu kadar boşluk bırakır

# type() fonksiyonu
deger=333
print(type(deger))#degerin tipini yazdırır


#sep parametresi

print("tolga","bektaş",sep=".")# arasına gelmesini istediğin değeri yazar
print(12,345,4576,12,sep ="/")

print(*"Tolga")# her harfin arasına boşluk bırakır
print(*"Tolga",sep="/")#bıraktığı boşluklara slash ekler

#---------------İNPUT() FONKSİYONU-----------------


input("Lütfen Bir Sayı Giriniz:")# burda sadece kullanıcı sayı girer bir işlem yapamayız
a=input("Lütfen Bir Sayı Giriniz:")# fakat burda girilen değeri bir değişkene atarsak işlem yapabiliriz
print("Kullanıcının girdiği değer:",a) 
print(type(a))# input tan dönen değer daima string tir
b=int(input("Sayı giriniz!: ")) # burda girilecek değeri int e çevirdik
print(type(b))

# üç sayının toplamını alalaım
sayi1= int(input("Birinci Sayıyı Giriniz:"))
sayi2= int(input("İkinci Sayıyı Giriniz:"))
sayi3= int(input("Üçüncü Sayıyı Giriniz:"))
print("Toplamları: ",sayi1+sayi2+sayi3)
input()