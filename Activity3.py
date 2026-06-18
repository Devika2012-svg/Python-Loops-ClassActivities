r = int(input("Enter the number of rows: "))

for j in range(1, r+1):
    for i in range(j):
        print('*', end=" ")
    print()