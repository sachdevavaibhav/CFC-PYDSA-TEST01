# 2. Write a Python program to count the number of times letter ‘a’ appears in
# given list(using loops).

string = input("Enter a string: ")

a_count = 0

for letter in string:
    if letter == 'a':
        a_count += 1

print(a_count)