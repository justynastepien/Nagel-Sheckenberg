import pygame
from datetime import datetime
import time
import numpy as np
import Car


FREE_LANE = 201
MAX_SPEED = 4

BLOCK_SIZE = 7
BIGG_BLOCK = BLOCK_SIZE + 1

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (80, 80, 80)

height = [204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 203, 203, 202, 202, 201, 201, 200, 200,
        199, 199, 198, 198, 197, 197, 196, 196, 196, 195, 195, 195, 194, 194, 194, 193, 193, 193, 192, 192,
        192, 192, 192, 192, 192, 191, 191, 191, 191, 191, 191, 190, 190, 190, 190, 190, 190, 189, 189, 189,
        189, 189, 189, 188, 188, 188, 188, 188, 190, 192, 194, 196, 198, 201, 204, 206, 209, 211, 213, 216,
        218, 221, 223, 225, 228, 231, 234, 236, 239, 242, 245, 247, 249, 252, 255, 257, 260, 263, 265, 268,
        270, 272, 274, 275, 275, 274, 274, 274, 273, 273, 271, 269, 267, 265, 263, 261, 259, 256, 254, 252,
        249, 247, 244, 242, 239, 236, 233, 230, 227, 224, 221, 219, 217, 216, 214, 213, 211, 210, 211, 212,
        212, 213, 215, 216, 218, 219, 220, 221, 222, 223, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232,
        233, 234, 235, 236, 237, 238, 239, 240, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253,
        255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 274, 275, 276
]

def draw_grid(screen, width):
    pygame.draw.line(screen, white, (0, 300), (width, 300), 1)
    pygame.draw.line(screen, white, (0, 310), (width, 310), 1)
    pygame.draw.line(screen, white, (0, 290), (width, 290), 1)

    for i in range(1, 200):
        pygame.draw.line(screen, white, (i * BIGG_BLOCK, 290), (i * BIGG_BLOCK, 310), 1)


def draw(board, screen):
    for j in range(board.shape[1]):
        for i in range(board.shape[0]):
            if board[i][j] == 0 and j == 1:
                pygame.draw.rect(screen, grey, (i * BIGG_BLOCK + 80, height[i], BLOCK_SIZE, BLOCK_SIZE)) # bottom line
                continue
            elif j == 1:
                pygame.draw.rect(screen, blue, (i * BIGG_BLOCK + 1, 301, BLOCK_SIZE, BLOCK_SIZE)) # cars at bottom
            elif board[i][j] == 0 and j == 0:
                pygame.draw.rect(screen, grey, (i * BIGG_BLOCK + 80, height[i] - BIGG_BLOCK, BLOCK_SIZE, BLOCK_SIZE)) # upper line
            elif j == 0:
                pygame.draw.rect(screen, blue, (i * BIGG_BLOCK + 1, 291, BLOCK_SIZE, BLOCK_SIZE)) # cars at upper


def find_free_id(board):
    i = 1
    while True:
        if i not in board:
            return i
        i += 1


def add_random_car(board, cars, screen):
    p = np.random.rand(2)

    if p[0] > 0.5 and board[0][1] == 0:
        id = find_free_id(board)
        cars.append(Car.Car(1, id))
        board[0][1] = id
        pygame.draw.rect(screen, blue, (0 * BIGG_BLOCK + 1, 301, BLOCK_SIZE, BLOCK_SIZE))

    if p[1] > 0.5 and board[199][0] == 0:
        id = find_free_id(board)
        cars.append(Car.Car(1, id))
        board[199][0] = id
        pygame.draw.rect(screen, blue, (199 * BIGG_BLOCK + 1, 291, BLOCK_SIZE, BLOCK_SIZE))


def find_car(id, cars):
    for c in cars:
        if c.id == id:
            return c


def find_next_car(board, i, j):
    match j:
        case 0:
            for k in range(i):
                if not board[k][j] == 0:
                    next_car = board[k][j]
                    return next_car, k
            return FREE_LANE, FREE_LANE
        case 1:
            for k in range(i + 1, board.shape[0]):
                if not board[k][j] == 0:
                    next_car = board[k][j]
                    return next_car, k
            return FREE_LANE, FREE_LANE

def f_acceleration(velocity):
    if velocity == 1:
        return 2
    else:
        return 1

def process(board, cars):

    new_board = np.zeros((200, 2))
    cars_to_rmv = []
    for j in range(board.shape[1]):
        for i in range(board.shape[0]):

            if board[i][j] == 0:
                continue

            car_id = board[i][j]
            car = find_car(car_id, cars)

            vel = car.v

            next_car, k = find_next_car(board, i, j)

            if next_car == FREE_LANE:
                new_vel = vel + f_acceleration(vel)

            if not next_car == FREE_LANE:
                distance = abs(k - i) - 1
                if distance > vel:
                    new_vel = vel + f_acceleration(vel)
                elif distance < vel:
                    new_vel = distance - 1  #funkcja hamowania
                    if distance == 1:
                        new_vel = 1
                    elif distance == 0:
                        new_vel = 0
                else:
                    new_vel = vel

            new_vel = min(new_vel, MAX_SPEED)
            car.change_velocity(new_vel)
            if i + new_vel < 200 and j == 1:
                new_board[i + new_vel][j] = car.id

            elif i-new_vel >= 0 and j == 0:
                new_board[i - new_vel][j] = car.id
            else:
                cars_to_rmv.append(car)
    for c in cars_to_rmv:
        cars.remove(c)

    return new_board, cars