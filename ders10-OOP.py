#nesne tabanlı programlaa
class araba():#yazılan özellikler herhangi bir obje ye özgü olmuyor Class a özgü oluyor 
    model="Renault Symbol"
    renk="beyaz"
    kilometre=130.000
    fiyat=39.500

araba1=araba() #araba classından obje üretme
print(araba1)

#ozellikerine erişme
print(araba1.kilometre)
#araba clasına ulaşma
print(araba.model)
#print(dir(araba()))#varsayılan özellkiler veya fonsiyonlar

class kisiBilgileri():
    def __init__(self,isim="Boş",soyisim="Boş",dogum_yeri="Boş"):
# Peki burada self ne anlama geliyor ? self anahtar kelimesi objeyi oluşturduğumuz zaman o
# objeyi gösteren bir referanstır ve metodlarımızda en başta bulunması gereken bir parametredir.
# Yani biz bir objenin bütün özelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.
        self.isim=isim
        self.soyisim=soyisim#obje özellikleri
        self.dogum_yeri=dogum_yeri

    def bilgileriGoster(self):#içindeki bilgileri görmek için yazılan bir method
        #OBJEYE METHOD EKLEME
        print(self.isim)
        print(self.soyisim)
        print(self.dogum_yeri)

    def dogum_yeri_degistir(self,yeni_dogum_yeri):# kullanıcıdan dogum yerini değiştirmesi için bir method
        self.dogum_yeri=yeni_dogum_yeri#veya fonksiyon
        print("Doğum Yeri Değiştirme Başarılı!")



Kullanici1=kisiBilgileri()
print("BU SATIRDAN SONRA Kullanici1 DEKİ ELEMANLARI bilgileriGoster() FONKSİYONU İLE GÖRECEĞİZ")
Kullanici1.bilgileriGoster()

print("OLUŞTULAN OBJENİN İÇİNE DEĞER ATAMADIK")
print("----------------------------------------------")
print("KULLANICIDAN OBJEYİ DOLDURMASINI İSTEDİK")

Kullanici1.isim=input("İsim:")
Kullanici1.soyisim=input("Soyisim:")
Kullanici1.dogum_yeri=input("Doğum Yeri:")

print("KULLANICI OBJEYİ DOLDURDU ")

print("İsim->",Kullanici1.isim)
print("Soyisim->",Kullanici1.soyisim)
print("Doğum Yeri->",Kullanici1.dogum_yeri)

Kullanici1.dogum_yeri_degistir(input("Yeni Doğum Yeri Gir:"))
print("Yeni Doğum Yeri->",Kullanici1.dogum_yeri)


#inheritance  kalıtım


class calisan():
    def __init__(self,isim,soyisim,maas,departman):#calisan classın değerlerini tanımlama alacağı değişkenleri
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.departman=departman

    def bilgileriGoster(self):
        print("İsim->",self.isim)
        print("Soyisim->",self.soyisim)
        print("Maaş->",self.maas)
        print("Departman->",self.departman)
        
        

    def departmanDegistirme(self, yeniDepartman):
        self.departman=yeniDepartman
calisanMert=calisan("Mert","Önüt",1500,"çaycı")
class Yonetici(calisan): #yonetici classının parantezine calisan classını yazarsak tüm özelliklerine sahip olur

    #bu classın içinde miras alınan methodlar yeniden yazılabilir ekleme yapılabilir
    #o zaman miras alınan geçersiz kalır
    #örneğin init fonksiyonunu alıp burda bir kaç eleman daha ekleyebiliriz o zaman üstteki miras alma olmaz
    #burdaki neyse o çalışır
    #isimleri aynı olursa methodlar miras iptal olur
    #örneğin calisan da yapılan bilgileriGoster methodunu aynı şekil yazarsak adını miras iptal olur
    #bir nevi üstüne yazar ama yukardaki class daki method o class için çalışmaya devam eder

    #super() fonksiyonu ile yukardaki init teki yazılanları burdada kullanabiliriz
    def __init__(self,isim,soyisim,maas,departman,sorumlu_eleman_sayisi):
    #sadece bu class ta sorumlu eleman sayısı isteniyor ekstradan ama diğer özelliklerde lazım
        super().__init__(isim,soyisim,maas,departman)
    #normalde aşağıdaki kodu tek tek yazmak zorundayık fakat super() fonksiyonu ile tekrar yazmaya gerek yok

        self.sorumlu_eleman_sayisi=sorumlu_eleman_sayisi

    def bilgileriGoster(self):#yukardakinden miras almaktan vazgeçtim super fonksiyonu ile ihtiyac olani alcam
        #print("İsim->",self.isim)
        #print("Soyisim->",self.soyisim)
        #print("Maaş->",self.maas)
        #print("Departman->",self.departman)
        super().bilgileriGoster()#bu şekilde yukardaki classtaki fonksiyonu alabiliriz
        print("Sorumlu Eleman Sayısı->",self.sorumlu_eleman_sayisi)


yoneticiTolga=Yonetici("Tolga","Bektaş",10000,"CEO",10)
print(yoneticiTolga.bilgileriGoster())
yoneticiTolga.departmanDegistirme("PATRON")
print(yoneticiTolga.bilgileriGoster())
print(calisanMert.bilgileriGoster())



#özel methodlar kullanımı

#yeni bir class oluşturalım
class kitap():
    pass#içine herhangi bir method tanımlamayalım

kitap1=kitap() #kitap1 objesini oluşturduk __init__ methodu OTOMATİK TANIMLI
print(kitap1) # __str__ methodu OTOMATİK TANIMLI
#len(kitap)#__len__ methodu fakat otomatik tanımlı değil
del kitap1 # oluşturulan objeleri silmek için kullanılır
print(kitap1) # name kitap1 is not defined yani silindi

class kitap():
    def __init__(self, isim,yazar,sayfa_sayisi):# burda yeniden tanımlama yapyoruz __init__ fonksiyonu için
        print("init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayisi=sayfa_sayisi

    def __str__(self):#print(obje adı) yazılınca return da yazılan değerler döndürülecek
        return "İsim {}\nYazar: {}\nSayfa Sayısı:{}".format(self.isim,self.yazar,self.sayfa_sayisi)
        #artık print(obje) yazınca bu değerler gelecek
        # bilgileriGoster tarzında bir method yazmak gerekmiyor bu durumda

    def __len__(self):
        return self.sayfa_sayisi
    #artık len(obje adı) methodu çalışacak ve sayfa_sayisi değerini döndürecek

    def __del__(self):#burda method varsayılanın yerine değişmez
    # sadece ekleme yapılır
        print("Obje Siliniyor...")
        #silme işlemi hala geçerli sadece "Obje Siliniyor..." yazdıracak
    