# find_min function definition goes here

def inc(num):
    if first < second:
        result = first
    elif second < first:
        result = second 
    else:
        result = second
    return result

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = inc(first)
minimum = inc(second)
    
# Call the function here
print("Minimum: ", minimum)