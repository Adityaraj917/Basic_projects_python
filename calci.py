while True:
    Operation = """1. Addition (+)
                   2. Subtraction (-)
                   3. Multiplication (*)
                   4. Division (/)
                   5. Exit"""

    choice = input("Choose an operation: ")

    if choice == "+" or choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == "-" or choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)

    elif choice == "*" or choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)

    elif choice == "/" or choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 / num2)

    else:
        break