"""
Tic Tac Toe Player
"""
import math
from copy import deepcopy
X = "X"
O = "O"
player_turn = None
EMPTY = " "


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    end_game = terminal(board)
    if end_game[0]:
        return "end"
    actions = []
    for r in range(3):
        for c in range(3):
            if (board[r][c]) == EMPTY:
                actions.append([r, c])
    return actions


def result(board, action):
    new_board = deepcopy(board)
    user = player(board)
    end_game = terminal(board)
    
    if end_game[0]:
        return "end"
    
    if isinstance(action, tuple):  # Check if action is a tuple (row, col)
        row, col = action
    else:
        row, col = action  # Single value treated as tuple (row, col)

    if new_board[row][col] == EMPTY:
        new_board[row][col] = user
        return new_board
    else:
        return "invalid"





def winner(board, ai_user):
    winner = utility(board, ai_user)    
    if winner == 1: 
            return X
    elif winner == 0:
        return "draw"
    elif winner == -1: 
        return O
    else: 
        return None


def terminal(board):
    # Check for draw condition
    empty_count = sum(1 for row in board for cell in row if cell == EMPTY)
    if empty_count == 0:
        return (True, "draw")
    
    # Check rows and columns for a win
    for i in range(3):
        if len(set(board[i])) == 1 and board[i][0] != EMPTY:
            return (True, board[i][0])

        if len(set(board[r][i] for r in range(3))) == 1 and board[0][i] != EMPTY:
            return (True, board[0][i])
    
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return (True, board[0][0])
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return (True, board[0][2])
    
    # Game is not over
    return (False, " ")

def utility(board, ai_user):
    results = terminal(board)
    if results[0]:
        if results[1] == "draw":
            return 0
        #user should be ai_value
        elif results[1] == X and ai_user == X:
                return 1
        elif results[1] == O and ai_user == O:
                return 1
        else:
                 return -1
    else:
        return None




def minimax(isMaxTurn, maximizerMark, board):
    end_result = terminal(board)
    if end_result[0]:
        return utility(board, maximizerMark)
    scores = []
    for action in actions(board):
        new_board = result(board, action)
        scores.append((minimax(not isMaxTurn, maximizerMark,  new_board)))

    return max(scores) if isMaxTurn else min(scores)

def bestMove(ai_turn, board):
    bestScore = -math.inf
    bestMove = None
    for action in actions(board):
        new_board = result(board, action)
        score = minimax(False, ai_turn, new_board)
        if (score > bestScore):
            bestScore = score
            bestMove = action
    return bestMove