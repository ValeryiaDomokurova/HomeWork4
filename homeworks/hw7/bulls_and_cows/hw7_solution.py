import random


def secret_number():

    return ''.join(random.sample('0123456789', 4))


def check_gamer(secret, gamer):

    bulls = 0
    cows = 0

    for i in range(4):
        if gamer[i] == secret[i]:
            bulls += 1

    for x in guess:
        if x in secret:
            cows += 1

    cows -= bulls
    return bulls, cows


if __name__ == "__main__":
    secret_num = secret_number()
    print("Компьютер загадал число")

    while True:
        guess = input("Введите 4 цифры без повторений: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Нужно ввести 4 цифры!")
            continue

        if len(set(guess)) != 4:
            print("Цифры не должны повторяться!")
            continue

        bulls, cows = check_gamer(secret_num, guess)

        print(f"Быки: {bulls}, Коровы: {cows}")

        if bulls == 4:
            print(f"Поздравляем! Вы угадали число {secret_num}")
            break
