import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
RED = (255,0,0)
BOARD_ROWS = 3
BOARD_COLS = 3
SAUQRE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SAUQRE_SIZE//4
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SAUQRE_SIZE//4
BG_COLOR = (24,170,156)
LINE_COLOR = (23,145,135)
CIRCLE_COLOR = (239,231,200)
CROSS_COLOR = (66,66,66)
X = 600
Y = 600
#Board AYMEN
board = np.zeros((BOARD_ROWS,BOARD_COLS))
#print(board)


display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AYMEN TIKTAKTOE #1")
screen.fill(BG_COLOR)
font = pygame.font.Font(None, 32)
text = font.render('AYMEN DEV', True, CIRCLE_COLOR)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)


#pygame.draw.line(screen,RED,(10,10),(300,300),10)

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SAUQRE_SIZE), (WIDTH, SAUQRE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2*SAUQRE_SIZE), (WIDTH, 2*SAUQRE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SAUQRE_SIZE, 0), (SAUQRE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2*SAUQRE_SIZE, 0), (2*SAUQRE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int( col * SAUQRE_SIZE + SAUQRE_SIZE // 2 ),int( row * SAUQRE_SIZE + SAUQRE_SIZE // 2 )),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE, row * SAUQRE_SIZE + SAUQRE_SIZE - SPACE),(col * SAUQRE_SIZE + SAUQRE_SIZE - SPACE, row * SAUQRE_SIZE + SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE, row * SAUQRE_SIZE + SPACE),(col * SAUQRE_SIZE + SAUQRE_SIZE - SPACE , row * SAUQRE_SIZE + SAUQRE_SIZE - SPACE),CROSS_WIDTH)

def mark_square( row, col, player):
    board[row][col] = player

def available_square(row,col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == board[2][col] == player:
            draw_vertical_winning_ling(col,player)
            return True
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[0][row] == player and board[1][row] == board[2][row] == player:
            draw_horizontal_winning_line(row,player)
            return True
    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board [0][2] == player:
        draw_asc_diagonal(player)
        return True
    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        draw_desc_diagonal(player)
        return False

def draw_vertical_winning_ling(col,player):
    posX = col * SAUQRE_SIZE + SAUQRE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT - 15),15)
def draw_horizontal_winning_line(row,player):
    posY = row * SAUQRE_SIZE + SAUQRE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,posY), (HEIGHT - 15,posY), 15)
def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT - 15), (WIDTH - 15 ,15),15)
def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,15), (WIDTH - 15,HEIGHT - 15), 15)
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] #X
            mouseY = event.pos[1] #Y

            clicked_row = int(mouseY // SAUQRE_SIZE)
            clicked_col = int(mouseX // SAUQRE_SIZE)

            if available_square(clicked_row,clicked_col):

                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()