def most_frequent_char(input_string):
    char_freq = {}

    for char in input_string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    most_frequent = max(char_freq, key=char_freq.get)
    return most_frequent

user_input = input("Enter a string: ")


result = most_frequent_char(user_input)

print(f"The most frequent character is: {result}")
