# Vous allez créer un jeu vidéo qui crée les statistiques de santé et d'attaque d'un personnage...

import os, random, time

def lance_de(nombre):
  result = random.randint(1, nombre)
  return result
  
def sante():
  santestat = ((lance_de(6)*lance_de(12))/2)+10
  return santestat

def force():
  forcestat = ((lance_de(6)*lance_de(8))/2 + 12)
  return forcestat

while True:
  print("CHAARACTERE BUILDER")
  print()
  name =  input("name your legend: ")
  type = input("charactere type of(human, elf, wiard, orc):")
  print()
  print(name)
  print("santé : ", sante())
  print("force :", force())
  print()
  repeat = input("repeat ? : ")
  if repeat == "NO" or repeat == "no":
     break
  time.sleep(0.6)
  os.system("clear")
  
  
  









