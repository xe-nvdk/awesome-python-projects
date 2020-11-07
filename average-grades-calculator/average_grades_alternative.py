print("System designed to calculate average grades by Ignacio Van Droogenbroeck")

name = str(input("what's your name: "))
print("hi " + name + " let's calculate some average grades")

math = float(input(name + " What's your math grade: "))
history = float(input(name +  " What's your history grade: "))
music = float(input(name + " What's your music grade: "))

average = (math + history + music) / 3

print("Your average grade is ", round(average,2)) # To concatenate text with a float or int number, we can use a comma (,)

if average >= 7 :
    print("Congratulations, you approved")

else : # if our condition is not comply print 👇
    print("You're a donkey, Keep studying")