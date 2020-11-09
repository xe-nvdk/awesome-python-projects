print("########################################################")
print("# Holiday days calculator by Ignacio Van Droogenbroeck #")
print("########################################################\n")

name = str(input("Please, insert the name of the employee: "))
department = int(input("Please, insert the ID of the department.\n Use 1 for Customer Support\n Use 2 for Logistics\n Use 3 for Management \nPlease, introduce your choice: "))

seniority = float(input("Please, insert the seniority in years: "))

if department == 1:

        if seniority < 1:
            print("\nThe employee", name, "has not right to vacations.")

        elif seniority >= 1 and seniority < 2:
            print("\nThe employee", name,"has 6 days of vacations.")

        elif seniority >= 2 and seniority < 7:
            print("\nThe employee", name,"has 14 days of vacations.")

        else:
            print("\nThe employee", name,"has 20 days of vacations.")

elif department == 2:

        if seniority < 1:
            print("\nThe employee", name, "no tiene derecho a vacaciones.")

        elif seniority >= 1 and seniority < 2:
            print("\nThe employee", name,"has 7 days of vacations.")

        elif seniority >= 2 and seniority < 7:
            print("\nThe employee", name,"has 15 days of vacations.")

        else:
            print("\nThe employee", name,"has 22 days of vacations.")

elif department == 3:

        if seniority < 1:
            print("\nThe employee", name, "no tiene derecho a vacaciones.")

        elif seniority >= 1 and seniority < 2:
            print("\nThe employee", name,"has 10 days of vacations.")

        elif seniority >= 2 and seniority < 7:
            print("\nThe employee", name,"has 20 days of vacations.")

        else:
            print("\nThe employee", name,"has 30 days of vacations.")

else :
    print("\nThe department ID is invalid. Please, try again.")

print("\nThank you for using this software.\n")
