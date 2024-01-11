import sys
sys.setrecursionlimit(1500) #Updating the recursion limit to 1500. by Default is 1000 

def countdown(i):
    print(i)
    if(i <=0 ):
        return
    else:
        countdown (i- 1)

num = int(input("enter a number to print in reverse till 0 - "))
result = countdown(num)