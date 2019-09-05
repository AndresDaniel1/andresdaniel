#algorithm that generates the numbers in the following sequence: 1,2,3,6,11,20,37
n = int(input("Enter the length of the sequence: ")) # Do not change this line

#write the rule for the sequence that executes as many times as the input
first = 1
second = 0
third = 0

for i in range(0,n):
    if first != 2:
        utkoma = first + second + third 
        print(utkoma)
        third = second
        second = first
        first = utkoma
    else:
        utkoma = first + second 
        print(utkoma)
        third = second
        second = first
        first = utkoma







    



