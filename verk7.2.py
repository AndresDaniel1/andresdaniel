# Your function definition goes here
def inc(num):
    upper = 0
    lower = 0
    for i in user_input:
        if i >= 'A' and i <= 'Z':
            upper += 1
        elif i >= 'a' and i <= 'z':
            lower += 1 
    return upper, lower

user_input = input("Enter a string: ")
# Call the function here
upper, lower = inc(user_input)


print("Upper case count: ", upper)
print("Lower case count: ", lower)