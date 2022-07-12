# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}


def getNumber(text: str) -> int:
    while True:
        numb = input(text)
        if numb.isdigit():
            numb = int(numb)
            return numb


def get_list(num: int) -> int:
    list = []
    for i in range(1, num+1):
        list.append((1 + 1/i)**i)
    return list


numb = getNumber('Input a number -> ')
print(get_list(numb))