num = int(input("enter a number to find factorial- "))
factorial = 1
# For loop
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)