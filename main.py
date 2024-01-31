cell = [[' ',' ',' '] for i in range(3)]
combinatons=[]
def takeTurn():
    while True:
        turn = input('Система: Введите координаты через пробел:').split()

        if len(turn) != 2:
            print('Система: Необходимо ввести  2 координаты через пробел')
            continue
        x,y = turn
        if  not (x.isdigit()) or not (y.isdigit()):
            print('Система: Координаты должны быть целыми числами')
            continue
        x,y = int(x),int(y)
        if any([x<0,x>2,y<0,y>2]):
            print('Система: Координаты должны быть в диапазоне [0,2]')
            continue
        if cell[x][y]!=' ':
            print('Система: Клетка с введенными координатами занята')
            continue
        return x,y

def displayBoard():
    print(" | 0 | 1 | 2 |")
    print("__________________")
    for i in range(3):
        print(f"{i}| {cell[i][0]} | {cell[i][1]} | {cell[i][2]} |")
        print("__________________")

def checkCombinations():
    for n in range(3):
        combinatons.append(check_line(cell[n][0], cell[n][1], cell[n][2]))
        combinatons.append(check_line(cell[0][n], cell[1][n], cell[2][n]))
    combinatons.append(check_line(cell[0][0], cell[1][1], cell[2][2]))
    combinatons.append(check_line(cell[2][0], cell[1][1], cell[0][2]))
    if any(combinatons):
        return True
    else:
        return False

def check_line(c1,c2,c3):
    if all([c1==c2, c2 == c3, c3==c1]):
        if  c1 == "X":
            print("Система: Выиграл X")
            return True
        if  c1 == "0":
            print("Система: Выиграл 0")
            return True
    return False


counter = 0


while True:
    while True:
        counter += 1
        print(f'Ход номер:{counter}')
        displayBoard()
        if counter % 2 != 0:
            print('Ходит крестик')
        else:
            print('Ходит нолик')
        x, y = takeTurn()

        if counter % 2 != 0:
            cell[x][y] = 'X'
        else:
            cell[x][y] = '0'

        if checkCombinations():
            displayBoard()
            break
        if counter == 9:
            print('Ничья')
            break

    end_point=input('Система: Чтобы прододжить играть нажмите Enter, для выхода нажмите ВЫХОД: ')
    if end_point == 'STOP':
        break
