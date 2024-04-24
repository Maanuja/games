import pygame
import random
from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, RED

class Fruit:
    def __init__(self, snake):
        self.snake = snake
        self.respawn()

    def respawn(self):
        while True:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if self.position not in self.snake.body:
                break

    def draw(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))