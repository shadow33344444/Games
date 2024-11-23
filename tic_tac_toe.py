#НАЧАЛЬНАЯ МАТРИЦА
matrix = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def won(matrix): #Проверка на победу
    for i in range(1):
        for j in range(1):
            if matrix[i][j] == matrix[i + 1][j + 1] == matrix[i + 2][j + 2] != " ":
                print("Победил игрок, который использовал " + matrix[i][j])
                return True
            if matrix[i][3 - i - 1] == matrix[i + 1][3 - i - 2] == matrix[i + 2][3 - i - 3] != " ":
                print("Победил игрок, который использовал " + matrix[i][j])
                return True
            if matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2] != " ":
                print("Победил игрок, который использовал " + matrix[i][j])
                return True
            if matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j] != " ":
                print("Победил игрок, который использовал " + matrix[i][j])
                return True
    return False

def draw():
    pass


#Вывод поля
def board(matrix):
    a = [[],
         [],
         []]
    print('_' * 12)
    for i in range(3):
        string = ' ' + "1" + ' ' + "|" + ' ' + "1" + ' ' + "|" + ' ' + "1" + ' ' + "|"
        a[i] = string

    for i in range(3):
        for j in range(3):
            a[i] = a[i].replace("1", matrix[i][j], 1)



    print(*a, sep='\n')
    print("-" * 12)
    return ''

def pomenyat_ZNACHENIE(matrix, q):
    a = int(input("Введите номер строки"))
    b = int(input("Введите номер столбца"))
    matrix[a][b] = q
    return ''


#Начало игры(САМА ИГРА ТИПА РАБОТАЕТ ТУТ)
q = ""
c = 0
board(matrix)
while won(matrix) != True:
    if c % 2 == 0:
        q = "X"
    else:
        q = "O"
    pomenyat_ZNACHENIE(matrix, q)
    won(matrix)
    board(matrix)
    c += 1
