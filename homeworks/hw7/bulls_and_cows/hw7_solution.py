import random

secret_num = ''.join(random.sample('0123456789', 4))
print("Компьютер загадал число")

while True:
    gamer = input("Введи 4 цифры без повторений ")

    if len(gamer) != 4 or not gamer.isdigit():
        print("Нужно ввести 4 цифры ")
        continue

    if len(set(gamer)) != 4:
        print("Цифры не должны повторяться ")
        continue

    bulls = 0
    for i in range(4):
        if gamer[i] == secret_num[i]:
            bulls += 1

    cows = 0
    for x in gamer:
        if x in secret_num:
            cows += 1
    cows -= bulls

    if bulls == 4:
        print(f"Поздравляю! Ты угадал число {secret_num}!")
        break
    else:
        print(f"Быки: {bulls} , Коровы: {cows}")
