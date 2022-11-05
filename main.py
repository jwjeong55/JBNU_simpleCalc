import  calcu_function as cf



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        if choice == '1':
            print(num1, "+", num2, "=", cf.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", cf.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", cf.multiply(num1, num2))
        elif choice == '4':
            if num2!=0:
                print(num1, "/", num2, "=", cf.divide(num1, num2))
            else:
                print("Error : div by zero")

        # check if user wants another calculation
        # break the while loop if answer is no
        firstFlag = False





        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.upper()
            if next_calculation == "YES": #continue calc
                break
            elif next_calculation == "NO": #quit calc
                while True:
                    next_calculation = input("Are you sure? (yes/no): ")
                    next_calculation = next_calculation.upper()
                    if next_calculation == "YES":
                        quit()
                    elif next_calculation == "NO":
                        firstFlag = True
                        break

            if firstFlag == True:
                break










    else:
        print("Invalid Input")
