with open("part5.txt","r+",encoding = "utf-8") as file:#r+ kipi hem okumamızı sağlıyor hemde yazmamızı sağlıyor
    print(file.read())
    #file.seek(6)
    #file.write("6. satır")#üzerine yazıyor 
    print(file.read())
   
#dosyanın sonuna ekleme yapma

#with open("part5.txt","a",encoding="utf-8") as file:
    #file.write("Dosya sonu ekleme")

with open("part5.txt","r+",encoding = "utf-8") as file:
    icerik=file.read()
    icerik="Dosyanın Başına Ekleme\n"+icerik
    file.seek(0)#dosyanın başına gelip iceriği tekrardan yazdırıyoruzs  
    file.write(icerik)

#dosyanın ortasına ekleme yapma

with open("part5.txt","r+",encoding = "utf-8") as file:
    liste=file.readlines()
    print(liste)
    liste.insert(3,"AHMED\n")#listenin 3. indexine ekleme yapar
    file.writelines(liste)