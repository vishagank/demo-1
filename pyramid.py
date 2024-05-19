rows = 20
number = 1

# Iterate over each row
for i in range(1, rows + 1):
    # Print leading spaces for the pyramid shape
    for _ in range(rows - i):
        print(" ", end="")

    # Print numbers in increasing order up to 2*i-1
    for _ in range(1, 2 * i):
        print(number, end="")
        number += 1

    # Move to the next line for the next row
    print()