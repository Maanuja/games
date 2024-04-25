import pygame
import random
from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, RED

apple_image = pygame.image.load("apple.png")  # Replace "apple.png" with the path to your apple image file

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
        center = (x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2)
        radius = GRID_SIZE // 2
        pygame.draw.circle(surface, RED, center, radius)        
        # surface.blit(apple_image, (x * GRID_SIZE, y * GRID_SIZE))