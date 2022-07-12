# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def getNumber(text: str) -> int:
    while True:
        numb = input(text)
        if numb.isdigit():
            numb = int(numb)
            return numb


def get_random_list(size: int, min=-100, max=101) -> list:
    list_number = []
    for i in range(size):
        list_number.append(randint(min, max))
    return list_number


def get_mult(numbers: list) -> int:
    indexes = input(
        'Which positions you want to read (input through space) -> ')
    indexes = indexes.split(' ')
    multiplication = 1
    for i in indexes:
        try:
            multiplication *= numbers[int(i)]
        except ValueError:
            print(f'"{i}" is not integer')
        except IndexError:
            print(f'"{i}" goes out of range')
    return multiplication


def get_mult_from_file(numbers: list, filename='file.txt') -> int:
    with open(filename) as file:
        multiplication = 1
        for line in file:
            try:
                multiplication *= numbers[int(line)]
            except ValueError:
                print(f'"{line}" is not integer in file')
            except IndexError:
                print(f'"{line}" goes out of range')
    return multiplication


size = getNumber('Input the size of list -> ')
list_numbers = get_random_list(size, -size, size+1)
print(list_numbers)
print(f'Result = {get_mult_from_file(list_numbers)}')
