
import pygame
from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, RIGHT, GREEN

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        x, y = self.direction
        new_head = (head[0] + x, head[1] + y)
        # Verifier que la position de la tête du serpent ne cogne pas une bordure de l'écran
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            return True  # Game over

        # Verifier que la position de la tête ne cogne pas son propre corps
        if new_head in self.body[1:]:
            return True  # Game over

        self.body.insert(0, new_head)

        #enleve la derniere position pour garder la bonne longeur du corps
        self.body.pop() 
        return False

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, surface):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(surface, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))