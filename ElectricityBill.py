# Take input for the number of units consumed from the user

units = int(input("Enter the number of units you have consumed:"))

#Check condition of units consumed
# Then calculate the amount and surcharge accordingly
# Surcharge is the tax value

# Units less than 50
if (units < 50):
    amount = units * 2.60
    surcharge = 25

# Units less than 100
elif (units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# Units less than or equal to 200
elif (units<= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

# Check for all the cases other than mentioned
# When units consumed are more than 200

else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75 

# Calculate and display the bill
# total amt = amount + surcharge
total = amount + surcharge
print("\n Electricity bill = %.2f" %total)