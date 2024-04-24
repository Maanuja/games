import requests

def choisir_mot():
    url = "https://random-word-api.herokuapp.com/word?lang=fr"
    response = requests.get(url)
    data = response.json()
    return data[0]

def afficher_mot_cache(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "🔵 "
    return mot_affiche.strip()

def afficher_bonhomme(vies_restantes):
    dessin = [
        "  _______",
        " |/      |",
        " |       ",
        " |       ",
        " |       ",
        " |       ",
        " |",
        "_|___"
    ]
    parties_corps = 8 - vies_restantes
    if parties_corps >= 1:
        dessin[2] = " |       |"
    if parties_corps >= 2:
        dessin[3] = " |      (_)"
    if parties_corps >= 3:
        dessin[4] = " |      \\"
    if parties_corps >= 4:
        dessin[4] += "|"
    if parties_corps >= 5:
        dessin[4] += "/"
    if parties_corps >= 6:
        dessin[5] = " |       |"
    if parties_corps >= 7:
        dessin[6] = " |      /"
    if parties_corps >= 8:
        dessin[6] += " \\"
    for line in dessin:
        print(line)

def pendu():
    mot = choisir_mot()
    lettres_trouvees = set()
    lettres_ratees = set()
    vies = 8

    print("╔══════════════════════════════════════╗")
    print("║ Bienvenue dans le jeu du Pendu !     ║")
    print("║ Le mot à deviner a", len(mot) if len(mot) > 9 else str(len(mot)) + " ", "lettres.       ║")
    print("╚══════════════════════════════════════╝\n")

    while vies > 0:
        print("Mot :", afficher_mot_cache(mot, lettres_trouvees))
        print("Lettres déjà citées :", ", ".join(lettres_ratees))
        afficher_bonhomme(vies)
        lettre = input("\nDevinez une lettre (ou tapez 'quit' pour quitter) : ").lower()
        print("══" * 30 + "\n")
        if lettre == 'quit':
            print("Merci d'avoir joué ! Au revoir !")
            return
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une lettre.")
            continue
        elif lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre !")
        elif lettre in mot:
            print("Bonne devinette ! La lettre", lettre, "est dans le mot.")
            lettres_trouvees.add(lettre)        
        elif lettre in lettres_ratees:
            print("Vous avez déjà essayé cette lettre, essayez une autre.")
        else:
            print("Désolé, la lettre", lettre, "n'est pas dans le mot.")
            lettres_ratees.add(lettre)
            vies -= 1
            print("Il vous reste", vies, "vies.\n")

        if len(lettres_trouvees) == len(set(mot)):
            print("\nFélicitations ! Vous avez deviné le mot:", mot)
            break

    if vies == 0:
        print("\nDésolé, vous avez perdu. Le mot était:", mot)
        afficher_bonhomme(0)

if __name__ == "__main__":
    pendu()
