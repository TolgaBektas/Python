try:
    with open("part3.txt","r",encoding = "utf-8") as file:#part3.txt adında dosya okumak için r kipini kullanıyoruz
        print("İçerik 1:")
        print(file.read(),end="")#fakat part3.txt dosyası olmaz ise hata verir
        #buradaki end parametresi fazladan bırakılan boşlukları engellemek için kullanılır
        #file.read() yaptktan sonra tekar okuma yapamayız çünkü dosyanın imleci sona gidicektir ve boş okuyacaktır
        print("İçerik 2:")
        print(file.read())
        #çıktı boştur
except FileNotFoundError:
    print("Dosya Bulunamadı!")#hatayı bu şekilde yakalayabiliriz
print("File.readline() denemesi")
with open("part3.txt","r",encoding = "utf-8") as file:
    print(file.readline())#tek satırı okur 
    print(file.readline())#ikinci satırı okur imlecin kaldığı yerden devam eder
    #okuycak birşey kalmaz ise boş string döndürür

print("file.readlines() fonksiyonu")
with open("part3.txt","r",encoding = "utf-8") as file:
    print(file.readlines())#her satırı okur ve listeye atar