def equation(root: float) -> float:
    return (root - 1) * (root - 2) * (root - 3)


def check_stop_criteria(absolute_value: float, epsilon: float) -> bool:
    return absolute_value < epsilon


def dichotomy_method(func: callable, lower_number: float, upper_number: float, epsilon: float) -> float | str:
    if lower_number * upper_number > 0:
        return "Одно из чисел должно быть меньше 0"

    while check_stop_criteria(abs(lower_number-upper_number), epsilon) is False:
        new_x = (lower_number + upper_number) / 2

        if func(new_x) == 0:
            return new_x
        elif func(lower_number) * func(new_x) < 0:
            upper_number = new_x
        else:
            lower_number = new_x

    return (lower_number + upper_number) / 2


print("Корень =", dichotomy_method(equation, -2, 2, 0.01))
