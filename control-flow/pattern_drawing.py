user_input = int(input("Enter the size of the pattern: "))
i = 0
while i < user_input:
    print("*", end="")
    j = 1
    while j < user_input:
        print("*", end="")
        j += 1
    print()
    i += 1