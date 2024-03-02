def find_max_limit(an: float, a: float) -> float:
    return 1 + a / abs(an)


def find_min_limit(a0: float, b: float) -> float:
    return 1 / (1 + b / abs(a0))


def theorem3(func: list) -> tuple[float, float]:
    a_list = []

    for number in func:
        a_list.append(abs(number))

    return (find_min_limit(a_list[-1], max(a_list[0:-1])),
            find_max_limit(a_list[0], max(a_list[1:-1])))


root_limits = theorem3([1, 2, -5, 8, -7, -3])

print(f"{root_limits[0]} < |root| <= {root_limits[1]}")
