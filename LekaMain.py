#import random
import time

print("##########################\n#                        #\n#   Leka: The RPG Game   #\n#                        #\n##########################\n\n\n")

playerhealth = 100
playerarmor = 5

def death():
    if playerhealth == 0:
      print("######################\n#                    #\n#      GAME OVER     #\n#                    #\n######################")
#name
name = input("What is your name?: ")

print("Hello", name + "\n")
time.sleep(1)
print(name + ", you are a wandering soul.")
time.sleep(1)
print("You have 5 Rows in your pocket.")
time.sleep(1)
print("You get on a boat to Leka")
time.sleep(1)
print("When you get to Leka you go to which of the three major cities\n")
time.sleep(1)
print("You can go to Lockin, Heedly, Guent.")
#where the player whats to go
travelLoc = input("use where do you want to go?: ")

if travelLoc == "Lockin":
    print("\n")
    time.sleep(1)
    print("Kone: Hey there stranger")
    time.sleep(1)
    print("Kone: The names Kone")

    time.sleep(1)
    KoneAnswer1 = input("A) Tell Kone your name. B) Why he's talking to you.: ")

    time.sleep(1)
    if KoneAnswer1 == "A":
        print(name + ": I'm " + name)
        time.sleep(1)
        print("Kone: Hey " + name)
    elif KoneAnswer1 == "B":
        print(name + ": Excuse why are you talking to me?")
        time.sleep(.5)
        print("Kone: Ooh! I'm the town guide")
        print("Kone:print i'll be showing you around")
    else:
        print("Kone: Ok then")

if travelLoc == "Heedly":
    print("gay")
