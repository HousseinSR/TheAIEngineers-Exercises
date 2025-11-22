num = int(input("Enter a number: "))

if num % 4 == 0:
    print("The number is a multiple of 4")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

num = int(input("Enter the number to check: "))
check = int(input("Enter the number to divide by: "))

if num % check == 0:
    print(f"{check} divides evenly into {num}")
else:
    print(f"{check} does NOT divide evenly into {num}")
