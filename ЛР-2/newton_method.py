# Простой критерий останова
def simple_stop_criteria(absolute_value: float, epsilon: float) -> bool:
    return absolute_value < epsilon


# Поиск производной
def calc_derivative(func: list) -> list:
    derivative = []

    for index, value in enumerate(func[1:], start=1):
        derivative.append(index * value)

    return derivative


def calc_y(func: list, x: float) -> float:
    args = [func[0], ]

    for index, value in enumerate(func[1:], start=1):
        args.append(value * (x ** index))

    return sum(args)


def calc_x(func: list, x: float) -> float:
    return x - (calc_y(func, x) / calc_y(calc_derivative(func), x))


def newton_method(func: list, initial_approx: float, stop_criteria: callable, epsilon: float) -> float:
    x = calc_x(func, initial_approx)

    stop_absolute_value = abs(x - initial_approx)

    while stop_criteria(stop_absolute_value, epsilon) is False:
        x, initial_approx = calc_x(func, x), x

        stop_absolute_value = abs(x - initial_approx)

    return x


initial = 0
eps = 0.01
function = [-6, 11, -6, 1]  # для (x-1)(x-2)(x-3) = 0

answer = newton_method(function, initial, simple_stop_criteria, eps)
print(f"Корень, найденный методом Ньютона,: {answer}. Что ≈ {round(answer)}")
