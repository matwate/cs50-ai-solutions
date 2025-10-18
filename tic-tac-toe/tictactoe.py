"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if countx(board) == counto(board) else O


def countx(board):
    count = 0
    for row in board:
        for cell in row:
            if cell == X:
                count += 1
    return count


def counto(board):
    count = 0
    for row in board:
        for cell in row:
            if cell == O:
                count += 1
    return count


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    x = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                x.add((i, j))
    return x


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)
    board = copy.deepcopy(board)
    board[action[0]][action[1]] = player_turn
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not None and checkrow(board, i):
            return board[i][0]
        if board[0][i] is not None and checkcol(board, i):
            return board[0][i]
    if board[0][0] is not None and checkdiag1(board):
        return board[0][0]
    if board[0][2] is not None and checkdiag2(board):
        return board[0][2]
    return None


def checkrow(board, row):
    return all(board[row][i] == board[row][0] for i in range(3))


def checkcol(board, col):
    return all(board[i][col] == board[0][col] for i in range(3))


def checkdiag1(board):
    return all(board[i][i] == board[0][0] for i in range(3))


def checkdiag2(board):
    return all(board[i][2 - i] == board[0][2] for i in range(3))


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        _, move = maximize(board)
    else:
        _, move = minimize(board)
    return move


def maximize(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    move = None
    for action in actions(board):
        min_value, _ = minimize(result(board, action))
        if min_value > v:
            v = min_value
            move = action
            if v == 1:
                break
    return v, move


def minimize(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        max_value, _ = maximize(result(board, action))
        if max_value < v:
            v = max_value
            move = action
            if v == -1:
                break
    return v, move
