while True:
    user_input =int(input("ENTER numbers to check whether positive or negative press 0 for exit : "))
    if user_input == 0:
        break

    elif user_input < 0:
        print("YOUR NUMBER IS NEGATIVE ")
    elif user_input>0:
        print("YOUR NUMBER IS POSITIVE ")