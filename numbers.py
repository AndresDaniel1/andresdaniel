#Finnur og skrifar út allar pósítívar tveggja stafa tölur sem eru 
#þannig að annað veldi af summu einstakra tölustafa er jafnt tölunni sjálfri
for i in range(10,100):
    number = i // 10 + i % 10
    if number ** 2 == i:
        print(i)
for i in range(1,100):
    deilir = 0
    for divisors in range(1,i,1):
        if i % divisors == 0:
        deilir += 1
        if deilir == 10:
            print(i)
