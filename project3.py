from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = 230
x2 = -200
y2 = 100
x3 = -200
y3 = -50
x4 = -200
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("racetrack_finish")
t1 = create_sprite("mycar",x1,y1)
t2 = create_sprite("yellowcar",x2,y2)
t3 = create_sprite("bluecar",x3,y3)
t4 = create_sprite("images",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or 
# sprite one will travel between 5 and 20 randomly, but always beat sprite 4. sprite 2 has a 4/5 chance of not moving at all, but it has a 1/5 chance of going 21 steps, and would beat everyone. sprite 3 with always go 8, beating sprite 4, and 3 could win depending on sprite 1 and 2's randomness. x4 will always go 4, so it will never win, but it could beat sprite 2 depending on the randomness.
for i in range(30):
    x1 += random.randint (5,20)
    x2 += random.choice ([1,1,1,1,21])
    x3 += 8
    x4 += 4

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("tatemcraeflag",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Silver car wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("Yellow car wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("Blue car wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    s5.write("Red car wins!")

turtle.exitonclick()