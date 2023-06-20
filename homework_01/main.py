"""
Домашнее задание №1
Функции и структуры данных
"""
from typing import List


def power_numbers(*nums: int) -> List[int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    # return [num ** 2 for num in numbers]
    return list(map(lambda x: x ** 2, nums))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


def filter_numbers(nums: List[int], filter_type: str) -> List[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    res = []
    if filter_type == EVEN:
        res = list(filter(lambda x: x % 2 == 0, nums))
    if filter_type == ODD:
        res = list(filter(lambda x: x % 2 != 0, nums))
    if filter_type == PRIME:
        res = list(filter(lambda x: is_prime(x), nums))

    return res
