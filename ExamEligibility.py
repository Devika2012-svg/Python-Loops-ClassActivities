#Take input for the student that he can attend the exam or nott
medical_cause = input("Did you have a medical cause? (Y/N)").strip().upper()
# Checking the user input and predicting output accordingly
if medical_cause == "Y": #Condition 1
    print("You are allowed to take the exam.")

else:
#Take attendence
    atten = int(input("Enter the attendence of the student:"))

    if atten >= 75:
        print("allowed")
    else:
        print("Not allowed")