import pygame
import numpy as np
from Car import Car
from Bus import Bus
from ModelStatistics import stats


START = 80
BLOCK_SIZE = 7
BLOCK_W_SPACE = BLOCK_SIZE+1
FREE_LANE = 201
MAX_SPEED = 4
INCREASED_SPEED = 0

BUSPAS = 1

free = 0

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (120, 120, 120)
orange = (30, 230, 55)

light_color = red
car_color = blue
bus_color = orange
empty_color = grey

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
    for i in range(1, 200):
        # vertical
        pygame.draw.line(screen, white, (i * BLOCK_W_SPACE + START, height[i]-BLOCK_W_SPACE), (i * BLOCK_W_SPACE + START, height[i]+20), 1)

        # horizontal
        k = width/200
        # add  + START
        # pygame.draw.line(screen, white, (k*i, height[i-1]), (k*(i+1), height[i]), 1)
        # pygame.draw.line(screen, white, (k*i, height[i-1]+BLOCK_W_SPACE), (k*(i+1), height[i]+BLOCK_W_SPACE), 1)
        # pygame.draw.line(screen, white, (k*i, height[i-1]-BLOCK_W_SPACE), (k*(i+1), height[i]-BLOCK_W_SPACE), 1)
        # pygame.draw.line(screen, white, (k*i, height[i-1]+20), (k*(i+1), height[i]+20), 1)


