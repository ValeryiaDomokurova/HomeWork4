import random


def generate_secret_number():

    return ''.join(random.sample('0123456789', 4))

def check_guess(secret, guess):

    BULLS = 0
    COWS = 0

    for i in range(4):
        if guess[i] == secret[i]:
            BULLS += 1

    for x in guess:
        if x in secret:
            COWS += 1

    COWS -= BULLS
    return BULLS, COWS


if __name__ == "__main__":
    SECRET_NUM = generate_secret_number()
    print("Компьютер загадал число")

    while True:
        guess = input("Введите 4 цифры без повторений: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Нужно ввести 4 цифры!")
            continue

        if len(set(guess)) != 4:
            print("Цифры не должны повторяться!")
            continue

        BULLS, COWS = check_guess(SECRET_NUM, guess)

        print(f"Быки: {BULLS}, Коровы: {COWS}")

        if BULLS == 4:
            print(f"Поздравляем! Вы угадали число {SECRET_NUM}")
            break
