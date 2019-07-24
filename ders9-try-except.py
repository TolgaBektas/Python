#print(a) # nameError
#int("asd1234") #valueError
#print(2/0)#zeroDivisionError
#print("tolga"asd)#syntaxError

#EXAMPLE

try:    
    a =  int("324234dsadsad") # Burası ValueError hatası veriyor.
    print("Program burada")
except: # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.
    
print("Bloklar sona erdi")


try:
    
    b =  int("324234") # Burası normal çalışıyor
    print("Program burada")
except ValueError: # Hatayı belirtirsek ValueError hatası bu kısma giriyor.
    print("Hata oluştu") # Hata olmadığı için çalışmadı.
    
print("Bloklar sona erdi")



try:
    c = int(input("Sayı1:"))
    d = int(input("Sayı2:")) # Hata burada oluşuyor. ValueError'a bloğuna giriyoruz. 
    print(c / d)
except ValueError:#değeri inte çevirdiğimiz için int haricinde hata verir 
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")



try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) 
except (ValueError,ZeroDivisionError):#aynı anda girer iki h atayıda aynı anda kontrol eder
    print("ZeroDivision veya ValueError hatası"),
 
#finally kısmı

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Her durumda çalışıyorum.")# bu kısım her türlü çalışacak


# Verilen string'i ters çevirmek
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")#foknsiyon içi hata yakalama
    else:
        return s[::-1]
    
try:
    print(terscevir(321))  
except:
    print("HATA")