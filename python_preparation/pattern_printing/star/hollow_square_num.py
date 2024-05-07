def pattern(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print(str(i) * rows)
        else:
            print(str(i) + " " * (rows - 2) + str(i))

pattern(5)

