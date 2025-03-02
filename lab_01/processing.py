def table_title_output():
    x = "x"
    y = "y"
    y_der = "y_der"
    y_der2 = "y_der2"
    print(f"|{x:^15}|{y:^15}|{y_der:^15}|{y_der2:^15}|\n")

def table_str_output(x: float, y: float, y_der: float, y_der2):
    print(f"|{x:^15.2g}|{y:^15.4g}|{y_der:^15.4g}|{y_der2:^15.4g}|\n")

def filedata_read(name: str):
    return 

def menu():
    print("MENU")
    print("1. Посчитать y(x) для заданного значения аргумента x (0.0 - 4.2)")
    print("3. Выйти из программы")

    code = int(input())

    return code

def run():
    flag = True

    while flag:
        action = menu()

        match action:
            case 1:
                pass
            case 3:
                flag = False
            case _:
                print("\nUndefined code\n")
        
    return 0
