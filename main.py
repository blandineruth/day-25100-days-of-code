



# Defi Jouez une chanson de cette réplique et créez un menu pour l'accompagner. Faites-le ressembler à un iPod !

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stopplayback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
    if stopplayback == 2:
      source.paused = True
      play()
    else:
      continue
while True:
  os.system("clear")
  print("my Pod player music player")
  time.sleep(1)
  print("press 1 to play music")
  time.sleep(1)
  print("press 2 to stop music")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue

  
  
