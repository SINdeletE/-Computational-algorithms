import copy

x_column = [[0], [1], [2], [3], [4]]
y_column = [[0], [1], [2], [3], [4]]
z_column = [[0], [1], [2], [3], [4]]

def c_1(x: list, y: list, c_0: float):
    h_1 = x[1] - x[0]
    h_2 = x[2] - x[1]
    
    A_1 = h_1
    B_1 = 2 * (h_1 + h_2)
    C_1 = h_2
    F_1 = 6 * ((y[2] - y[1]) / h_2 - (y[1] - y[0]) / h_1)

    c_1 = F_1 / (C_1 + B_1)

    return c_1
    
def c_next(x: list, y: list, c: list):
    h_i = x[1] - x[0]
    h_i_next = x[2] - x[1]
    
    A_i = h_i
    B_i = 2 * (h_i + h_i_next)
    C_i = h_i_next
    F_i = 6 * ((y[2] - y[1]) / h_i_next - (y[1] - y[0]) / h_i)

    c_i_next = F_i - A_i * c[0] - B_i * c[1]

    return c_i_next

def c_list(x: float, y: float, n: int):
    c_list_tmp = []

    for i in range(n - 1):
        if i == 0 or (i + 1) == n:
            c_list_tmp.append(0)
        else:

            if i == 1:
                x_012 = [x[0], x[1], x[2]]
                y_012 = [y[0], y[1], y[2]]

                c = c_1(x_012, y_012, c_list_tmp[0])

                c_list_tmp.append(c)

            x_list = [x[i - 1], x[i], x[i + 1]]
            y_list = [y[i - 1], y[i], y[i + 1]]
            c_list = [c_list_tmp[i - 1], c_list_tmp[i]]

            c = c_next(x_list, y_list, c_list)

            c_list_tmp.append(c)

    c_list_tmp.append(0) # i == n

    return c_list_tmp

def d_list(x: list, y: list, c: list, n: int):
    d_list_tmp = []

    for i in range(n):
        if i == 0:
            d_list_tmp.append(0)
        else:
            h_i = x[i] - x[i - 1]

            d = (c[i] - c[i - 1]) / (3 * h_i)
            d_list_tmp.append(d)
    
    return d_list_tmp

def b_list(x: list, a: list, n: int):
    b_list_tmp = []

    for i in range(n):
        if i == 0:
            b_list_tmp.append(0)
        else:
            h_i = x[i] - x[i - 1]

            d = (a[i] - a[i - 1]) / h_i
            b_list_tmp.append(d)
    
    return b_list_tmp

def end_index(x_list: list, x: float):
    i = 1
    while i < len(x_list) and x < x_list[i]:
        i += 1
    
    return i

def polynome_x_multi(x: float, xi: float, n: int):
    return (x - xi) ** n

def polynome_value(a, b, c, d, x, xi):
    result = a
    result += b * polynome_x_multi(x, xi, 1)
    result += c * polynome_x_multi(x, xi, 2)
    result += d * polynome_x_multi(x, xi, 3)

    return result

def spline_interpolation(data: list, x: float, n: int):
    x_list = [stroke[0] for stroke in data]
    y_list = [stroke[1] for stroke in data]
    
    c = c_list(x_list, y_list, len(x_list))
    d = d_list(x_list, y_list, c, len(x_list))
    a = copy.deepcopy(y_list)
    b = b_list(x_list, a, len(x_list))

    i = end_index(x_list, x)

    result = polynome_value(a[i], b[i], c[i], d[i], x, x_list[i - 1])

    return result

def y_u_configure(field_data: list, j: int):
    y_u = copy.deepcopy(y_column)

    for i in range(len(field_data)):
        y_u[i].append(field_data[i][j])

    return y_u

def spline_field_interpolation(field_data: list, x: float, y: float, nx, ny):
    x_u = copy.deepcopy(x_column)

    for j in range(len(field_data[0])):
        y_u = y_u_configure(field_data, j)
        u = spline_interpolation(y_u, y, ny)

        x_u[j].append(u)

    u = spline_interpolation(x_u, x, nx)

    return u

def spline_cube_interpolation(cube_data: list, x: float, y: float, z: float, nx, ny, nz):
    z_u = copy.deepcopy(z_column)

    for i in range(len(z_u)):
        u = spline_field_interpolation(cube_data[i], x, y, nx, ny)

        z_u[i].append(u)

    result = spline_interpolation(z_u, z, nz)

    return result

