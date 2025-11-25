

corportes = {
    "Sachin": 1234,
    "Aditya": 2341,
    "Souvik": 6968,
    "Ayush": 8787,
    "Pruthvi": 3242
}


leaves_souvik = (1, 0, 0, 0, 1)
leaves_pruthvi = (1, 0, 0, 1, 1)
leaves_sachin = (0, 0, 1, 1, 1)
leaves_ayush = (0, 0, 0, 1, 1)
leaves_aditya = (1, 0, 0, 0, 0)


salary_souvik = (65000, 65000, 67000, 67000, 68000, 69000, 69000, 69000, 69000, 69000)
salary_pruthvi = (70000, 70000, 68000, 68000, 67000, 67000, 69000, 69000, 69000, 69000)
salary_Ayush = (66000, 67000, 67000, 67000, 67000, 67000, 67000, 67000, 67000, 69000)
salary_sachin = (78000, 78000, 78000, 78000, 78000, 78000, 67000, 67000, 66000, 66000)
salary_Aditya = (88000, 87000, 87000, 86000, 85000, 87000, 86000, 87000, 87000, 87000)

print("Welcome to MYCORPORATE_life")

username = input("Enter your name sir: ")
userpin = int(input("Enter your password sir: "))

if username in corportes and userpin == corportes[username]:

    while True:
        print(f"\nWelcome {username} sir\n")
        print("What option you want to know?\n"
              "1. Today's task at MYCORPORATE_life\n"
              "2. Recent salaries credited\n"
              "3. Leaves taken in this week\n"
              "4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                with open(f"{username}.txt", "r") as file:
                    print(file.read())
            except:
                print("No task file found for", username)

        elif choice == "2":
            sal = input("In which manner you want to review your salary?\n"
                        "1. Monthwise\n"
                        "2. All recent salaries\n"
                        "Enter choice: ")

            if username == "Souvik":
                salary_data = salary_souvik
            elif username == "Pruthvi":
                salary_data = salary_pruthvi
            elif username == "Ayush":
                salary_data = salary_Ayush
            elif username == "Sachin":
                salary_data = salary_sachin
            elif username == "Aditya":
                salary_data = salary_Aditya

            if sal == "1":
                k = int(input("Enter your month number (1 to 10 as 1 for jan...): "))
                if 1 <= k <= 10:
                    print("Salary for month", k,"th", "is:", salary_data[k - 1])
                else:
                    print("Invalid month number")
            else:
                for amount in salary_data:
                    print(amount)

        elif choice == "3":
            print("Leaves taken this week:")

            if username == "Souvik":
                for item in leaves_souvik:
                    print(item)
            elif username == "Pruthvi":
                for item in leaves_pruthvi:
                    print(item)
            elif username == "Ayush":
                for item in leaves_ayush:
                    print(item)
            elif username == "Sachin":
                for item in leaves_sachin:
                    print(item)
            elif username == "Aditya":
                for item in leaves_aditya:
                    print(item)

        elif choice == "4":
            print("BYE", username, "Meet you tomorrow.")
            break

        else:
            print("Invalid option! Try again.")

else:
    print("YOU ARE AN INTRUDER! BHAG JA YAHAN SE!")




