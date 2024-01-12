def find_sum_of_n_numbers(n):
    sum = n* (n+1) // 2
    return sum

n = int(input("enter a number to find sum "))
result = find_sum_of_n_numbers(n)
print(f"sum of {n} numbers are {result}")