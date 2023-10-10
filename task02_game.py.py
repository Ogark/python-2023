# Користовучу пропонується пограти у гру камінь, ножиці, папір з комп'ютером
# Гра реалізується за допомогою функції random тому переможець у грі визначається випадковим чином

import random

def main():
    print("Welcome to the game!")
    print("Choose rock (1), scissors (2) or paper (3):")

    user_choice = input("Enter 1, 2, 3: ")
    user_choice = user_choice.strip()

    if user_choice not in ('1', '2', '3'):
        print("Wrong choice. Try again.")
        return

    user_choice = int(user_choice)
    computer_choice = random.randint(1, 3)

    print("Your choice:", user_choice)
    print("Choosing a computer:", computer_choice)

    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        print("You won!")
    else:
        print("The computer won!")

if __name__ == "__main__":
    main()