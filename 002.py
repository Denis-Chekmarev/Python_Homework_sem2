# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def getNumber(text: str) -> int:
    while True:
        numb = input(text)
        if numb.isdigit():
            numb = int(numb)
            return numb


def get_list(N: int) -> list:
    res = [1]
    for index in range(N-1):
        res.append(res[index] * (index + 2))
    return res


N = getNumber('Input a number -> ')
print(get_list(N))
