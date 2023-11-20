# créons un générateur de statistiques de santé pour un personnage de jeu vidéo.

# Créez un sous-programme qui lance un dé de n’importe quelle taille et renvoie ce nombre.
# Ensuite, créez un deuxième sous-programme qui lance un dé à six faces et un dé à huit faces.
# Multipliez le nombre des dés à six faces et des dés à huit faces et renvoyez ce sous-programme en tant que statistiques de santé d'un personnage pour un jeu vidéo.
# Imprimez les statistiques de santé du personnage.

import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")


haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")