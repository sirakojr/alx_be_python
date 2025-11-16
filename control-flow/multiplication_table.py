# first declare a variable that recive input form user
# create a for loop that loop from input num for 1 upto 10
#   for index in range(10):
#         mulitplication = number * index
# then print mulitplication



number = float(input("Enter a number to see its multiplication table: "))

for index in range(1, 11):
    mulitplication = number * index
    # print(f"{number} * {index} = {mulitplication}")
    print(mulitplication)