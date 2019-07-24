#upper() ve lower()
#upper() metodu stringin tüm karakterlerini büyük harfe çevirir.

#lower() metodu stringin tüm karakterlerini küçük harfe çevirir.


print("TOLGA BEKTAŞ".lower())
print("tolga bektaş".upper())

#replace()
#replace(x,y) : Stringteki x değerlerini y ile değiştirir.
print("Python Programlama Dili".replace(" ","-"))
print("Kunduz".replace("duz","zun"))

#startswith() ve endswith()
#startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.

#endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.
print("Tolga".startswith("to"))#büyük küçük harf önemli
print("Tolga".startswith("To"))
print("Tolga".endswith("a"))
print("Tolga".endswith("b"))



#split()
#split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.


liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.
print(liste)
liste2 = "Python-Php-Java-C-Javascript".split("-")
print(liste2)


#strip() , lstrip() ve rstrip()
#strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

#lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

#rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.

print("                   python                          ".strip())#strip() içi boş olduğu için boşluk olarak alır ve boşlukları siler
print(">>>>>>>>>>>>>>Tolga>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">"))
print("                            python      ".lstrip()) #left strip yani soldan sil
print("                            python      ".rstrip())# right strip yani sağdan sil

#count()
#count(x): Stringin içindeki x değerlerini sayar.

#count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
print("ada kapısı yandan çarklı".count("a"))
print("ada kapısı yandan çarklı".count(" "))
print("ada kapısı yandan çarklı".count("a",2))



#find() ve rfind()
#find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

#rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

print("araba".find("a"))
print("araba".find("s"))
print("araba".rfind("a"))
print("araba".rfind("s"))