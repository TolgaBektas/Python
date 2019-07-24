#Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veritipidir. 
#Bu açıdan kullanıldıkları yerlerde çok önemli bir veritipi olmaktadırlar.

x =  set() # Boş küme
print(type(x))
liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste) # Veri tipi dönüşümü
print(x)# Aynı elemanlar tek bir elemana indirgendi.

x = {"Python","Php","Java","C","Javascript"}
for i in x:
    print(i) 


#bir kümenin elemanlarına ne indexle ne de eleman ismiyle erişebiliyoruz. 
#Erişmek için mutlaka veritipi dönüşümü yapmamız gerekiyor.
a=list(x)
print(a)

#Kümelerin Metodları


#Eleman Eklemek : add() metodu

#Kümeye eleman eklemimizi sağlar. 
#Aynı eleman eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz.
x = {1,2,3}
x.add(4)
print(x)

#İki kümenin farkı : difference() metodu
#Bu metod birinci kümenin ikinci kümeden farkını döner.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.difference(kume2))
print(kume2.difference(kume1))
print("################################")
print(kume1,kume2)
#İki kümenin farkı ve güncelleme : difference_update() metodu

#Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.

kume1.difference_update(kume2)
print(kume1)
print(kume2)


#Kümeden Eleman Çıkartmak : discard() metodu
#İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).

kume1 = {1,2,3,4,5,6}
kume1.discard(2)
print(kume1)

#Küme kesişimleri : intersection() metodu
#Bu metod iki kümenin kesişimleri bulmamızı sağlar.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.intersection(kume2))


#Küme kesişimleri ve güncelleme : intersection_update() metodu
#Bu metod birinci kümeyle ikinci kümenin kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller.

kume1.intersection_update(kume2)
print(kume1)


#Kümeler ayrık küme mi ? : isdisjoint() metodu

#Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner. # ortak yok ise true var ise false

kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume3 = {30,40,50}

print(kume1.isdisjoint(kume2))
print(kume1.isdisjoint(kume3))

#Alt kümesi mi ? : issubset() metodu
#Bu metod , birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.

kume1 = {1,2,3}
kume2 = {1,2,3,4}
kume3 = {5,6,7}
print(kume1.issubset(kume2))
print(kume1.issubset(kume3))


#Birleşim Kümesi : union() metodu
#Bu metod, iki kümenin birleşim kümesini döner.

kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.union(kume2))

#Birleşim Kümesi ve update : update() metodu
#Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.

kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

kume1.update(kume2)
print(kume1)
print(kume2)