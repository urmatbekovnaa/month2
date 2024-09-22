from random import randint
from decouple import config


num1 = int(config('DIAPASON'))
num2 = int(config('DIAPASONDVA'))
balance = int(config('START_CAPITAL'))

def logic():

    global balance
    print(' Угадай число!')
    print("Я загадала число от", num1, "до", num2)
    print(f'Ваш баланс: {balance}')



    while balance > 0:
        secret = randint(num1, num2)
        print("Введите число:")
        number = int(input())
        if number < num1 or number > num2:
            print("Неверный ввод")
            continue

        print("Ваша ставка:")
        suma = int(input())
        if suma > balance or suma < 1:
            print("Неверный ввод")
            continue

        if number == secret:
            print(f"Вы угадали число: {secret} и получили {suma} баллов\n")
            balance += suma
        else:
            print(f"Вы не угадали число: {secret} и потеряли {suma} баллов\n")
            balance -= suma

        if balance > 0:
            play = input(f'Хотите сыграть еще? Ваш баланс: {balance}.\n(yes/no)')
            if play == 'yes':
                continue
            elif play == 'no':
                break
        else:
            print("У вас закончились баллы.")

    print("\nИгра завершена. Ваш баланс:", balance)

if __name__ == '__main__':
    logic()


