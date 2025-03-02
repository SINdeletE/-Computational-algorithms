EPS = 1e-8

def table_title_output():
    x = "x"
    y = "y"
    y_der = "y_der"
    y_der2 = "y_der2"
    print(f"|{x:^15}|{y:^15}|{y_der:^15}|{y_der2:^15}|\n")

def table_str_output(x: float, y: float, y_der: float, y_der2):
    print(f"|{x:^15.2g}|{y:^15.4g}|{y_der:^15.4g}|{y_der2:^15.4g}|\n")

def filedata_read():
    data = []

    f = open("data.txt", "r")

    stroke = f.readline()

    while (stroke := f.readline()) != "":
        stroke = stroke.rstrip()
        stroke = stroke.split()
        stroke = list(map(float, stroke))

        data.append(stroke)

    f.close()

    return data

def matrix_output(matrix: list):
    for i in range(len(matrix)):
        print(*matrix[i])

def find_range(data: list, x: float, n: int):
    left = 0
    right = left + n

    if (x < -EPS or x - 4.2 > EPS):
        return None

    flag = True
    while flag and right < len(data) - 1:
        if x - data[right][0] <= EPS:
            flag = False
        else:
            left += 1
            right += 1

    if right < len(data) - 1:
        left += 1
        right += 1
    
    return left, right

def delta_calculate(x1: float, x2: float, y1: float, y2: float):
    return (y2 - y1) / (x2 - x1)

def matrix_end_get(data: list, x: float, n: int):
    matrix_end = [] * (n + 1)
    left, right = find_range(data, x, n)

    # Добавляем X
    for i in range(left, right + 1):
        matrix_end.append([data[i][0]])

    # Добавляем Y
    for i in range(left, right + 1):
        matrix_end[i - left].append(data[i][1])

    args_shift = 1
    for iter in range(2, n + 2):
        for i in range(n - iter + 2):
            x1 = matrix_end[i][0]
            x2 = matrix_end[i + args_shift][0]
            y1 = matrix_end[i][iter - 1]
            y2 = matrix_end[i + 1][iter - 1]

            matrix_end[i].append(delta_calculate(x1, x2, y1, y2))

        args_shift += 1

    return matrix_end

def x_multi_get(matrix_end: list, count: int, x: float):
    c_list = matrix_end[0]
    res = 1

    for i in range(count):
        res *= x - matrix_end[i][0]
    
    return res

def res_by_matrix_end(matrix_end: list, x: float):
    c_list = matrix_end[0]
    res = 0

    for i in range(len(matrix_end)):
        x_multi = x_multi_get(matrix_end, i, x)
        res += c_list[i + 1] * x_multi

    return res

def newton_interpolation(data: list, x: float, n: int):
    matrix_end = matrix_end_get(data, x, n)
    
    print("\nКонфигурация")
    matrix_output(matrix_end)

    result = res_by_matrix_end(matrix_end, x)
    print("\nРезультат:", result)

def menu():
    print("MENU")
    print("1. Посчитать y(x) для заданного значения аргумента x (0.0 - 4.2) полиномом Ньютона")
    print("3. Выйти из программы")

    code = int(input())

    return code

def run():
    flag = True

    data = list()
    data = filedata_read()

    while flag:
        action = menu()

        match action:
            case 1:
                x = float(input("X: "))
                n = int(input("N: "))
                newton_interpolation(data, x, n)

                pass
            case 3:
                flag = False
            case _:
                print("\nUndefined code\n")
        
    return 0
