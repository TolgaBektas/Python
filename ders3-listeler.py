#--------------LİSTELER---------------------

liste=["Tolga","Mert","Sezgin",34,58]#liste tanımlarken köşeli parantez kullanılır

print(type(liste))
print(len(liste))
liste2=list("Tolga")# her bir harfi ayrı ayrı alacak
print(liste2)
#listeler birbirleri ile toplanabilir
yeniListe=liste+liste2#liste ile liste2 yi birleştir ve yeniListe ye at
print(yeniListe)
yeniListe[3]=32452354#3üncü indexini değiştir
print(yeniListe)
yeniListe[:2]=["TOLGA","MERT"]# ilk 2 indexini değiştir
print(yeniListe)

yeniListe.append(11111)#listeye veri ekleme
print(yeniListe)

yeniListe.pop()#son elemanı listeden atar PARANTEZ içine index numarası yazılır
print(yeniListe)

sayiListesi=[1,2,3,4123,1245,432,11]
sayiListesi.sort() # küçükten büyüğe sıralar
print(sayiListesi)

sayiListesi.sort(reverse=True)# büyükten küçüğe ssıralar
print(sayiListesi)
# aynı şekilde kelimelerde de çalışır ama hem kelime hem sayılar ile olursa hata verir


#iç içe listeler

iciceListe=[[1,2],[3,4],[5,6]]
print(iciceListe)

print(iciceListe[1])# 1. indexdeki listeye ulaştık
print(iciceListe[1][0])# 1. indexteki listenin 0 numaralı indexine ulaştık