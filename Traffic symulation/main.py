import sys

import pygame
from pygame.locals import *
import time
import numpy as np
import Model


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)

LIGHT1_TIME_S = 40
LIGHT2_TIME_S = 28


class Application:
    light1 = True
    light2 = True

    def __init__(self):
        (self.width, self.height) = (1800, 600)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Nagel-Schreckenberg Simulation")
        self.bg_img = pygame.image.load('agh.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (1950, 650))
        self.updateTime = 0.5

        self.running = True
        
        self.running_time = 0

        # przechowuje położenia samochów w czasie t, gdzie wartość > 0 oznacza id samochodu znajdujcy się na danym polu, 0 - brak samochodu
        self.board = np.zeros((200, 3))
        
        self.cars = []
        self.initialize_busline()
        self.draw_model()
        self.run()

    def initialize_busline(self):
        for i in range(21):
            self.board[i][2] = 10001

        for i in range(40, 44):
            self.board[i][2] = 10001

        for i in range(74, 114):
            self.board[i][2] = 10001

        for i in range(160, 165):
            self.board[i][2] = 10001

        for i in range(190, 200):
            self.board[i][2] = 10001

    def draw_model(self):
        Model.draw_grid(self.screen, self.width)
        pygame.display.flip()
        start = time.time()

    def show_board(self):
        stri = '#'
        for j in range(self.board.shape[1]):
            for i in range(self.board.shape[0]):
                stri = stri + str(self.board[i][j])+' '
                if i == 199:
                    print(stri)
                    stri = '#'

    def manage_traffic_light(self):
        if self.running_time % LIGHT1_TIME_S/2 == 0:
            self.light1 = self.change_traffic_light(self.light1, 94)

        if self.running_time % LIGHT2_TIME_S/2 == 0:
            self.light2 = self.change_traffic_light(self.light2, 137)

    def change_traffic_light(self, light, position) -> bool:
        if light:
            light = False
            if position == 94:
                self.board[94][0] = 0
                self.board[94][1] = 0
            elif position == 137:
                self.board[137][0] = 0
                self.board[137][1] = 0
                self.board[137][2] = 0
        else:
            light = True
            if position == 94:
                self.board[94][0] = 10000
                self.board[94][1] = 10000
            elif position == 137:
                self.board[137][0] = 10000
                self.board[137][1] = 10000
                self.board[137][2] = 10000
        return light
    
    def manage_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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


    def run(self):
        while self.running:
            self.screen.blit(self.bg_img,(-100,0))
            self.board, self.cars = Model.process(self.board, self.cars)
            self.board, self.cars = Model.add_random_car(self.board, self.cars, self.screen)

            Model.draw(self.board, self.screen, self.width)
            pygame.display.flip()

            self.manage_traffic_light()
            time.sleep(self.updateTime)
            self.manage_keys()

            self.running_time += 1


app = Application()