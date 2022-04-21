import pygame
import numpy as np
pygame.init()

class swipe:
    def __init__(self):
        self.array = [[0 for i in range(6)] for j in range(9)]



game = swipe()
if __name__ == "__main__":
    print(game.array)