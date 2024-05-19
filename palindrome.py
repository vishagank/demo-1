#Take a string and return if it palindrome or false otherwise:

user_input = input("enter the input :")
user_input2 = input("enter the input2 :")

user_input = user_input.lower()
user_input2 = user_input2.lower()

for i in user_input:
    if i in user_input == user_input2:
print("enterd palindrome is true")
else:
print("enterd palindrome is false")