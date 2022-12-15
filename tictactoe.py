import numpy as np

table = np.array([[" "," "," "],
                  [" "," "," "],
                  [" "," "," "]])
def display():
    print("   1   2   3")
    print(f"1  {table[0][0]} | {table[0][1]} | {table[0][2]} ")
    print("  --- --- --- ")
    print(f"2  {table[1][0]} | {table[1][1]} | {table[1][2]} ")
    print("  --- --- --- ")
    print(f"3  {table[2][0]} | {table[2][1]} | {table[2][2]} ")

def checker(x):
    count = 0
    possible = [[table[0][i] for i in range(3)],
                [table[1][i] for i in range(3)],
                [table[2][i] for i in range(3)],
                [table[i][0] for i in range(3)],
                [table[i][1] for i in range(3)],
                [table[i][2] for i in range(3)],
                [table[0][0],table[1][1],table[2][2]],
                [table[2][0],table[1][1],table[0][2]]
                ]
    for y in possible:
        for c in y:
            if c==x:
                count+=1
        if count == 3:
            return True
        else:
            count = 0

    return False

print("Hello! welcome to the tic tac toe game , here is your table")
display()

while(" " in table):
    row = int(input("player 1 , the row index where u want to enter 'O' "))
    column = int(input("player 1 , the column index where u want to enter 'O' "))
    if table[row-1][column-1] != " ":
        print("not an empty place")
        continue
    table[row-1][column-1] ='O'
    display()
    if(checker('O')):
        print("player1 has won!")
        exit(1);

    while(True):
        row = int(input("player 2 , the row index where u want to enter 'X' "))
        column = int(input("player 2 , the column index where u want to enter 'X' "))
        if table[row-1][column-1] != " ":
            print("not an empty place")
            continue
        table[row - 1][column - 1] = 'X'
        display()
        if (checker('X')):
            print("player2 has won!")
            exit(1);
        break;

print("table is full , its a draw")