def reverse_string(names):
     reversed_str = names[::-1]
     return reversed_str

# name = "divyansh"
name = str(input("enter your name - "))

output = reverse_string(name)

if(name==output):
     print ("Entered Value is a palindrome")
else:
     print("Not a Palindrome")

# print (f"Reversed String:{output}")
