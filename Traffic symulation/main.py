import pygame
from datetime import datetime
import time
import numpy as np
import Car
import Model

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

(width, height) = (1900, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nagel Schreckenberg Symulation")
updateTime = 0.05

running = True
prevTime = datetime.now()

board = np.zeros((200, 2)) #przechowuje położenia samochów w czasie t, gdzie wartość > 0 oznacza id samochodu znajdujcy się na danym polu, 0 - brak samochodu
cars = []

Model.draw_grid(screen, width)

cars.append(Car.Car(4, 1))
cars.append(Car.Car(1, 2))

board[10][1] = 1
board[13][1] = 2
pygame.draw.rect(screen, red, (10*10 + 1, 501, 9, 9))
pygame.draw.rect(screen, red, (13*10 + 1, 501, 9, 9))
pygame.display.flip()
time.sleep(2)

while running:
    board = Model.process(board, cars)
    Model.add_random_car(board, cars, screen)
    Model.draw(board, screen)
    pygame.display.flip()

    time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

