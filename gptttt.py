# Начальная матрица
matrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Проверка на победу
def won(matrix):
    # Проверка строк и столбцов
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != " ":  # Строка
            print(f"Победил игрок, который использовал {matrix[i][0]}")
            return True
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != " ":  # Столбец
            print(f"Победил игрок, который использовал {matrix[0][i]}")
            return True

    # Проверка диагоналей
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":  # Главная диагональ
        print(f"Победил игрок, который использовал {matrix[0][0]}")
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":  # Побочная диагональ
        print(f"Победил игрок, который использовал {matrix[0][2]}")
        return True

    return False

# Проверка на ничью
def draw(matrix):
    for row in matrix:
        if " " in row:  # Если есть хотя бы одна пустая клетка
            return False
    print("У вас ничья!")
    return True

# Отрисовка игрового поля
def board(matrix):
    print("_" * 13)
    for row in matrix:
        print("| " + " | ".join(row) + " |")
        print("_" * 13)

# Изменение значения в матрице
def change_value(matrix, symbol):
    while True:
        try:
            row = int(input("Введите номер строки (1-3): ")) - 1
            col = int(input("Введите номер столбца (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and matrix[row][col] == " ":
                matrix[row][col] = symbol
                break
            else:
                print("Некорректный ввод или ячейка уже занята. Попробуйте снова.")
        except ValueError:
            print("Введите числа от 1 до 3.")

# Главный цикл игры
def main():
    symbol = "X"
    move_count = 0
    board(matrix)

    while True:
        print(f"Ход игрока с символом {symbol}")
        change_value(matrix, symbol)
        board(matrix)
        move_count += 1

        if won(matrix):  # Победа
            break
        if draw(matrix):  # Ничья
            break

        # Переключение между X и O
        symbol = "O" if symbol == "X" else "X"

# Запуск игры
main()
