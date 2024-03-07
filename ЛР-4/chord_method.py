# Пример из учебного пособия Киреева
def equation(x: float) -> float:
    return x**3 - x - 1


def stop_criteria(absolute_value: float, epsilon: float) -> bool:
    return absolute_value < epsilon


def chord_method(func: callable, a: float, b: float, epsilon: float) -> float | str:
    if func(a) * func(b) >= 0:
        return "Границы интервала должны иметь разные знаки"

    root = a - (b - a) * func(a) / (func(b) - func(a))

    while stop_criteria(abs(func(root)), epsilon) is False:
        if func(a) * func(root) < 0:
            b = root
        else:
            a = root

        root = a - (b - a) * func(a) / (func(b) - func(a))

    return root


result = chord_method(equation, -2, 2, 1e-6)
print(f"Корень: {result}")
