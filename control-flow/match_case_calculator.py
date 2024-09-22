num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case  "+":
        print("The result is: ", int(num1) + int(num2))
    case "-":  
        print("The result is: ", int(num1) - int(num2))
    case "*":
        print("The result is: ", int(num1) * int(num2))
    case "/":
       if num2 == "0":
           print("You cannot divide by zero")
       else:
            print("The result is: ", int(num1) / int(num2))
    case _:
        print("Invalid operation")