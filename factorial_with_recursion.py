def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

num = int(input("enter a number to find factorial- "))
factorial = fact(num)
print("The factorial of",num,"is",factorial)