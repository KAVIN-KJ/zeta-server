n = int(input("Enter the number of rows: \n"))

# Print the upper half of the rhombus
for i in range(n):
    # Print spaces before the asterisks
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Print the asterisks
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()

# Print the lower half of the rhombus
for i in range(n - 2, -1, -1):
    # Print spaces before the asterisks
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Print the asterisks
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()