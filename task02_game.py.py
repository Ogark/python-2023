import random

def main():
    print("Ласкаво просимо до гри!")
    print("Виберіть, камінь (1), ножиці (2) чи папір (3):")

    user_choice = input("Введіть 1, 2, 3: ")
    user_choice = user_choice.strip()

    if user_choice not in ('1', '2', '3'):
        print("Невірний вибір. Спробуйте ще раз.")
        return

    user_choice = int(user_choice)
    computer_choice = random.randint(1, 3)

    print("Ваш вибір:", user_choice)
    print("Вибір комп'ютера:", computer_choice)

    if user_choice == computer_choice:
        print("Нічия!")
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        print("Ви виграли!")
    else:
        print("Комп'ютер виграв!")

if __name__ == "__main__":
    main()