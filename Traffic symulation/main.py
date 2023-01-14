import sys

import pygame
from pygame.locals import *
from datetime import datetime
import time
import numpy as np
import Car
import Model
import Bus

light1 = False
light2 = False

def show(board):
    stri = '#'
    for j in range(board.shape[1]):
        for i in range(board.shape[0]):
            stri = stri + str(board[i][j])+' '
            if i == 199:
                print(stri)
                stri = '#'

def change_traffic_light(light, board, possition):
    if light:
        light = False
        if possition == 81:
            board[81][0] = 0
            board[81][1] = 0
        elif possition == 134:
            board[134][0] = 0
            board[134][1] = 0
            board[134][2] = 0
    else:
        light = True
        if possition == 81:
            board[81][0] = 1000
            board[81][1] = 1000
        elif possition == 134:
            board[134][0] = 1000
            board[134][1] = 1000
            board[134][2] = 1000
    return light, board


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)

(width, height) = (1800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nagel-Schreckenberg Simulation")
bg_img = pygame.image.load('agh.png')
bg_img = pygame.transform.scale(bg_img,(1950,650))
updateTime = 0.5

running = True
prevTime1 = time.perf_counter()
prevTime2 = time.perf_counter()
prevTime3 = time.perf_counter()

#przechowuje położenia samochów w czasie t, gdzie wartość > 0 oznacza id samochodu znajdujcy się na danym polu, 0 - brak samochodu
board = np.zeros((200, 3))

for i in range(21):
    board[i][2] = 1001

for i in range(40, 44):
    board[i][2] = 1001

for i in range(74, 114):
    board[i][2] = 1001

for i in range(160, 165):
    board[i][2] = 1001

for i in range(190, 200):
    board[i][2] = 1001

cars = []

Model.draw_grid(screen, width)

pygame.display.flip()
start = time.time()

while running:
    screen.blit(bg_img,(-100,0))
    board, cars = Model.process(board, cars)
    board, cars = Model.add_random_car(board, cars, screen)
    if light1 and board[81][0] == 0:
        board[81][0] = 1000
    elif light1 and board[81][1] == 0:
        board[81][1] = 1000
    if light2 and board[134][0] == 0:
        board[134][0] = 1000
    elif light2 and board[134][1] == 0:
        board[134][1] = 1000
    elif light2 and board[134][2] == 0:
        board[134][2] = 1000

    Model.draw(board, screen, width)
    pygame.display.flip()

    checkTime1 = time.perf_counter()
    if checkTime1 - prevTime1 > 10:
        light1, board = change_traffic_light(light1, board, 81)
        prevTime1 = time.perf_counter()

    checkTime2 = time.perf_counter()
    if checkTime2 - prevTime2 > 7:
        light2, board = change_traffic_light(light2, board, 134)
        prevTime2 = time.perf_counter()

    time.sleep(updateTime)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            pygame.event.clear()
            while True:
                event = pygame.event.wait()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        break
                    if event.key == K_RIGHT:
                        newevent = pygame.event.Event(pygame.locals.KEYDOWN, unicode="", key=K_SPACE,
                                                      mod=pygame.locals.KMOD_NONE)
                        pygame.event.post(newevent)
                        break
