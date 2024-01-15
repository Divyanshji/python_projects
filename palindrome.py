def reverse_string(names):
     reversed_str = names[::-1]       # Using string slicing to reverse the string
     return reversed_str

name = str(input("enter your name - "))

output = reverse_string(name)

if(name==output):
     print ("Entered Value is a palindrome")
else:
     print("Not a Palindrome")

