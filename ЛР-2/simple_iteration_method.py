# Ищем решение для x = sqrt(number)

num = 16
x0 = 7
eps = 0.01


# Простой критерий останова
def simple_stop_criteria(absolute_value: float, epsilon: float) -> bool:
    return absolute_value < epsilon


# Одна итерация
def make_iteration(number: float, initial_approx: float) -> float:
    return 0.5 * (initial_approx + (number / initial_approx))


# Реализация
def simple_iteration_method(stop_criteria: callable, number: float, initial_approx: float, epsilon: float) -> float:
    x = make_iteration(number, initial_approx)

    stop_absolute_value = abs(x - initial_approx)

    while stop_criteria(stop_absolute_value, epsilon) is False:
        x, initial_approx = make_iteration(number, x), x

        stop_absolute_value = abs(x - initial_approx)

    return x


answer = simple_iteration_method(simple_stop_criteria, num, x0, eps)

print(f"Корень числа {num} ≈ {answer}")
