import numpy as np


def theorem4(func: list) -> float | str:
    function = np.array(func)

    if min(function) >= 0 or max(function) <= 0:
        return 'Нельзя применить теорему'

    if function[0] < 0:
        function *= -1

    a_index = 0

    for index, a in enumerate(function, start=1):
        if a < 0:
            a_index = index
            break

    return 1 + float(function[function < 0].min() / -function[0]) ** (1 / (len(function) - 1 - a_index))


print(theorem4([1, 2, -5, 8, -7, -3]))
