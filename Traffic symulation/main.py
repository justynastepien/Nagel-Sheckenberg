import pygame
from datetime import datetime
import time
import numpy as np
import Car
import Model

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

(width, height) = (1800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nagel-Schreckenberg Symulation")
bg_img = pygame.image.load('agh.png')
bg_img = pygame.transform.scale(bg_img,(1950,650))
updateTime = 0.05

running = True
prevTime = datetime.now()

board = np.zeros((200, 2)) #przechowuje położenia samochów w czasie t, gdzie wartość > 0 oznacza id samochodu znajdujcy się na danym polu, 0 - brak samochodu
cars = []

Model.draw_grid(screen, width)

while running:

    screen.blit(bg_img,(-100,0))
    board, cars = Model.process(board, cars)
    Model.add_random_car(board, cars, screen)
    Model.draw(board, screen)
    pygame.display.flip()

    time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

