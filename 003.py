# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [4, 7, 10, 13, 16, 19}

def getNumber(text: str) -> int:
    while True:
        numb = input(text)
        if numb.isdigit():
            numb = int(numb)
            return numb


def get_list(num: int) -> int:
    list = []
    for i in range(1, num):
        list.append((1 + 1/i)**i)
    return list


numb = getNumber('Input a number -> ')
print(get_list(numb))