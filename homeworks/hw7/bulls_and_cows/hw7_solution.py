import random


def generate_secret_number():

    return ''.join(random.sample('0123456789', 4))


def check_guess(secret, user_guess):

    bulls_count = 0
    cows_count = 0

    for i in range(4):
        if user_guess[i] == secret[i]:
            bulls_count += 1

    for x in user_guess:
        if x in secret:
            cows_count += 1

    cows_count -= bulls_count
    return bulls_count, cows_count


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

        res_bulls, res_cows = check_guess(SECRET_NUM, guess)

        print(f"Быки: {res_bulls}, Коровы: {res_cows}")

        if res_bulls == 4:
            print(f"Поздравляем! Вы угадали число {SECRET_NUM}")
            break
