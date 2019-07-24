#-----------------VERİ TİPİ DÖNÜŞÜMLERİ---------------------

tamSayi=45 # tam sayi iken
tamSayi=float(tamSayi)# float yaani ondalılı sayi tipine dönüştürüldü ve tekar değişkenin içine atıldı
print(tamSayi)

tamSayi=int(tamSayi)# şimdi ise 45.0 ı int türüne çevirdi
print(tamSayi)
tamSayi=str(tamSayi)#artık 45 sayısı bir string türüdür
print(tamSayi)
print(len(tamSayi))#string değer olduğunu len fonk ile de görebiliriz 
# çevirmek istediğimiz değeri parantez içine yazmamız yeterli int(*) float(*) str(*)

# stringden inte çevirme
string="00421asd"# bu şekilde harf de var ise int e çevirme işlemi olmaz
#int(string) hata verir
string="1234"## sadece rakam var ise
string=int(string)##çevirme başarılı olur
print(string)

ondalik="3.14"# ondalık değerde string tür
ondalik=float(ondalik) # birden fazla nokta (3.14) olmadığı için çalışır
print(ondalik)
