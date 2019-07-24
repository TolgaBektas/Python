#---------------SÖZLÜKLER DICTIONARY LER -----------------------------



sozluk1={1:"Bir",2:"İki",3:"Üç",4:"Dört"} # anahtar kelimeler ile kullanılıyor 1 2 vb anahtar kelimedir
print(sozluk1)# index numarası yoktur anahtar kelime vardır
print(sozluk1[1])# Bir yazdırıyor
sozluk1[5]="Beş" #değer ekleme
print(sozluk1[5])

sozluk2={"bir":[1,2,3,4],"iki":[[1,2],[3,4],[5,6]],"üç":15}
print(sozluk2["iki"])

print(sozluk2["iki"][1][0]) # iki nin 1. indexinin 0. indexini yazdırır yani 3


#değer değiştirme 

sozluk2["üç"]=324423
print(sozluk2)

# ayni şeklide iç içe sözlükte oluşturabiliriz

print(sozluk1.keys()) # sadece anahtarlar çıkar
print(sozluk1.values())# değerleri gösterir

print(sozluk1.items()) # elemanları gösterir