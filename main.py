import time
import random
p1hp = 100
p2hp = 100
name = input("Choose a nickname")
while p1hp >= 0 or p2hp >= 0:
    def p1turn():
        print("Attack or Heal")
        choice = input("").lower()
        if choice == "attack":
            p1attack()
        elif choice == "heal":
            p1heal()
        else:
            p1turn()
    #------------------------
    def p1attack():
        global p2hp
        dmg = random.randint(16,25)
        p2hp -= dmg
        print("You have damaged "+str(dmg)+"HP")
        print(f"{name} HP = {p1hp}")
        print(f"Enemy HP = {p2hp}")
        if p2hp == abs(p2hp):
            time.sleep(1)
            print("\n////////////////////////////////////\n")
            p2move()
        else:
            print("You JUST WON !")
    #------------------------
    def p1heal():
        global p1hp
        if p1hp > 88:
            print("Your HP cant be greater than 100")
            print(f"{name} HP = {p1hp}")
            print(f"Enemy HP = {p2hp}")
            p1turn()
        else:
            p1hp += 18
            p2move()
    #------------------------

    def p2move():
        a = random.randint(0, 10)
        global p1hp
        global p2hp
        if a > 7:
            p2hp +=18
            print("Computer Healed 18HP")
            print(f"{name} HP = {p1hp}")
            print(f"Enemy HP = {p2hp}")
            p1turn()
        else:
            b = random.randint(16,25)
            p1hp -= b
            print("Computer has damaged "+str(b)+" HP")
            print(f"{name} HP = {p1hp}")
            print(f"Enemy HP = {p2hp}")
            if p1hp == abs(p1hp):
                p1turn()
            else:
                print("Computer Wins")
    p1turn()
