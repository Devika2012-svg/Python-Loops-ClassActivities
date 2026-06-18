# input the value of terms
n = int(input("Enter the value of the terms: "))

sum = 0
i = 1 # initialize
while i <= n:
    sum = sum + i
    i = i + 1

print("\nSum =", sum)