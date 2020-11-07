print("System designed to calculate average grades by Ignacio Van Droogenbroeck")

# This program will ask for the name of the student, grades for three classes, sum that three grades and then, make an operation to get the average. Here, also I use conditionals to calcuate if the student reach the average grade to pass or not and print one or another text depending of the results.

name = str(input("what's your name: "))
print('hi ' + name + " let's calculate some average grades")

math = float(input(name + " what's your math grade: "))
history = float(input(name +  " what's your history grade: "))
music = float(input(name + " what's your music grade: "))

average_sum = math + history + music # I divided in two operations, because if I made in one, the results is not the expected.
average = average_sum / 3

# Another way - average = (math + history + music) / 3

print("Your average grade is " + str(average)) # Here I need to convert the average that is original a float data type to a string. I using this approach to concatenate the text and the average grade.

if average >= 7 :
    print("Congratulations, you approved")

if average < 7 :
    print("You're a donkey, Keep studying")