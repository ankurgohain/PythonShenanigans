import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 4
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Fonts
pygame.display.set_caption("Tic Tac Toe - Minimax AI")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)

# Board
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                          row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

def evaluate(board):
    for row in board:
        if row.count('X') == 3:
            return +10
        elif row.count('O') == 3:
            return -10
    for col in range(3):
        if [board[r][col] for r in range(3)] == ['X']*3:
            return +10
        elif [board[r][col] for r in range(3)] == ['O']*3:
            return -10
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag1 == ['X']*3 or diag2 == ['X']*3:
        return +10
    elif diag1 == ['O']*3 or diag2 == ['O']*3:
        return -10
    return 0

def is_moves_left(board):
    return any(cell == ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

def best_move():
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def check_winner():
    score = evaluate(board)
    if score == 10:
        return 'X'
    elif score == -10:
        return 'O'
    elif not is_moves_left(board):
        return 'Draw'
    return None

# Add a flag to track if the result has been printed
result_printed = False

# Game loop
draw_lines()
game_over = False
player_turn = True  # Human = O, AI = X

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and player_turn and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

            if board[row][col] == ' ':
                board[row][col] = 'O'
                player_turn = False
                draw_figures()

        if not player_turn and not game_over:
            ai_move = best_move()
            if ai_move != (-1, -1):
                board[ai_move[0]][ai_move[1]] = 'X'
                draw_figures()
                player_turn = True

        result = check_winner()
        if result and not result_printed:
            print(f"Game Over: {result} wins!" if result != 'Draw' else "Game Over: It's a draw!")
            game_over = True
            result_printed = True

    pygame.display.update()

