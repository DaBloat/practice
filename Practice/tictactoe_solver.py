# TicTacToe Game
# Return numbers -1 if no winner and still has empty slots
# 0 if its a draw with all the slots are not empty
# 1 if 'X' or '1' won the game
# 2 if 'O' OR '2' won the game
# 3 ways to win
# check vertical lines  3 lines
# check horizontal lines 3 lines
# check a diagonals 2 diagonals

def is_solved(board):
    # vertical check
    for row in list(zip(*board)):
        if len(list(set(row))) == 1:
            if list(set(row))[0] != 0:
                return list(set(row))[0]

    # diagonal check
    fdiag = []
    bdiag = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j:
                fdiag.append(board[i][j])
        for k in reversed(range(len(board[i]))):
            if abs(k - i) == 2:
                bdiag.append(board[i][k])
            if k == 1 and i == 1:
                bdiag.append(board[i][k])

    for diag in [fdiag, bdiag]:
        if len(list(set(diag))) == 1:
            if list(set(diag))[0] != 0:
                return list(set(diag))[0]

    # horizontal check
    for row in board:
        if len(list(set(row))) == 1:
            if list(set(row))[0] != 0:
                return list(set(row))[0]
    
    # check if done playing or not
    finish = -1
    for i in board:
        if 0 not in i:
            finish = 0
        else:
            finish = -1
            break
    return finish




print(is_solved([[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]))

print(is_solved([[1, 1, 1],
                 [0, 2, 2],
                 [0, 0, 0]]))


print(is_solved([[1, 1, 2],
                 [0, 1, 2],
                 [0, 0, 2]]))


print(is_solved([[1, 2, 1],
                 [0, 1, 2],
                 [0, 0, 1]]))


print(is_solved([[1, 2, 1],
                 [1, 2, 2],
                 [2, 1, 1]]))

print(is_solved([[2,0,2],
                 [2,1,1],
                 [1,2,1]]))

print(is_solved([[1,2,1],
                 [1,1,2],
                 [2,2,0]]))

print(0 in [2,2,0])
