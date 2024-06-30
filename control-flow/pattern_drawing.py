number = int(input("Enter a positive integer: "))
man = number
while number > 0:
    for b in range(man):
        print("*", end="")
    print()
    number -= 1
