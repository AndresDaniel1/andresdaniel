my_int = input('Give me an int >= 0: ')
# Fill in the missing code
int1 = int(my_int)
str = " "
str1 = "1"
str0 = "0"
while int1 >= 1:
    if int1 % 2 == 0:
        str = str + str0
        int1 = int1 // 2
    elif int1 % 2 == 1:
        int1 = int1 // 2
        str =str + str1 

print("The binary of", my_int, "is", str[::-1])