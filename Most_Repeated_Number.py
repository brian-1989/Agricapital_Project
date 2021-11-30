#!/usr/bin/python3
""" Most repeated number.

"""


def f(numbers_list):
    """ This function finds the most repeated number
    in an array of integers.

    """
    my_dict = {}
    my_list = []
    for number in numbers_list:
        my_dict[number] = numbers_list.count(number)
    maximo = max(my_dict.values())
    for key, value in my_dict.items():
        if maximo == value:
            my_list.append(key)
    return max(my_list)


print(f([5, 1, 2, 1, 4, 3, 5, 5, 1]))
