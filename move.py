#forrit sem hreyfir notanda a x as
numb = int(input("Input a position between 1 and 10:"))

lil_str = " "
#bua til lista yfir stokin 
lis = ["x","x","x","x","x","x","x","x","x","x"]
position_of_o = numb-1
lis[position_of_o] = "o"

for i in lis:
    lil_str += i
print(lil_str)

print("l- for moving left")
print("r- for moving right")  
print("any other letter for quitting") 
move = "r"

while move == "r" or move == "l": 
    lil_str2 = "" 
    move = input("input your choice: ")
    if move == "r":
        if position_of_o != 9:
            lis[position_of_o] = "x"
            position_of_o += 1
            lis[position_of_o] = "o"
        for i in lis:
            lil_str2 += i
    if move == "l":
        if position_of_o != 0:
            lis[position_of_o] = "x"
            position_of_o -= 1
            lis[position_of_o] = "o"
        for i in lis:
            lil_str2 += i
    print(lil_str2)
         
        