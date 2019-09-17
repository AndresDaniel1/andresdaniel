largest = 0
num = 0 
# Fill in the missing code

# á meðan númerið er stærri en -1 heldur lúppan áfram
while num > -1:
    num = int(input("input a number: "))
#ef númerið er stærri en largest verður númerið largest svo að hann beri alltaf allar
#tölur saman og í lokin verður þá largest stærsta talan

    if num > largest:
        largest = num
    
print("The maximum is", largest)    # Do not change this line
