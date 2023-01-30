"""
Polashi Dey
Tp 3
406
Description:C,est un jeu de combat des jeu,c'est a dire que le

"""

import random

niveau_de_vies = 20
numero_adversaire = 0
numero_jeu = 0
nombre_victoires = 0
nombre_des_defaites = 0
nombre_victoires_consecutives = 0


boucle_jeu = True

while boucle_jeu: 

    if niveau_de_vies <= 0:
        print("vous avez perdu le jeu!")
        print("recomensez un nouveau jeu!")

        niveau_de_vies = 20
        numero_adversaire = 0
        numero_jeu = 0
        nombre_victoires = 0
        nombre_des_defaites = 0
        nombre_victoires_consecutives = 0

    print(f"votre niveau de vie = {niveau_de_vies}")

    print("\nVoici les options"
          "\n1.Combattre l'adversaire"
          "\n2.Contourner cet adversaire et aller ouvrir une autre porte"
          "\n3.Afficher les règles du jeu"
          "\n4.Quitter la partie")

    choix = int(input("choisir un de numéros d'options"))

    if choix == 1:

        de_du_joueur = random.randint(1, 6) + random.randint(1, 6)

        numero_adversaire += 1
        numero_jeu += 1

        print(f"votre force = {de_du_joueur}")
        print(f"\n nombre d'adversaire = {numero_adversaire}")

        if nombre_victoires_consecutives >= 3:  # boss fight

            print("combat vs le boss!")
            force_boss = random.randint(4, 5) + random.randint(4, 5)
            print(f"Voici la force de votre adversaire:{force_boss}")
            print(f"votre force = {de_du_joueur}")

            if de_du_joueur <= force_boss:
                print("vous avez perdu contre le monstre")
                niveau_de_vies -= force_boss
                nombre_des_defaites += 1
                nombre_victoires_consecutives = 0

            elif de_du_joueur > force_boss:
                print("Vous avez battue le monstre")
                niveau_de_vies += force_boss
                nombre_victoires += 1
                nombre_victoires_consecutives += 1

        else:  # normal fight

            force_adversaire = random.randint(1, 5) + random.randint(1, 5)
            print(force_adversaire)
            print(f"Voici la force de votre adversaire:{force_adversaire}")

            if de_du_joueur <= force_adversaire:  # lose
                print("vous avez perdu contre le monstre")
                niveau_de_vies -= force_adversaire
                nombre_des_defaites += 1
                nombre_victoires_consecutives = 0
            elif de_du_joueur > force_adversaire:  # win
                print("Vous avez battue le monstre")
                niveau_de_vies += force_adversaire
                nombre_victoires += 1
                nombre_victoires_consecutives += 1

        print("Voici votre profile du jeu:"
              f"\n niveau de vies:{niveau_de_vies}"
              f"\n nombre des défaites:{nombre_des_defaites} "
              f"\n nombre de victoires :{nombre_victoires}"
              f"\n nombre de victores consecutives :{nombre_victoires_consecutives}")

    elif choix == 2:
        niveau_de_vies -= 1
        print("Vous avez perdu un vie comme la pénalité")

    elif choix == 3:
        print("voici les règles du jeu:\n"
              "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
              "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de"
              " l’adversaire.  \nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
              "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement,"
              " il y a une pénalité de 1 point de vie.")

    elif choix == 4:
        print("merci et au revoir")
        boucle_jeu = False

    # Vérifier si le joueur est mort.
