import pygame
from snake import Snake
from fruit import Fruit
# Paramètres de la fenêtre
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, RIGHT, LEFT, UP, DOWN

# Initialisation de Pygame
pygame.init()

apple_image = pygame.image.load("apple.png") 

# Fonction de fin de jeu
def game_over(screen, points, time_elapsed):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    # Afficher les points et le temps écoulée
    points_text = font.render("Points: {}".format(points), True, WHITE)
    time_text = font.render("Time: {:.2f} seconds".format(time_elapsed), True, WHITE)
    screen.blit(points_text, (SCREEN_WIDTH // 2 - points_text.get_width() // 2, SCREEN_HEIGHT // 2 + 25))
    screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    pygame.display.flip()

# Fonction pour attendre que l'utilisateur appuie sur une touche pour quitter le jeu
def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            
# Fonction principale
def main():
    # Création de la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake')

    # Création du snake et du fruit
    snake = Snake()
    fruit = Fruit(snake)

    # Boucle de jeu
    running = True
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    while running:
        # recupération du mouvement de l'utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        # Vérification de la collision avec le fruit
        if snake.body[0] == fruit.position:
            fruit.respawn()
            snake.grow()

        
        # Game Over
        if snake.move():
            end_time = pygame.time.get_ticks()
            time_elapsed = (end_time - start_time) / 1000  #temps en seconde
            game_over(screen, len(snake.body) - 1, time_elapsed)
            break

        # Affichage
        screen.fill(BLACK)
        snake.draw(screen)
        fruit.draw(screen)
        fruit.draw(screen)

        pygame.display.flip()

        # Rafraîchissement de l'écran
        clock.tick(10)

    wait_for_key()

    # Fermeture de Pygame
    pygame.quit()

# Lancement du jeu
if __name__ == '__main__':
    main()
