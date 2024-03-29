# This is a sample Python script.
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from typing import List, Any

import numpy as np
import copy
from numpy import ndarray

###
def Move(grid, row, column, n):
    instruction = input("Please use (L)->Left, (U)->Up, (R)->Right, and (B)->Bottom, and(Q)->quit:")
    print('\n')
    if instruction == 'L' and column - 1 >= 0:
        # start move to left
        grid[row][column] = grid[row][column - 1]
        grid[row][column - 1] = n * n - 1
        column = column - 1

    elif instruction == 'R' and column + 1 < n:
        # start move to right
        grid[row][column] = grid[row][column + 1]
        grid[row][column + 1] = n * n - 1
        column = column + 1

    elif instruction == 'U' and row - 1 >= 0:
        # start move to up
        grid[row][column] = grid[row - 1][column]
        grid[row - 1][column] = n * n - 1
        row = row - 1

    elif instruction == 'B' and row + 1 < n:
        # start move to bottom
        grid[row][column] = grid[row + 1][column]
        grid[row + 1][column] = n * n - 1
        row = row + 1

    elif instruction == 'Q':
        return grid, row, column, 0
    else:
        print('Wrong instruction!!!!')
    return grid, row, column, 1

### print puzzle method ###
def printPuzzle(grid, n):
    for row in range(0, n):
        for column in range(0, n):
            if grid[row][column] == n * n - 1:
                print(" \t", end=' ')
            else:
                print(grid[row][column], "\t", end=' ')
        print("\n")

def find_start(grid, n):
    for row in range(0, n):
        for column in range(0, n):
            if grid[row][column] == n * n - 1:
                return row, column

####Success jugment for 4 situation####
def succesJugement(grid, n, step):
    if grid.all == CreateendpuzzleRA(n).all:
        print('Congratulations,you have sorted row-wise in ascending order with' + step + 'moves')
        return True
    elif grid.all == CreateendpuzzleRD(n).all:
        print('Congratulations,you have sorted row-wise in descending order with' + step + 'moves')
        return True
    elif grid.all == CreateendpuzzleCA(n).all:
        print('Congratulations,you have sorted column-wise in ascending order with' + step + 'moves')
        return True
    elif grid.all == CreateendpuzzleCD(n).all:
        print('Congratulations,you have sorted column-wise in descending order with' + step + 'moves')
        return True

def changePuzzle(grid, row, column, direction, n):
    if direction == 'L':
        # column - 1 >= 0:
        # start move to left
        grid[row][column] = grid[row][column - 1]
        grid[row][column - 1] = n * n - 1
        column = column - 1

    elif direction == 'R':
        # column + 1 < n:
        # start move to right
        grid[row][column] = grid[row][column + 1]
        grid[row][column + 1] = n * n - 1
        column = column + 1

    elif direction == 'U':
        # row - 1 >= 0
        # start move to up
        grid[row][column] = grid[row - 1][column]
        grid[row - 1][column] = n * n - 1
        row = row - 1

    elif direction == 'B':
        # row + 1 < n
        # start move to bottom
        grid[row][column] = grid[row + 1][column]
        grid[row + 1][column] = n * n - 1
        row = row + 1
    return grid, row, column

def toint(martix):
    sum = ''
    for i in range(0,n):
        for j in range(0,n):
            sum = sum + str(martix[i][j]) +'/'

    return sum
###BFS function###
class Puzzle_condition:

    # need use input to change the 'n'
    def __init__(self, puzzleC, rowC, columnC, n,chacr):
        self.condition = puzzleC
        self.row = rowC
        self.column = columnC
        self.parent = None
        self.n = n
        self.chacr = chacr


