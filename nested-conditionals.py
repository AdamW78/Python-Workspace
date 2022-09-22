import random


class Player:
    def __init__(self, name, moving):
        self._health = 20;
        self.name = name;
        self.moving = moving;
        self.alive = True;

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if value <= 0:
            print("You died!")
            self.alive = False
            exit(0)


playerOne = Player("username", False)
playerOne.moving = True;

leftRight = input("Quickly: You are on a cliff that is crumbling, please decide whether to go left or"
                  " right (type your decision here): ").casefold()
if leftRight == "left" or leftRight == "l" or leftRight == "le" or leftRight == "lef":
    rockhit = random.randint(10, 15)
    playerOne.health -= rockhit
    print(f"Going left lead to being hit by a rock and losing {rockhit} health! Ouch!")
    leftbool = True
elif leftRight == "right" or leftRight == "r" or leftRight == "ri" \
        or leftRight == "rig" or leftRight == "righ":
    print("You dodged a rock to your left that surely would have hurt! Lucky!")
    leftbool = False
else:
    print("You weren't able to decide and fell off the cliff!")
    playerOne.health -= 20
movingdec = input("Do you want to keep moving or stay where you are at? Enter \"move\" or \"stay\": ").casefold()
if movingdec == "move":
    playerOne.moving = True
elif movingdec == "stay":
    playerOne.moving = False
else:
    print("You couldn't decide whether to move or stay, so you flip a coin!")
    decision = random.randint(0, 1)
    if decision == 0:
        playerOne.moving = True
        direction = "left" if leftbool else "right"
        print(f"The coin landed on heads! You decide to keep moving {direction}!")
    else:
        print("The coin landed on tails! You decide to stay still.")
        playerOne.moving = False

if playerOne.moving:
    if playerOne.health >= 10:
        print("You were able to move fast enough to escape the crumbling cliff!")

    else:
        playerOne.health -= 5
        print("You slip and take some damage, but barely escape the crumbling cliff!")
else:
    healthhit = random.randint(10, 20)
    if healthhit > 0:
        print(f"You are hit by a spell that takes away {healthhit} health!")
        if playerOne.health > healthhit:
            print(f"You survived with {playerOne.health - healthhit}/20 health remaining!")
            playerOne.health -= healthhit
        else:
            playerOne.health -= healthhit

    elif healthhit < 0:
        print(f"You are hit with a healing spell that gives you {-1*healthhit} health back!")
        if playerOne.health == 20:
            print("Too bad! You are already at full health!")
        elif playerOne.health+(-1 * healthhit) >= 20:
            playerOne.health = 20
            print("You are brought back to full health by the spell!")
        else:
            playerOne.health -= healthhit
    else:
        print("Nothing happened!")

print("You survived! Congratulations!")
print(f"You had {playerOne.health}/20 health left!")