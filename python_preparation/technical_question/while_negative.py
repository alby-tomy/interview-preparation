total = 0

while True:
    number = float(input("Enter a number (enter negative number to stop): "))
    if number < 0:
        break
    total += number

print("Sum of the positive number:", total)
