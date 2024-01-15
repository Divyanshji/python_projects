def reverse_string(names):
       # Using string slicing to reverse the string
     reversed_str = names[::-1]
     return reversed_str

# name = "divyansh"
name = str(input("enter your name "))

output = reverse_string(name)

print (f"Reversed String:{output}")
