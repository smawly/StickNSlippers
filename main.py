import time
import random
p1hp = 100
p2hp = 100

def p1turn():
    print("Attack or Heal")
    choice = input("")
    if choice == "Attack":
        p1attack()
#------------------------
def p1attack():
    global p2hp
    dmg = random.randint(16,25)
    p2hp -= dmg
    print("You have damaged "+str(dmg)+"HP")
# ------------------------
def p1heal():
    global p1hp
    if p1hp > 99:
        print("Your HP is full choose other sections")
        p1turn()
    else:
        p1hp += 18
#------------------------

p1turn()