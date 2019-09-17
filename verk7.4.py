# is_prime function definition goes here
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % 2 == 0:
                return False
                break
        else:
            return True
    else:
        return False
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
prime = is_prime(num)
if prime == True:
    print(num, "is a prime")
elif prime == False:
    print(num, "is not a prime")
