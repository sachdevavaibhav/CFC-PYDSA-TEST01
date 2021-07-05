# 3. Write a Python program to sum of two given integers. However, if the sum
# is between 15 to 20 it will return 20.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

ans = num1 + num2

if 15 <= ans <= 20:
    print(20)
else:
    print(ans)