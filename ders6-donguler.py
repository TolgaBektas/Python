#while döngüsü
a=1
while(a<10):
    print(a)
    a+=1
sayi=10
while True:
    tahmin=int(input("Tahmin Et: "))
    if tahmin<sayi:
        print("Daha Büyük Sayı Gir!")
    elif tahmin>sayi:
        print("Daha Küçük Sayı Gir!")
    else:
        print("Bildin!")
        break

#for dögüsü
diller =["Python","Java","C#","JavaScript","Ruby","C++"]
for a in diller: #dillere gir her birini a degişkenine al 
    print(a)