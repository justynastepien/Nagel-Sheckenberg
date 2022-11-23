import pygame
from datetime import datetime
import time
import numpy as np
import Car


FREE_LANE = 201

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


def draw_grid(screen, width):
    pygame.draw.line(screen, white, (0, 500), (width, 500), 1)
    pygame.draw.line(screen, white, (0, 510), (width, 510), 1)
    pygame.draw.line(screen, white, (0, 490), (width, 490), 1)

    for i in range(1, 200):
        pygame.draw.line(screen, white, (i * 10, 490), (i * 10, 510), 1)


def draw(board, screen):
    for j in range(board.shape[1]):
        for i in range(board.shape[0]):
            if board[i][j] == 0:
                pygame.draw.rect(screen, black, (i * 10 + 1, 501, 9, 9))
                continue
            pygame.draw.rect(screen, red, (i * 10 + 1, 501, 9, 9))


def find_free_id(board):
    i = 1
    while True:
        if i not in board:
            return i
        i += 1


def add_random_car(board, cars, screen):
    p = np.random.rand(1)

    if p > 0.5 and board[0][1] == 0:
        id = find_free_id(board)
        cars.append(Car.Car(1, id))
        board[0][1] = 1
        pygame.draw.rect(screen, red, (0 * 10 + 1, 501, 9, 9))


def find_car(id, cars):
    for c in cars:
        if c.id == id:
            return c


def find_next_car(board, i, j):
    for k in range(i + 1, board.shape[0]):
        if not board[k][j] == 0:
            next_car = board[k][j]
            return next_car, k
    return FREE_LANE, FREE_LANE


def process(board, cars):

    new_board = np.zeros((200, 2))

    for j in range(board.shape[1]):
        for i in range(board.shape[0]):

            if board[i][j] == 0:
                continue

            car_id = board[i][j]
            car = find_car(car_id, cars)

            vel = car.v

            next_car, k = find_next_car(board, i, j)

            if next_car == FREE_LANE:
                new_vel = vel + 1 #tu ma być funkcja przyrostu

            if not next_car == FREE_LANE:
                distance = k - i - 1
                if distance > vel:
                    new_vel = vel + 1 #tu ma być funkcja przyrostu
                elif distance < vel:
                    new_vel = distance - 1  # tu ma być funkcja hamowania
                    if distance == 1:
                        new_vel = 1
                    elif distance == 0:
                        new_vel = 0
                else:
                    new_vel = vel

            car.change_velocity(new_vel)
            if i + new_vel < 200:
                new_board[i + new_vel][j] = car.id
    return new_board