import pygame
import sys
import time
from pygame.locals import *

# declaring the global variables
XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255,255,255)
line_color = (0,0,0)
board = [[None]*3,[None]*3,[None]*3]

pygame.init()
fps = 30
CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode((width,height+100))
pygame.display.set_caption("Tic Tac Toe Game")

# load images
initiating_window = pygame.image.load("bg.webp")
x_img = pygame.image.load("x_img.png")
o_img = pygame.image.load("o_img.png")

# resize images
initiating_window = pygame.transform.scale(initiating_window,(width,height+100))
x_img = pygame.transform.scale(x_img,(80,80))
o_img = pygame.transform.scale(o_img,(80,80))

def game_initiating_window():
    screen.blit(initiating_window,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.fill(white)

    # drawing vertical lines
    pygame.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pygame.draw.line(screen,line_color,(width/3 * 2,0),(width/3 * 2,height),7)

    #drawing horizontal lines
    pygame.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pygame.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)

    draw_status()

def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Game Draw!!!"
    
    font = pygame.font.Font(None,30)
    text = font.render(message,True,white)
    text_rect = text.get_rect(center=(width/2,500-50))
    screen.fill((0,0,0),(0,400,400,100))
    screen.blit(text,text_rect)
    pygame.display.update()

def check_win():
    global board, winner, draw

    # checking for winning rows
    for row in range(0,3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(screen,(250,0,0),(0,(row+1)*height/3 - height/6),(width,(row+1)*height/3 - height/6),5)
            break
    
    # checking for winning columns
    for col in range(0,3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(screen,(250,0,0),((col+1)*width/3 - width/6,0),((col+1)*width/3 - width/6,height),5)
            break
    
    # check for diagonal winners
    # game won diagonal left to right
    if (board[0][0] == board[1][1] == board[2][2] and (board[0][0] is not None)):
        winner = board[0][0]
        pygame.draw.line(screen,(250,70,70),(50,50),(350,350),5)
    # game won diagonal right to left
    if (board[0][2] == board[1][1] == board[2][0] and (board[0][2] is not None)):
        winner = board[0][2]
        pygame.draw.line(screen,(250,70,70),(350,50),(50,350),5)
    
    if (all([all(row) for row in board]) and winner is None):
        draw = True
    draw_status()

def drawXO(row,col):
    global board, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width/3*2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height/3*2 + 30
    
    board[row-1][col-1] = XO
    if XO == 'x':
        screen.blit(x_img,(posy,posx))
        XO = 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO = 'x'
    pygame.display.update()

def user_click():
    x, y = pygame.mouse.get_pos()

    if x < width/3:
        col = 1
    elif x < width/3*2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None
    
    if y < height/3:
        row = 1
    elif y < height/3*2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None
    
    if (row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row,col)
        check_win()

def reset_game():
    global board, winner, draw, XO
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3,[None]*3,[None]*3]

game_initiating_window()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            user_click()
            if (winner or draw):
                reset_game()
    pygame.display.update()
    CLOCK.tick(fps)
    