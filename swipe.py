import pygame
import numpy as np
import random
from pygame import gfxdraw
# 기본적인 상수 정의
WIDTH = 600  # 게임판의 가로크기
HEIGHT = 800  # 게임판의 세로크기
FPS = 60  # 게임의 프레임
MIN_DEG = 10  # 최소 반사각도
MAX_DEG = 170  # 최대 반사각도
BRICK_WIDTH = 100
BRICK_HEIGHT = 66
GREEN_COLOR = (62, 211, 92)
BRICK_COLOR = (255, 65, 81)
BALL_COLOR = (93, 167, 238)
WHITE_COLOR = (255, 255, 255)

# 스프라이트 목록
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
bricks = pygame.sprite.Group()

class swipe_board:
    def __init__(self):
        self.array = [[0 for i in range(6)] for j in range(9)]  # 없으면 0, 초록공 있으면 -1, 벽돌 있으면 벽돌에 숫자로 나타내는걸로
        self.level = 0  # 블럭의 체력과 레벨 등에 관여하는 레벨, 시작은 0
        self.axis = 300  # 공이 바닥에 있을때 위치, 기본은 정중앙에서 시작

    def show_board_status(self):
        for i in range(9):
            for j in range(6):
                print("%2d" % self.array[i][j], end=" ")
            print()
        print("level : " + str(self.level) + " , brick_axis : " + str(self.axis))

def next_level(board):  # 공이 돌아온 후 레벨 갱신
    board.level += 1
    return board


def new_line(board):  # 한줄에 최소 블럭 한개, 초록공 한개 조건 걸고 섞은 후 나머지 0 4개 대상으로 넣냐 안넣냐 랜덤하게 결정
    temp_line = [board.level, -1, 0, 0, 0, 0]  # 가장 기본조건
    random.shuffle(temp_line)  # 기본조건 셔플
    # print(temp_line)
    for i in range(len(temp_line)):  # 기본조건에서 빈공간을 채울지 안채울지 랜덤하게 결정
        if temp_line[i] == 0:
            temp_line[i] = random.randint(0, 1) * board.level
    # print(temp_line)
    for i in range(len(temp_line)):  # 맨 윗줄을 대입
        board.array[0][i] = temp_line[i]
    return board


def next_line(board):  # 맨 윗줄에 블럭이 생성된 후 보드에 있는 블럭들을 하나씩 내리는 역할
    for i in range(7, -1, -1):  # 맨 아랫줄 바로 위부터 한칸씩 아래로 내리면서 작업
        for j in range(6):
            board.array[i + 1][j] = board.array[i][j]
    for i in range(6):  # 가장 첫번째 줄 0으로 초기화
        board.array[0][i] = 0
    return board


def next_board(board):  # 공이 도착한 후 보드의 벽돌 등을 갱신하는 함수
    next_level(board)
    new_line(board)
    next_line(board)
    board.show_board_status()



def draw_board_brick(board): # 보드의 블럭만 그리는 부분
    for i in range(9):
        for j in range(6):
            board.show_board_status()
            print(i, j)
            l, r, t, b = -BRICK_WIDTH / 2, BRICK_WIDTH / 2, BRICK_HEIGHT / 2, -BRICK_HEIGHT / 2
            brick_cords = [(l, b), (l, t), (r, t), (r, b)]
            brick_cords = [(c[0] + j * BRICK_WIDTH + BRICK_WIDTH / 2 , c[1] + i * BRICK_HEIGHT + BRICK_HEIGHT / 2) for c in brick_cords]
            surf = pygame.Surface((WIDTH, HEIGHT))
            gfxdraw.aapolygon(surf, brick_cords, BRICK_COLOR)
            gfxdraw.filled_polygon(surf, brick_cords, BRICK_COLOR)
            # print(board, i, j)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.set_colorkey(WHITE_COLOR)
pygame.display.set_caption("Swipe Brick Breaker")
clock = pygame.time.Clock()
board = swipe_board()
if __name__ == "__main__":
    # running = True
    # while running:
    #     clock.tick(FPS)
    #     screen.fill((0, 0, 0, 0))
    #     screen.set_alpha(0)
    #     all_sprites.draw(screen)
    #     pygame.display.flip()
    print(board.level)
    next_board(board)
    draw_board_brick(board)
    print(board.level)
    next_board(board)
    draw_board_brick(board)
    print(board.level)
    next_board(board)
    draw_board_brick(board)
    print(board.level)
    next_board(board)
    draw_board_brick(board)
    print(board.level)
    while True:
        draw_board_brick(board)
