# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# - 12,096 -> 26 


def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def count_digits(numb: int) -> int:
    sum = 0
    while numb > 0:
        digit = int(numb % 10)
        sum += digit
        numb //= 10
    return sum


def count_digits_float(numb: float) -> int:
    str_list = str(numb).split('.')
    return count_digits(int(str_list[0])) + count_digits(int(str_list[1]))


number = input('Введите число -> ')
while not is_float(number):
    number = input('Wrong input. Try again -> ')
number = float(number)

print(count_digits_float(number))