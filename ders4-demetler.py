#------------DEMETLER Tuplelar ---------------------------


#listeye benzer fakat değiştirilemez
#aynı şekil kalır
#birkez tanımlanır daha hızlı çalışır

demet=(1,2,33,44,556,1,1,1)
print(demet)
print(type(demet))
print(demet[3])# demetin 3. idexine ulaşır
print(demet.count(1))# demetin içinde kaç tane 1 olduğunu yazdırır

demet2=("Tolga","Bektaş","Mert")
print(demet2.index("Tolga"))#demetteki index numarasını veriyor
##print(demet2.index("Sezgin")) Olmadığı için hata veriyor

# değiştirilmesini istemediğiniz değerleri demet te depolarız
