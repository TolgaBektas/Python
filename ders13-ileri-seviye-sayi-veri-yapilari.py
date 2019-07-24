print(bin(4))  # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
print(bin(19)) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
print(bin(521))# bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
#çıktıda ki -0b- 2lik tabanın göstergesi
print(hex(32)) # Sayımız 16'lık tabanda yazıldı.
print(hex(54)) # Sayımız 16'lık tabanda yazıldı.
print(hex(1212)) # Sayımız 16'lık tabanda yazıldı.
#çıktıda ki 0x 16lik tabanın göstergesi


#fonksiyonlar

#abs fonksiyonu
#Sayının mutlak değerini almamızı sağlar.
print(abs(-4))

#round fonksiyonu
#Sayıları alta veya üste yuvarlar.
print(round(3.7))
print(round(3.4))

#max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.
#min() fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür.

print(max(100,-2,3,4,1,131))  # İstediğimiz kadar değer verebiliriz.
# Sayıları liste şeklinde de verebiliriz.
# Sayıları demet şeklinde de verebiliriz.
print(min(100,-2,3,4,1,131))

#sum fonksiyonu
#sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.
#print(sum(3,4)) hatalı kullanım
print(sum([3,4,5,6,7])) #doğru kullanım


#pow fonksiyonu
#pow() fonksiyonu üs alma işlemlerinde kullanılır.
print(pow(2,4)) # 2 üzeri 4