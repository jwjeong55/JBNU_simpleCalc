import calcu_function as cf
import logging

logging.basicConfig(filename='CalcuRecord', level=logging.DEBUG, datefmt= '%Y-%m-%d %H:%M:%S',format = '%(asctime)s | %(levelname)s | %(message)s' )

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            resultString = str(num1)+ "+" + str(num2) +"=" + str(cf.add(num1,num2))
            print(resultString)
            logging.debug(resultString)

        elif choice == '2':
            resultString = str(num1) + "-" + str(num2) + "=" + str(cf.subtract(num1, num2))
            print(num1, "-", num2, "=", cf.subtract(num1, num2))
            logging.debug(resultString)

        elif choice == '3':
            resultString = str(num1) + "*" + str(num2) + "=" + str(cf.multiply(num1, num2))
            print(num1, "*", num2, "=", cf.multiply(num1, num2))
            logging.debug(resultString)

        elif choice == '4':
            if num2!=0:
                resultString = str(num1) + "/" + str(num2) + "=" + str(cf.divide(num1, num2))
                print(num1, "/", num2, "=", cf.divide(num1, num2))
                logging.debug(resultString)

            else:
                print("Error : div by zero")
                logging.warning("input zero in divide")

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
        logging.warning("exceed range of input")
        print("Invalid Input")