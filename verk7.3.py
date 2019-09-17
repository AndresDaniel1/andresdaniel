# The function definition goes here
def inc(num):
    if num > 1 and num < 555:
        print(num, "is in range. ")
    else:
        print(num, "is outside the range! ")
    return num 

num = int(input("Enter a number: "))

# You call the function here
inc(num)


