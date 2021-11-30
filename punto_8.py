#!/usr/bin/python3
""" Concatenate two vectors.

"""


def F(string_list, number_list):
    """ This function concatenates two interleaved vectors.
    """
    concat_list = string_list + number_list
    pair = 0
    odd = 1
    for number in string_list:
        concat_list[pair] = number
        pair += 2
        if pair >= len(concat_list):
            pair -= 1
    for number in number_list:
        concat_list[odd] = number
        odd += 2
        if odd > pair:
            odd -= 1
    return concat_list


print(F(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], [1, 2, 3, 4, 5, 6, 7]))
