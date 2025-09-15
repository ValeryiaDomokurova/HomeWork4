import random

SECRET_NUM = ''.join(random.sample('0123456789', 4))
print("Компьютер загадал число")

while True:
    gamer = input("Введи 4 цифры без повторений: ")

    if len(gamer) != 4 or not gamer.isdigit():
        print("Нужно ввести 4 цифры ")
        continue

    if len(set(gamer)) != 4:
        print("Цифры не должны повторяться ")
        continue

    BULLS = 0
    for i in range(4):
        if gamer[i] == SECRET_NUM[i]:
            BULLS += 1

    COWS = 0
    for x in gamer:
        if x in SECRET_NUM:
            COWS += 1
    COWS -= BULLS

    if BULLS == 4:
        print(f"Поздравляю! Ты угадал число {SECRET_NUM}!")
        break

    print(f"Быки: {BULLS} , Коровы: {COWS}")
