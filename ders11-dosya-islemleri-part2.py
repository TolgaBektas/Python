with open("part2.txt","a",encoding = "utf-8") as file:#part1.txt adında dosya açıyoruz kip olarak a kullanıyoruz
    #kip olarak a kullanırısak (append) eğer böyle bir dosya yoksa oluşturacaktır var ise sadece ekeleme yapacaktır
    #dosyanın en sonuna ekleme yapar
    file.write("tolga\n")#program çalıştıkça ekleme yapıyor dosyanın üzerine yazmıyor