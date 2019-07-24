with open("part4.txt","r",encoding = "utf-8") as file:#part3.txt adında dosya okumak için r kipini kullanıyoruz
    print(file.tell())#imlecin nerde olduğunu hangi byte olduğnu söyler
    #0 çıktısı yani dosyanın başında olduğunu söylüyor
    file.seek(21)#21. karaktere git 
    print(file.tell())
    print(file.read(4))#21.karakterden itibaren 4 karakteri aldık ve yazdırdık
    print(file.tell())#imlecin nerde olduğnu öğrenelim
    file.seek(0)#imleci en başa aldık
    print(file.tell())
        