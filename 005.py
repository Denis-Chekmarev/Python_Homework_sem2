# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности


import time


def count_digits(numb: int) -> int:
    sum = 0
    while numb > 0:
        digit = int(numb % 10)
        sum += digit
        numb //= 10
    return sum


def get_random_int(min: int, max: int, sleeping=0.002) -> int:
    nano_sec = str(time.time_ns())[10:-2]
    # time.sleep(sleeping)
    distance = max - min
    result = int(nano_sec[int(len(nano_sec))-distance:])
    result %= max
    return(result)


print(get_random_int(50, 200))
