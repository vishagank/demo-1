string1 = input("enter the string1:")
string2 = input("enter the string2:")

string1 = string1.lower()
string2 = string2.lower()

sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

if sorted_string1 == sorted_string2:
    print("the givenn string is anagram.")
else:
    print("the givenn string is not anagram.")