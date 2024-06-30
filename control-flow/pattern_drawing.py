number = int(input("Enter the size of the pattern: "))
man = number
while number > 0:
    for b in range(man):
        print("*", end="")
    print()
    number -= 1
