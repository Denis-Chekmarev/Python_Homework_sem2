org_str = 'Hello world world wor    w o r '
find_str = 'worl'


def count_substring(text: str, substring: str) -> int:
    amount = 0
    for index in range(0, len(text)):
        if text[index] == substring[0]:
            for j in range(1, len(substring)):
                try:
                    if substring[j] != text[index+j]:
                        flag = False
                    else:
                        flag = True
                except IndexError:
                    flag = False
            if flag:
                amount += 1
    return amount


print(count_substring(org_str, find_str))

