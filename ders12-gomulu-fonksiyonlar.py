#map() fonksiyonu
#parametre olarak ilk fonksiyon alır, for döngüsü ile üzerinde gezinebilenecek liste demet tipi şey ise 2. parametredir
#örnek map(fonksiyonAdi,UygulanakListe)
#son olarak map objesine dönüşür

def ikiCarp(x):
    return x*2

a=list(map(ikiCarp,[1,2,3,4,5,6,7,8,9])) #listedeki ögelere tek tek fonksiyonu uygular
print(a)

#istenilen sayıda liste gönderilebilir fakat o kadar fonksiyon eleman almalıdır (liste1icin,liste2icin)
#iki adet liste ve 2 adet eleman istenirse ilk eleman ilk listeden ikinci eleman ikinci lsiteden alınır


#reduce() fonksiyonu
from functools import reduce# fakat import etmemiz lazımdır
#parametre olarak ilk fonksiyon alır, daha sonrada liste veya demet vb veri tipini alır
#fonksiyondaki işlemi listenin ilk iki elemanında uygular çıkan sonuç ile 3. elemana geçer ve ugular 

def topla(x,y):
    return x+y
b=reduce(topla,[1,2,3,4,5,6,7,8,9])# 1 ile 2 yi topladı çıkan sonuç ile 3 üzerinde işlem yaptı
print(b)

def faktoriyel1(sayi1,sayi2):
    return sayi1*sayi2

redListe=[1,2,3,4,5]
red=reduce(faktoriyel1,redListe)# fonksiyonu 1 ile 2 arasında uyguladı çıkan sonuç ile 3e uyguladı
#tekrar çıkan sonuç ile 4e uyguladı tekrarrr çıkan sonuç ile 5 e uguladı ve tek değer döndü
print(red)




#filter fonksiyonu 
#filter(fonsiyon,liste) map ile aynı mantık fakat fonksiyonda dönen değer true ise listeye atar
#false ise listeye almaz 

def teksayi(sayi):
    return sayi%2==1

sayi20adet=range(1,20)# 1 ile 20 arası sayılar
filterFonks=list(filter(teksayi,sayi20adet))# fonksiyon tek sayıları bulur true değer döndürür
print(filterFonks) # çift sayılar false döneceği için filterFonks'un içine atılmaz 
#çünkü false değerler filter fonksiyonu ile listeye alınmaz değersizdir


#zip fonksiyonu
# iki listeyi birbirini gruplamaya yarıyor

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
c=list(zip(liste1,liste2))#eşlenmeyen fazla elemanı almıyor
print(c)

## Aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)

# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}
print(list(zip(sözlük1,sözlük2))) # Anahtarlar eşleşti.
print(list(zip(sözlük1.values(),sözlük2.values())))# Değerler eşleşti



#Enumerate Fonksiyonu
liste = ["Elma","Armut","Muz","Kiraz"]
print(list(enumerate(liste)))#her bir elememana index numarası atıyor ve demet haline getiriyor

liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):#liste demet olduğundan her demet te 2 eleman index,eleman
    if (index % 2 == 0):#index numarası 2 ye bölümünden kalan 0 ise yazdırır
        print("Eleman: ",eleman)


#all() fonksiyonu 
#bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.

liste = [True,False,True,False,True]
print(all(liste))
liste = [1,2,3,4,5]
print(all(liste))

#any() fonksiyonu
# bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
liste = [True,False,True,False,True]
print(any(liste))
liste = [0,0,0,0,0,0,0]
print(any(liste))