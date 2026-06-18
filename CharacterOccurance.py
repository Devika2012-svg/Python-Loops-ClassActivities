# Take input of a string
string = input("Please enter your string: ")
#Take input of a character
char = input("Please enter your own character: ")
i = 0 
count = 0
# Loop will find the occurance of a character
while (i < len(string)): #String operation

    if(string[i] == char): # condition 1
        count = count + 1
    i = i + 1

#Display the result
print("The total number of times", char, "has occurred =", count)