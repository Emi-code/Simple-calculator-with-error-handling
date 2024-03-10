while True:
    print("welcome to your calculator")

    while True:
        try:
            value1=float(input("first value" ))
            break
        except ValueError:
            print("Error: That wasn't a numerical value. Please try again.")
        

    operation=input("choose your arithmetic operation" )

    while True:
        try:
            value2=float(input("second value" ))
            break
        except ValueError:
            print("Error: That wasn't a numerical value. Please try again.")

    def arithmetic(operation):
        if operation == "+" :
            return value1 + value2
        elif operation == "-":
            return value1 - value2
        elif operation == "*":
            return value1 * value2
        elif operation == "/":
            if value2 !=0:
                return print("cannot divide by 0")
            else:
                return value1 / value2
        
        else:
            print("invalid opera")
        
    print(arithmetic(operation))

    end=input("calculation Finished, Would you like to do another? Y or N :" )
    if end == "N":
        break