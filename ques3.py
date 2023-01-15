import random
num_questions = 10
points = 0
for i in range(num_questions):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = int(input("What is {} x {}? ".format(num1, num2)))
    if answer == num1 * num2:
        points += 1
        print("Correct!")
    else:
        print("Incorrect. The correct answer is {}.".format(num1 * num2))
print("You scored {} points.".format(points))