def bfs(q, v1, v2, list):
    for _ in range(0, len(q)):
        # print(len(q))
        u = q.pop(0)
        # print(u.condition)
        # print(len(q))
        if u.chacr in v2:
            list.append(u)
            v1[u.chacr] = u
            return 1
        if u.chacr not in v1:
            v1[u.chacr] = u
            # go left
            if (u.column - 1) >= 0:
                p1, r, c = changePuzzle(np.array(u.condition), u.row, u.column, "L", u.n)
                chacr = toint(np.array(p1))
                new = Puzzle_condition(np.array(p1), r, c, n, chacr)
                new.parent = copy.deepcopy(u)
                q.append(new)
            # print('the poc', u.column)
            # print('the por', u.row)
            # print(len(q))
            # go right
            if (u.column + 1) < u.n:
                p2, r, c = changePuzzle(np.array(u.condition), u.row, u.column, 'R', u.n)
                chacr = toint(np.array(p2))
                new = Puzzle_condition(np.array(p2), r, c, n, chacr)
                new.parent = copy.deepcopy(u)
                q.append(new)
            # print(len(q))
            # go up
            if (u.row - 1) >= 0:
                p3, r, c = changePuzzle(np.array(u.condition), u.row, u.column, 'U', u.n)
                chacr = toint(np.array(p3))
                new = Puzzle_condition(np.array(p3), r, c, n, chacr)
                new.parent = copy.deepcopy(u)
                q.append(new)

            # go bottom
            if (u.row + 1) < u.n:
                p4, r, c = changePuzzle(np.array(u.condition), u.row, u.column, 'B', u.n)
                chacr = toint(np.array(p4))
                new = Puzzle_condition(np.array(p4), r, c, n, chacr)
                new.parent = copy.deepcopy(u)
                q.append(new)

def CreateendpuzzleRA(dim):
    endpuzzleRA = []
    for i in range(0, dim*dim):
        endpuzzleRA.append(i)
    endpuzzleRA = np.array(endpuzzleRA)
    endpuzzleRA = np.reshape(endpuzzleRA, [dim, dim])
    return endpuzzleRA

def CreateendpuzzleRD(dim):
    endpuzzleRD = []
    for i in range(0, dim*dim):
        endpuzzleRD.append(dim*dim-i-1)
    endpuzzleRD = np.array(endpuzzleRD)
    endpuzzleRD = np.reshape(endpuzzleRD, [dim, dim])
    return endpuzzleRD

def CreateendpuzzleCA(dim):
    endpuzzleCA = []
    for i in range(0, dim):
        for j in range(0, dim*dim, 3):
            endpuzzleCA.append(i+j)
    endpuzzleCA = np.array(endpuzzleCA)
    endpuzzleCA = np.reshape(endpuzzleCA, [dim, dim])
    return endpuzzleCA

def CreateendpuzzleCD(dim):
    endpuzzleCD = []
    for i in range(0, dim):
        for j in range(0, dim*dim, 3):
            endpuzzleCD.append(dim*dim-1-i-j)
    endpuzzleCD = np.array(endpuzzleCD)
    endpuzzleCD = np.reshape(endpuzzleCD, [dim, dim])
    return endpuzzleCD

def Creatpuzzle(dim):
    puzzle = np.arange(dim * dim)
    np.random.shuffle(puzzle)
    puzzle = np.reshape(puzzle, [dim, dim])
    return puzzle

def dbfs(grid, endpuzzle):
    rowS, columnS = find_start(grid, n)
    rowE, columnE = find_start(endpuzzle,n)
    chacrS = toint(grid)
    chacrE = toint(endpuzzle)
    step = -1
    grid = Puzzle_condition(np.array(grid), rowS, columnS, n, chacrS)
    stackS = []
    stackS.append(grid)
    endpuzzle = Puzzle_condition(np.array(endpuzzle), rowE, columnE, n, chacrE)
    stackE = []
    stackE.append(endpuzzle)
    list = []
    used_puzzleS = {}
    used_puzzleE = {}
    start = time.time()
    while stackS and stackE:
        step += 1
        if len(stackS) < len(stackE):
            ret = bfs(stackS, used_puzzleS, used_puzzleE, list)
        else:
            ret = bfs(stackE, used_puzzleE, used_puzzleS, list)
        if ret == 1:
            break
    print('The minimum number of moves to solve was ' + str(step) + ". A list of moves and the after each move is extracted on a log file named 'minimumNBR.txt'")
    wayM = list.pop(0)
    wayS = used_puzzleS[wayM.chacr]
    wayE = used_puzzleE[wayM.chacr]
    while wayS.parent != None:
        list.append(wayS.condition)
        wayS = wayS.parent
    while wayE.parent != None:
        list.insert(0, wayE.condition)
        wayE = wayE.parent
    print("min solution is ")
    i = 1
    f = open('minimumNBR.txt', 'w')
    while list:
        # print("step", i)
        a = list.pop()
        f.write('next step' + '\n')
        for i in range(len(a)):
            f.write(str(a[i]) + '\n')
        # printPuzzle(a, n)
        i += 1
    print('step', step)
    # printPuzzle(endpuzzle.condition, n)
    f.write('step' + str(step) + '\n')
    for i in range(len(endpuzzle.condition)):
        f.write(str(endpuzzle.condition[i]) + '\n')
    f.close
    end = time.time()
    print('running time',end-start)


