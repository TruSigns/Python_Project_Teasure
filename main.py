print("Welcome to the island")
print("Find the Treasure")

c1 = input('Youre on a island. Which way are you trying to go? Type "left" or "right".').lower()

if c1 == "left":
 #continue
    c2 = input("You're at a lake").lower()
    if c2 == "wait":
        c3 = input("You're there unarmed").lower()
        if c3 == "red":
            print("Definitely not the right room")
        elif c3 == "yellow":
            print("Found the Teasure")
        elif c3 == "Blue":
            print("Room with a beast in")
    else:
     print("You were attacked")
else:
    print("Game Over")
