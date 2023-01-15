marks = int(input("Enter your marks: "))
if marks < 25:
    print("Your grade for " + str(marks) + " marks is F")
elif 45 > marks >= 25:
    print("Your grade for " + str(marks) + " marks is E")
elif 50 > marks >= 45:
    print("Your grade for " + str(marks) + " marks is D")
elif 60 > marks >= 50:
    print("Your grade for " + str(marks) + " marks is C")
elif 80 > marks >= 60:
    print("Your grade for " + str(marks) + " marks is B")
elif marks > 80:
    print("Your grade for " + str(marks) + " marks is A")