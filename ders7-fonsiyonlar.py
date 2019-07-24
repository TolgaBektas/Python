# fonsiyonlar daha sonra kullanılmak üzere tanımlanır
# mutlaka bir ismi vardır
# her fonksiyon (paranteze) 'e sahiptir
# fonksiyonlar 1 veya daha fazla parametre alabilir

def selamVer():  # fonksiyon yaparken def ile tanımlarız
    print("Selamun Aleyküm!")


selamVer()  # çağırırken verdiğimiz isim ile çağırırız ()leri unutmadan


def kullaniciBilgileri(isim, soyisim, yas):
    print("İsminiz: " , isim, "\nSoyisminiz: " , soyisim , "\nYaşınız: ",yas)

kullaniciBilgileri(input("Adınız:"),input("Soy adını gir:"),input("Yaşını gir:"))

def topla(x,y):
    z=x+y
    return z # z'yi döndür
topla(10,5) # yazarsak içinde z değeri olur fonsiyonda yazdırmadığımız için yazdırmaz

a=1 # global alan

def fonksiyon():
    global a # yazar isek a nin değeri fonksiyon dışında da geçerlidir
    a=5 # yerel alan
    print(a)
fonksiyon()#çıktı 5dir fonksiyon içinde değer 5 
print(a) # çıktı 1dir fonsiyon dışındı değer 1


def faktoriyel(n):
    if n>=0:
        if n==1 or n==0:
            return 1
        else:
            return n*faktoriyel(n-1)
            #print(n*faktoriyel(n-1))
    else:
        print("Negatif sayı girme!")
faktoriyel(10)



def selamla(isim = "İsimsiz"):
    print("Selam",isim)

def baslik(kelime):
    return kelime.istitle()# istitle() fonksiyonu kelimelerin baş harfleri büyük ise başlık olarak
    #kabul eder ve true değer verir 
print(baslik("Ben Tolga")) # filter ile bir listedeki başlıkları kontrol ettirebiliriz 
#harfleri büyük olanları alır ve yazdırır olmayanları almayız




print(selamla())#içine bir parametle almaz ise isimsiz yazısı o parametrede olduğu için onu yazdıracak


def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabilirim.
    #istediğim sayıda parametre yazabilirim * sayesinde
    toplam =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam += i
    return toplam


#lambda ile hızlı fonsiyon yazma

fonksiyonAdi=lambda parametre1 : parametre1*3
print(fonksiyonAdi(5))