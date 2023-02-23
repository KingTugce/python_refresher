number = 8
user_input = input("if you wanna play say 'y' ").lower()

if user_input == "y":
    user_number = int(input("enter a number "))
    if user_number == number:
        print("You win")
    elif abs(number - user_number) == 1:
        print("you were off by one.")
    else:
        print("try again!")