def draw(board, screen, width):
    draw_grid(screen, width)
    to_skip = -1
    for j in range(board.shape[1]):
        for i in range(board.shape[0]):
            if board[i][j] == to_skip:
                continue

            if board[i][j] == 10001:
                pygame.draw.rect(screen, white, (i * BLOCK_W_SPACE + START, height[i]+BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
                continue
            if board[i][j] == 10002:
                pygame.draw.rect(screen, white, (i * BLOCK_W_SPACE + START, height[i]+20, BLOCK_SIZE, BLOCK_SIZE))
                continue


            if board[i][j] == 10000:
                if j == 1 and i == 94:
                    pygame.draw.rect(screen, light_color, (94 * BLOCK_W_SPACE + START, height[i], BLOCK_SIZE, BLOCK_SIZE))
                elif j == 0 and i == 94:
                    pygame.draw.rect(screen, light_color, (94 * BLOCK_W_SPACE + START, height[i]-BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
                elif j == 1 and i == 137:
                    pygame.draw.rect(screen, light_color, (137 * BLOCK_W_SPACE + START, height[i], BLOCK_SIZE, BLOCK_SIZE))
                elif j == 0 and i == 137:
                    pygame.draw.rect(screen, light_color, (137 * BLOCK_W_SPACE + START, height[i]-BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
                elif j == 2 and i == 137:
                    pygame.draw.rect(screen, light_color, (137 * BLOCK_W_SPACE + START, height[i]+BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
                elif j == 1 and i == 198:
                    pygame.draw.rect(screen, light_color, (137 * BLOCK_W_SPACE + START, height[i], BLOCK_SIZE, BLOCK_SIZE))
                elif j == 2 and i == 198:
                    pygame.draw.rect(screen, light_color, (137 * BLOCK_W_SPACE + START, height[i]+BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
                continue

            if board[i][j] == 0 and j == 1:
                pygame.draw.rect(screen, empty_color, (i * BLOCK_W_SPACE + START, height[i], BLOCK_SIZE, BLOCK_SIZE))
                continue
            elif j == 1:
                if i + 1 < 200 and board[i][j] == board[i + 1][j]:
                    pygame.draw.rect(screen, bus_color, (i * BLOCK_W_SPACE + START, height[i], BLOCK_SIZE*2, BLOCK_SIZE))
                    to_skip = board[i][j]
                    continue
                pygame.draw.rect(screen, car_color, (i * BLOCK_W_SPACE + START, height[i], BLOCK_SIZE, BLOCK_SIZE))
            elif board[i][j] == 0 and j == 0:
                pygame.draw.rect(screen, empty_color, (i * BLOCK_W_SPACE + START, height[i]-BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
            elif j == 0:
                if i + 1 < 200 and board[i][j] == board[i + 1][j]:
                    pygame.draw.rect(screen, bus_color, (i * BLOCK_W_SPACE + START, height[i]-BLOCK_W_SPACE, BLOCK_SIZE*2, BLOCK_SIZE))
                    to_skip = board[i][j]
                    continue
                pygame.draw.rect(screen, car_color, (i * BLOCK_W_SPACE + START, height[i]-BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
            elif board[i][j] == 0 and j == 2:
                pygame.draw.rect(screen, empty_color, (i * BLOCK_W_SPACE + START, height[i]+BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
                continue
            elif j == 2:
                if i + 1 < 200 and board[i][j] == board[i + 1][j]:
                    pygame.draw.rect(screen, bus_color, (i * BLOCK_W_SPACE + START, height[i]+BLOCK_W_SPACE, BLOCK_SIZE*2, BLOCK_SIZE))
                    to_skip = board[i][j]
                    continue
                pygame.draw.rect(screen, car_color, (i * BLOCK_W_SPACE + START, height[i]+BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))


def find_free_id(board):
    global free
    free += 1
    if free == 10000 or free == 10001 or free == 10002 or free == FREE_LANE:
        free += 1
    return free


def add_random_car(board, cars, screen):
    p = np.random.rand(4)
    flag1 = 0
    flag2 = 0
    if p[0] > 0.2 and board[0][1] == 0:
        if board[1][1] == 0 and p[2] < 0.2:
            bus_id = find_free_id(board)
            cars.append(Bus(1, bus_id, 'bus'))
            board[0][1] = bus_id
            board[1][1] = bus_id
            #print('bus')
            pygame.draw.rect(screen, bus_color, (0 * BLOCK_W_SPACE + START, height[0], BLOCK_SIZE*2, BLOCK_SIZE))
            flag1 = 1
        if flag1 == 0:
            car_id = find_free_id(board)
            cars.append(Car(1, car_id, 'car'))
            board[0][1] = car_id
            #print('car')
            pygame.draw.rect(screen, car_color, (0 * BLOCK_W_SPACE + START, height[0], BLOCK_SIZE, BLOCK_SIZE))

    if p[1] > 0.2 and board[199][0] == 0:
        if board[198][0] == 0 and p[3] < 0.2:
            bus_id = find_free_id(board)
            cars.append(Bus(1, bus_id, 'bus'))
            board[199][0] = bus_id
            board[198][0] = bus_id
            pygame.draw.rect(screen, red, (198 * BLOCK_W_SPACE + START, height[198]-BLOCK_W_SPACE, BLOCK_SIZE*2, BLOCK_SIZE))
            flag2 = 1
        if flag2 == 0:
            car_id = find_free_id(board)
            cars.append(Car(1, car_id, 'car'))
            board[199][0] = car_id
            pygame.draw.rect(screen, car_color, (199 * BLOCK_W_SPACE + START, height[199]-BLOCK_W_SPACE, BLOCK_SIZE, BLOCK_SIZE))
    return board, cars

def find_car(id, cars):
    for c in cars:
        if c.id == id:
            return c

def change_line(behind_car, p, i, j):
    r = np.random.rand(2)
    car = find_car(behind_car)
    if i-p > car.v:
        if r[0] < 0.9:
            return True
    elif i-p <= car.v:
        if r[1] < 0.2:
            return True
    else:
        return False


def find_next_car(board, i, j):
    match j:
        case 0:
            for k in range(i, -1, -1):
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
        case 2:
            for k in range(i + 1, board.shape[0]):
                if not board[k][j] == 0:
                    next_car = board[k][j]
                    return next_car, k
            return FREE_LANE, FREE_LANE


def find_car_before(board, i, j, v_type):
    p = j + 1
    if board[i][j + 1] == 10001:
        return -1, -1
    if v_type == 'car':
        for k in range(i, -1, -1):
            if board[k][p] == 10001:
                return FREE_LANE, FREE_LANE
            if not board[k][j] == 0:
                next_car = board[k][j]
                return next_car, k
    elif v_type == 'bus':
        for k in range(i+1, -1, -1):
            if board[k][p] == 10001:
                return FREE_LANE, FREE_LANE
            if not board[k][j] == 0:
                next_car = board[k][j]
                return next_car, k


def f_acceleration(velocity):
    if velocity == 1:
        return 2
    else:
        return 1


def process(board, cars):

    new_board = np.zeros((200, 3))
    cars_to_rmv = []
    to_skip = -1
    stop = False

    for j in range(board.shape[1]):
        for i in range(board.shape[0]):
            if board[i][j] == 10000:
                new_board[i][j] = 10000
                continue
            if board[i][j] == 10001:
                new_board[i][j] = 10001
                continue
            if board[i][j] == 10002:
                new_board[i][j] = 10002
                continue
            if board[i][j] == 0:
                continue
            if board[i][j] == to_skip:
                continue
            t = j
            car_id = board[i][j]
            car = find_car(car_id, cars)

            vel = car.v

            if not BUSPAS:
                r = np.random.rand(1)
                if j == 1 and car.vehicle_type == 'car' and r[0] <= 0.2:
                    if board[i][j+1] == 0 and board[i+1][j+1] == 0 and board[i+2][j+1] != 1001:
                        t = 2

            car.time += 1

            # if j == 1 and car.vehicle_type == 'car':
            #     behind_car, p = find_car_before(board, i, j, car.vehicle_type)
            #     # print(behind_car)
            #     if not behind_car == -1:
            #         if not i - p == -1:
            #             if board[i][j+1] == 0 and change_line(behind_car, p, i, j):
            #                 t = 2

            if j == 1 and car.vehicle_type == 'bus':
                if board[i][j+1] == 0 and board[i+1][j+1] == 0 and board[i+2][j+1] != 10001:
                    t = 2

            if j == 2:
                # print([car_id, board[i][j - 1] == 0, board[i + 1][j - 1] == 0, board[i+1][j] == 10001])
                if car.vehicle_type == 'bus' and board[i][j - 1] == 0 and board[i + 1][j - 1] == 0 and board[i+2][j] == 10001 and i < 198:
                    t = 1
                elif car.vehicle_type == 'car' and board[i][j-1] == 0 and board[i+1][j] == 10001:
                    t = 1

            next_car, k = 0, 0
            if car.vehicle_type == 'bus':
                if t == 1 or t == 2:
                    next_car, k = find_next_car(board, i + 1, t)
                elif t == 0:
                    next_car, k = find_next_car(board, i - 1, t)
                to_skip = car_id
            elif car.vehicle_type == 'car':
                if t == 1 or t == 2:
                    next_car, k = find_next_car(board, i, t)
                else:
                    next_car, k = find_next_car(board, i - 1, t)

            if next_car == FREE_LANE:
                new_vel = vel + f_acceleration(vel)

            if not next_car == FREE_LANE:
                if car.vehicle_type == 'bus':
                    distance = abs(k - (i+1)) - 1
                    if j == 0:
                        distance = abs(k - i) - 1
                else:
                    distance = abs(k - i) - 1

                if distance < 0:
                    distance = 0
                if distance > vel + INCREASED_SPEED:
                    new_vel = vel + 1 + INCREASED_SPEED
                elif distance > vel:
                    new_vel = vel + 1
                elif distance < vel:
                    new_vel = distance - 1 - INCREASED_SPEED  #funkcja hamowania
                    if distance == 1:
                        new_vel = 1
                        if car.vehicle_type == 'bus':
                            new_vel = 0
                    elif distance == 0:
                        new_vel = 0
                else:
                    new_vel = vel
            if j == 1 and i < 197:
                if car.vehicle_type == 'car' and board[i+3][j+1] == 10001 and board[i+1][j+1] != 0 and board[i+2][j+1] != 10001 and board[i+2][j+1] != 0 and board[i+1][j+1] != 10001:
                    new_vel = 0

            if car.vehicle_type == 'bus' and new_vel > 0 and (i<23 and i > 14):
                new_vel = 1
            if car.vehicle_type == 'bus' and j == 2 and new_vel > 0 and (i<137 and i > 137):
                new_vel = 1
            if t == 2 and t != j and (i < 23 or i == 136 or i == 283):
                new_vel = 0

            new_vel = min(new_vel, MAX_SPEED)
            car.change_velocity(new_vel)

            if car.vehicle_type == 'car':
                if i + new_vel < 200 and (t == 1 or t == 2):
                    new_board[i + new_vel][t] = car.id

                elif i-new_vel >= 0 and j == 0:
                    new_board[i - new_vel][j] = car.id
                else:
                    cars_to_rmv.append(car)
            elif car.vehicle_type == 'bus':
                if i + new_vel + 1 < 200 and (t == 1 or t == 2):
                    new_board[i + new_vel][t] = car.id
                    if i + new_vel + 1 < 200:
                        new_board[i + 1 + new_vel][t] = car.id

                elif i - new_vel >= 0 and j == 0:

                    new_board[i - new_vel][j] = car.id
                    if i - new_vel + 1 < 200:
                        new_board[i + 1 - new_vel][j] = car.id
                else:
                    cars_to_rmv.append(car)
            stop = False
    for c in cars_to_rmv:
        cars.remove(c)
        if stats.can_add():
            if isinstance(c, Car):
                stats.add_car(c.time)
            elif isinstance(c, Bus):
                stats.add_bus(c.time)
        
    print("\ncar avg pass time:", stats.get_avg_car(), "(", stats.total_cars, ")")
    print("bus avg pass time:", stats.get_avg_bus(), "(", stats.total_buses, ")")

    return new_board, cars