def end_des(Martix, n):
    cmp = 0
    Tfront = 0
    Tback = 0
    end = Martix.reshape(-1)
    for i in range(0, n*n-1):
        if end[i] > end[i+1]:
            cmp +=1
    for i in range(0, n*n-1):
       if end[i] == 8:
           start = i
    for i in range(0, n):
        Tfront = Martix[0][i] + Martix[i][0] + Tfront
        Tback = Martix[n-1][i] + Martix[i][n-1] + Tback
    if cmp%2 != start%2:
        if Tfront > Tback:
            endpuzzle = CreateendpuzzleCD(n)
        else:
            endpuzzle = CreateendpuzzleCA(n)
    else:
        if Tfront > Tback:
            endpuzzle = CreateendpuzzleRD(n)
        else:
            endpuzzle = CreateendpuzzleRA(n)
    return endpuzzle



# main function
if __name__ == "__main__":

    ###### puzzle size#####

    ###################################
    ##############For test############
    ###################################

    # puzzle = np.arange(n * n).reshape(n, n)
    # puzzle[2][2] = 7
    # puzzle[2][1] = 6
    # puzzle[2][0]=8
    # print("test:")
    # printPuzzle(puzzle, n)
    # endpuzzleRD = CreateendpuzzleRD(n)
    # endpuzzleRA = CreateendpuzzleRA(n)
    # endpuzzleCD = CreateendpuzzleCD(n)
    # endpuzzleCA = CreateendpuzzleCA(n)
    ##############################################
    #######Initialization for random puzzle#######
    #############################################

    while True:
        select = input('Press M if you want to enter the maze manually, or press R if you want to generate the maze automatically')
        n = int(input('Please enter the size of the grid'))
        if select == 'R':
            grid = Creatpuzzle(n)
        else:
            grid = np.array(input('Please manually enter your maze in order from left to right, top to bottom'))
            grid = np.reshape(grid, [n * n])
        printPuzzle(grid, n)
        puzzleS = copy.deepcopy(grid)
        endpuzzle = end_des(grid, n)
        row, column = find_start(grid, n)
        stepm = 0
        while True:
            grid, row, column, give_up = Move(grid, row, column, n)
            printPuzzle(grid, n)
            stepm += 1
            if succesJugement(grid, n, stepm) or give_up == 0:
                break
        dbfs(puzzleS, endpuzzle)
        ask = input('Do you want to play again(Y/N)')
        if ask == 'N':
            break

    # endpuzzle = end_des(puzzle)


    ##############################################
    #######Get the start position#######
    #############################################
    # print('the step to the end is ')
    # dbfs(puzzleS, endpuzzle)
    # print('the step to the ColumnDescending is ')
    # dbfs(puzzle, endpuzzleCD)
    # print('the step to the RowAscending is ')
    # dbfs(puzzle, endpuzzleRA)
    # print('the step to the ColumnAscending is ')
    # dbfs(puzzle, endpuzzleCA)
    # rowS, columnS = find_start(puzzle, n)
    # rowE, columnE = find_start(endpuzzle,n)
    # chacrS = toint(puzzle)
    # chacrE = toint(endpuzzle)




