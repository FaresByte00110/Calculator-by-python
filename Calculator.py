while True:
    while True:
        try:
            frist_number = float(input("enter frist number: "))
            break
        except ValueError:
            print("invalid number, enter real number")
    while True:
        try:
            operation = input("enter operation type (+,-,*,/): ")
            if operation in ("+", "-", "*", "/"):
                break
            else:
                raise ValueError
        except ValueError:
            print("invalid operation type, enter real operation type")
    while True:
        try:
            second_number = float(input("enter second number: "))
            if second_number == 0 and operation == "/":
                raise ZeroDivisionError
            break
        except ZeroDivisionError:
            print("cannot divide by zero, please enter another number")
        except ValueError:
            print("invalid number, enter real number")
            
    result = ""
    
    if operation == "+":
        result = frist_number + second_number
    elif operation == "-":
        result = frist_number - second_number
    elif operation == "*":
        result = frist_number * second_number
    elif operation == "/":
        result = frist_number / second_number
    else:
        result = None
    if result != None:
        print("your result is:", result)
    else:
        print("invalid error")
    while True:
        try:
            repeat = input("do you want another operation (y/n): ")
            if repeat != "y" and repeat != "n":
                raise ValueError
            break
        except ValueError:
            print("invalid answer, please enter real answer")
    if repeat == "n":
        break
            
        
        
print("program exited")