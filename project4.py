from utils import *

# The goal of my game is to generate money by clicking space, which you can then use to buy pointe shoes by clicking p. If you buy 10 pairs of pointe shoes you win and go to a dance summer intensive.

# Section 1 - setup
set_background("shoeshop")

money = 0
pointeshoes = 0
money_sprite_list = []
pointeshoe_sprite_list = []


# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()
m2 = create_sprite("baseball", -350,100) 
m2.hideturtle()



# Section 2 - controls

def getmoney():
    # the "getmoney" control adds 10 to the money variable, creates a money sprite in a random spot on the screen, and adds the sprite to a list so it can easily be hidden later, such as when money is minused because the player buys pointe shoes, and when the player wins.
    global money
    money += 10
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    s1 = create_sprite("money",x,y)
    money_sprite_list.append (s1)


window.onkeypress(getmoney, "space")


def getpointeshoes():
    # the "getpointeshoes" control checks if money is greater than 100, and if it  is, it allow a series of actions to happen when the "p" key is pressed; it adds 1 to the pointe shoes variable, minuses 100 money, and creates a pointe shoe sprite in a random spot on the screen. It also adds the sprites that have been created to a list so that they can be hidden easier once the player has won.
    global pointeshoes , money
    if money >= 100:
        pointeshoes += 1
        money -= 100
        x = random.randint (-200,200)
        y = random.randint (-200,200)
        s2 = create_sprite("pointeshoes",x,y)
        pointeshoe_sprite_list.append (s2)

        for i in range (10):
            s = money_sprite_list.pop()
            s.hideturtle()


window.onkeypress(getpointeshoes, "p")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    if pointeshoes >= 10:
        set_background ("lines")
        for s in money_sprite_list:
            s.hideturtle()
        for s in pointeshoe_sprite_list:
            s.hideturtle()
        m2.clear()
        m2.color ("white")
        m2.write ("You won! You're going to Alonzo King Lines Summer Program!",font = ("Arial", 15, "normal"))
        


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"Money: {money} \nPointe Shoes: {pointeshoes}")

    time.sleep(0.01)
    window.update()