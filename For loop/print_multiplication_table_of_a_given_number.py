# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


input = int(input("Which table you want to print: "))

for i in range(1, 11, 1):
    table = input*i
    print(table)