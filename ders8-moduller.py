#modul.py adlı dosyayı buraya import edebiliriz ve içindeki verileri kullanabiliriz
import modul #bu şekilde edersek modul de ne varsa import eder
#üsteki gibi import edersek değişkeni çağırırken modul.ad olarak çağırmak zorundayız
#from modul import ad # bu şekilde sadece adı import ederiz #burda direk ad diye çalğırabiliriz

print(modul.ad)
print(modul.soyad)
print(modul.liste)

import random
a=random.random()# 0 ile 1 arası float değer döndürür random
print(a)

b=random.uniform(1,50)# ile 50 arası float random değer döndürür
print(b)


c=random.randint(1,50) # int değer döndürür
print(c)

d=random.randrange(1,50) # 1 ile 50 arası 50 dahil değil int 
print(d)

liste=range(0,50)
e=random.choice(liste)#listenin içinden random sayı seçer
print(e)

f=random.sample(liste,5)# 5 tane random sayi seçer
print(f)

import math #matematik işlemlerini daha kolay yapmamıza yarar


a=math.factorial(5)#faktoriyel alma
print(a)

b=math.pow(3,3) # 3ün 3 üstünü alır
print(b)

print(math.pi)

c=math.sqrt(16)# karekokünü hesaplar
print(c)

d=math.floor(3.8)#kendisinden küçük olan tam sayıya yuvarlar
print(d)

#cmd veya terminal ekranına pythonı çalıştırıp sonra modulu (kütüphaneyi) import edip örneğin dir(math)
#yazarsak tüm fonksiyonlarını yazar


#time modulu
import time
print(time.time())#pc toplam zaman
print(time.gmtime())#günümüz ama dandik artı yanlış saat
print(time.gmtime(0))# pc milat zamanı 1970 olarak
print(time.localtime())#orjinal pcnin zamanı
print(time.asctime())# tuple olarak vermez
print(time.strftime("%a"))#sadece günü verir kısa hali
#%A günün tam adı
#%b  ayın kısa adı
#%B ayın tam adı
#%c tam tarih ve saat
#%d sayı değeri olarak gün
#%m sayı değeri olarak ay
#%Y ile 2019 ün 19unu alır
#%y yılın tam hali
#%x tam tarih 
#%X tam saat


time.sleep(1)#1 saniye duracak

