import random
import curses

def devine_le_nombre(stdscr):
    # Initialisation
    curses.curs_set(1)  # Afficher le curseur
    stdscr.clear()
    stdscr.refresh()

    # Configurations
    hauteur, largeur = stdscr.getmaxyx()

    # Calcul de la position de l'encadrement
    cadre_hauteur = 10
    cadre_largeur = 60
    cadre_x = (largeur - cadre_largeur) // 2
    cadre_y = (hauteur - cadre_hauteur) // 2

    # Affichage de l'encadrement
    for i in range(cadre_hauteur):
        stdscr.addstr(cadre_y + i, cadre_x, "|" + " " * (cadre_largeur - 2) + "|")
    stdscr.addstr(cadre_y, cadre_x, "+" + "-" * (cadre_largeur - 2) + "+")
    stdscr.addstr(cadre_y + cadre_hauteur - 1, cadre_x, "+" + "-" * (cadre_largeur - 2) + "+")

    # Affichage du message principal
    message = "Devinez le nombre entre 1 et 100 (Q pour quitter) :"
    stdscr.addstr(cadre_y + 2, cadre_x + (cadre_largeur - len(message)) // 2, message)

    nombre_a_deviner = random.randint(1, 100)
    essais = 0

    while True:
        stdscr.refresh()
        saisie = ""
        curses.echo()  # Activer l'écho de la saisie
        saisie = stdscr.getstr(cadre_y + 3, cadre_x + (cadre_largeur - 20) // 2, 20).decode()
        curses.noecho()  # Désactiver l'écho de la saisie

        if saisie.lower() == 'q':
            message = "Vous avez quitté le jeu."
            stdscr.addstr(cadre_y + 5, cadre_x + (cadre_largeur - len(message)) // 2, message)
            stdscr.refresh()
            stdscr.getch()  # Attente d'une touche pour quitter
            break

        try:
            essai = int(saisie)
        except ValueError:
            message = "Veuillez entrer un nombre valide."
            stdscr.addstr(cadre_y + 5, cadre_x + (cadre_largeur - len(message)) // 2, " " * (cadre_largeur - 4))
            stdscr.addstr(cadre_y + 5, cadre_x + (cadre_largeur - len(message)) // 2, message)
            continue

        essais += 1

        if essai < nombre_a_deviner:
            message = "Trop bas ! Essayez encore :"
        elif essai > nombre_a_deviner:
            message = "Trop haut ! Essayez encore :"
        else:
            message = f"Bravo ! Vous avez deviné le nombre en {essais} essais."
            stdscr.addstr(cadre_y + 5, cadre_x + (cadre_largeur - len(message)) // 2, message)
            stdscr.refresh()
            stdscr.getch()  # Attente d'une touche pour quitter
            break

        stdscr.addstr(cadre_y + 5, cadre_x + (cadre_largeur - len(message)) // 2, " " * (cadre_largeur - 4))
        stdscr.addstr(cadre_y + 5, cadre_x + (cadre_largeur - len(message)) // 2, message)

if __name__ == "__main__":
    curses.wrapper(devine_le_nombre)
