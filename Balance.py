balance = 5000
pin = 1234
count = 0

while count < 3:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("CORRECT PIN")
        
        amount = int(input("Enter amount: "))
        
        if amount <= balance:
            balance =balance - amount
            print("Withdrawal successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")

        break
    else:
        count += 1
        print("Incorrect PIN")

        if count < 3:
            print("Attempts left:", 3 - count)

if user_pin != pin:
    print("Your card is blocked due to 3 incorrect attempts.")

