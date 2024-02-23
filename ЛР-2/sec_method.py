def simple_stop_criteria(absolute_value: float, epsilon: float) -> bool:
    return absolute_value < epsilon


def calc_y(func: list, x: float) -> float:
    args = [func[0], ]

    for index, value in enumerate(func[1:], start=1):
        args.append(value * (x ** index))

    return sum(args)


def calc_x(func: list, x: float, xn: float) -> float:
    return xn - ((calc_y(func, xn) * (xn - x)) / (calc_y(func, xn) - calc_y(func, x)))


def seq_method(func: list, initial_approx: float, xn: float, stop_criteria: callable, epsilon: float) -> float:
    x = calc_x(func, initial_approx, xn)

    stop_absolute_value = abs(x - initial_approx)

    while stop_criteria(stop_absolute_value, epsilon) is False:
        x, initial_approx = calc_x(func, x, initial_approx), x

        stop_absolute_value = abs(x - initial_approx)

    return x


initial = 0
x_n = 0.5  # не равное 0
eps = 0.01
function = [-6, 11, -6, 1]  # для (x-1)(x-2)(x-3) = 0

answer = seq_method(function, initial, x_n, simple_stop_criteria, eps)
print(f"Корень, найденный методом секущих,: {answer}. Что ≈ {round(answer)}")
