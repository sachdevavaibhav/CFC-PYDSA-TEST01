# 4. Print the following pattern for input n = 5

rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end='')

    spaces = rows-i
    spaces_02 = rows-(i+1)
    print(spaces*' ', end='')
    print(spaces_02*' ', end='')

    start = i
    end = 1
    while start >= end:
        if start != 5:
            print(start, end='')
            start -= 1
        else:
            start = 4

    print()