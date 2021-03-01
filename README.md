# chess-tournaments

#Introduction 
Cette application a pour but de gérer l'organisation des tournois d'échecs suisse.
Il permet de créer un tournois, d'ajouter des joueurs et de générer des matchs suivant les classements des joueurs, 
Une base de données permet de sortir de l'application à tout moment sans perdre les informations.

# Notice :

Lors de l'ouverture de l'application le menu général apparaitra :

1 : Créer un tournoi
2 : Tournois en cour
3 : Liste de tous les acteurs d'un tournoi
4 : Liste de tous les joueurs
5 : Liste de tous les tournois
6 : Liste de tous les tours d'un tournoi
7 : Liste de tous les matchs d'un tournoi
S : Sauvegarder
E : Effacer la base de données
Q : Quitter)


1) pour la création d'un tournoi il vous faudra renseigner son nom, la date, le lieu, le nombre de tours (valeurs par défaut 4), le contrôleur de temps (Bullet, blitz, coup rapide), le nombre de participants, et une description(facultatif).
Le tournois est créé, il vous sera demandé de renseigner les informations des joueurs :
 Le prénom, le nom, la date de naissance, le sexe (m ou f), et le niveau du joueur.
 Cette opération se répète jusqu'à ce que le nombre des joueurs renseigner dans la création du tournoi soit atteint.

2) Le menu 'tournois en cour' est disponible seulement si des tournois sont créer.
   C'est dans ce menu que l'utilisateur renseignera les scores des matchs.

3) Affiche tous les joueurs d'un tournois sélectionnés.

4) Affiche tous les joueurs de tous les tournois

5) Affiche tous les tournois (en cour et fini)

6) Affiche tous les tours d'un tournoi (seulement ceux qui ont déjà été fait).

7) Affiche la liste de tous les matchs d'un tournoi (seulement ceux qui ont déjà été fait).

s) Sauvegarde l'intégralité des informations, celle-ci seront restauré automatiquement lors de l'ouverture de l'application.

e) Efface la base de données.


# Installation

-Avec CMD, placez-vous dans votre dossier
-Créez un environnement avec la commande : python -m venv env
-Activez votre environnement avec la commande : env\Scripts\activate
-Installez les paquets avec la commande : pip install -r requirements.txt
-Exécutez le programme avec la commande : python main.py
