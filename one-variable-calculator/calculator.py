print("#####################################################")
print("############ One variable calculator ################")
print("#####################################################\n")

print("*****************************************************")
print("****************** Options **************************")
print("*****************************************************\n")

number = int(input("1: Sum\n2: Substraction\n3: Multiplication\n4: Division\n5: Integer Division\n6: Exponent\n7: Rest\n\nInsert your choice: "))

if number == 1 :
    print("You choose Sum\n")
    number = float(input("Insert the first number: "))
    number += float(input("Insert the second number: "))
    print("the result is", number)

elif number == 2 :
    print("Elegiste Resta\n")
    number = float(input("Insert the first number: "))
    number -= float(input("Insert the second number: "))
    print("the result is", number)

elif number == 3 :
    print("Elegiste Multiplicacion\n")
    number = float(input("Insert the first number: "))
    number *= float(input("Insert the second number: "))
    print("the result is", number)

elif number == 4 :
    print("Elegiste Division\n")
    number = float(input("Insert the first number: "))
    number /= float(input("Insert the second number: "))
    print("the result is", number)

elif number == 5 :
    print("Elegiste Division Entera\n")
    number = float(input("Insert the first number: "))
    number //= float(input("Insert the second number: "))
    print("the result is", number)

elif number == 6 :
    print("Elegiste Exponente\n")
    number = float(input("Insert the first number: "))
    number **= float(input("Insert the second number: "))
    print("the result is", number)

elif number == 7 :
    print("Elegiste Modulo o Resto\n")
    number = float(input("Insert the first number: "))
    number %= float(input("Insert the second number: "))
    print("the result is", number)

else:
    print("The operation is not valid")