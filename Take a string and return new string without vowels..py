#take a string and return new string without vowels.
user_input = input("Enter a string: ")

result = ""

for char in user_input:

    if char.lower() not in "aeiou":

        result += char

print("String without vowels:", result)

