# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности
# Реализуйте алгоритм перемешивания списка


import time


# Самописная функция получения рандомного натурального числа 
def get_random_nature_int(min: int, max: int) -> int:
    nano_sec = str(time.time_ns())[10:-2]
    time.sleep(0.002)
    distance = max - min
    result = int(nano_sec[int(len(nano_sec))-distance:])
    result += min
    if result > max:
        result = result % max
        if result < min: result += min
    return(result)


# Функция перемешивания значений листа, количество перестановок указывается параметром repeat
def shake_list(origin_list: list, repeat=50) -> list:
    new_list = origin_list[:]
    for index in range(repeat):
        x = get_random_nature_int(0, len(new_list))
        y = get_random_nature_int(0, len(new_list))
        new_list[x], new_list[y] = new_list[y], new_list[x]
    return new_list


example_list = []
for index in range(10):
    example_list.append(index+1)  # Создаем отсортированный лист для примера от 1 до 10

print(example_list)
print(shake_list(example_list))
