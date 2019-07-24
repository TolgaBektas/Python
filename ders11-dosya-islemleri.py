#open("bilgiler.txt","w") # Dosyayı bulunduğumuz dizinde açıyor.
#eğer öyle bir dosya varsa üzerine (w)rite eder "w"'nun anlamı budur
#file = open("bilgiler.txt","w") # Dosya üzerinde işlem yapacak dosya imlecini file isimli değişkene atıyoruz.


#dosya boş yere açık kalmamalıdır
#file.close()  # Dosyayı kapatmak
#Eğer bir dosyayı bulunduğumuz dizinde değil de başka bir dizinde açmak istersek, dizinin yolunu özellikle belirtmeliyiz.

#file = open("C:/Users/user/Desktop/bilgiler.txt","w") # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.


#file = open("bilgiler.txt","w",encoding="utf-8") # Türkçe karakter kullanacaksak encoding="utf-8" parametresini veriyoruz.
#file.write("tolga bektaş mert önüt") # write fonksiyonu ile dosyamıza yazıyoruz. 20 bytelık yani 20 karakter yazıldı.
#file.close()

#“append” (ekleme) kelimesinin kısaltması olan “a” kipiyle bir dosyayı açtığımızda ,
# dosya eğer yoksa oluşturulur. Eğer öyle bir dosya mevcut ise, dosya tekrar oluşturulmaz ve 
# dosya imleci dosyanın sonuna giderek dosyaya ekleme yapmamızı sağlar.
file = open("bilgiler.txt","a",encoding="utf-8")
file.write("\nmert tolga") #bir alt satıra yazdırmak için \n  kullandık
file.close()
file = open("bilgiler.txt","r", encoding="utf-8")
file.close()

try:
    file = open("bilgiler2.txt","r",encoding= "utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı....")
file.close()
#dosya okuma
file = open("bilgiler.txt","r",encoding= "utf-8") # Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.

#for i in file: # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    #print(i,end = "") # Her bir satırı ekrana basıyoruz.#her bir satır arasını boşlukla yazmamak için end parametresini kullandık

icerik=file.read()
print("İçerik1:\n",icerik)

file.close()
#readline() fonksiyonu 
#her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde 
#dosya imlecimiz (file) bir satır atlayarak devam eder.
file=open("bilgiler.txt","r",encoding= "utf-8")
print("---------------------------")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#readlines() fonksiyonu dosyanın bütün satırları bir liste şeklinde döner.
file=open("bilgiler.txt","r",encoding= "utf-8")
print("---------------------------")
print(file.readlines())

with open("bilgiler.txt","r",encoding = "utf-8") as file:#dosyayı otomatik kapatatmaya yarıyor
    for i in file:#Eğer dosya işlemlerini bu blok içinde yaparsak işlemimiz bittiği zaman dosyamız otomatik olarak kapanacaktır.
        print(i)


#Biliyorsunuz önceki dersimizde dosyaları okurken sadece dosyanın en başından başlayabiliyorduk
#ve dosya imlecimiz okuma işleminin sonunda , dosyanın en sonuna gidiyordu.
#Ancak biz çoğu zaman dosya imlecini (file) dosyanın herhangi bir yerine götürmek isteyebiliriz.
#Bunun için Pythondaki seek() fonksiyonunu kullanacağız. Ancak ondan önce dosya imlecinin hangi byteda 
#olduğunu söyleyen tell() fonksiyonuna bakalım.
print("------------------")
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.tell())#0 çıktısı yanı dosyanın başında olduğnu söylüyor
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(20) # 20.byte götürdük.
    print(file.tell()) 


with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(6) # 6.byte gidiyoruz.
    icerik = file.read(11)  # 11 karakteri okuyoruz.
    print(icerik)
    print(file.tell())#hangi byte ta (karakterde olduğumuzu söylüyor)

with open("bilgiler.txt","r+",encoding = "utf-8") as file: #r+ hem okuma hem yazma işlemi yaptırır
    file.seek(10) # 10. byte
    file.write("Deneme")#10. karakterden sonrasına üstüne yazdırır 
    print(file.read())
    

with open("bilgiler.txt","a",encoding = "utf-8") as file:
    file.write("\nasdasasddsadsa\n") # "append" metoduyla açılan bir dosyanın imleci direk dosyanın sonunda olduğu için sadece write
    #print(file.read()) burda okuma işlemi yapmaz çünkü dosya kipi a yani append ekleme

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.read())

#“bilgiler.txt” dosyamızın başına bir tane satır eklemek için ne yapabiliriz ? 
#Bunun için dosyamızı bütünüyle string halinde alıp daha sonra satırımızı string’in başına eklememiz gerekiyor. 
#Daha sonra dosyanın en başına seek() fonksiyonuyla giderek ,direk write() fonksiyonunu kullanabiliriz.

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    
    icerik = "Semih Aktaş\n" + icerik
    file.seek(0)
    file.write(icerik)
    print(file.read())



with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Mehmet Keper\n")
    file.seek(0)
    for satır in liste:
        file.write(satır)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)
 