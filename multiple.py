# This Python program finds multiples of any number with user input.

number = int(input("Enter a number: "))

# Find the multiples of the number.
multiples = []
for i in range(1, 11):
    multiple = number * i
    multiples.append(multiple)

# Print the multiples.
print("The multiples of", number, "are:", multiples)