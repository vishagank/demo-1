#Take string and return a new the number of unique charater:

new_string = input("Enter the character:")
new_string = new_string.lower()

new_string_ok = set(new_string)
unique_char = len(new_string_ok)

print("The number unique char in",unique_char)
