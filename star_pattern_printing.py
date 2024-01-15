n=5
# Star Square
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print("")
print("-----------")

# Increasing Triangle
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print("")
print("-----------")
# Decreasing Stars
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print("")
    
print("-----------")
