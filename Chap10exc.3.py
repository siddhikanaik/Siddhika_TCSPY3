import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes light")
wn.bgcolor("lightgreen")
redcircle = turtle.Turtle()
orangecircle = turtle.Turtle()
greencircle = turtle.Turtle()

def turtle_setups():
    redcircle.setpos(40, 40)
    redcircle.shape("circle")
    redcircle.shapesize(3)
    redcircle.fillcolor("red")
    orangecircle.setpos(40, 175)
    orangecircle.shape("circle")
    orangecircle.shapesize(3)
    orangecircle.fillcolor("orange")
    greencircle.setpos(40, 115)
    greencircle.shape("circle")
    greencircle.shapesize(3)
    greencircle.fillcolor("green")

def draw_housing():
    redcircle.pensize(3)
    redcircle.color("black", "darkgrey")
    redcircle.begin_fill()
    redcircle.forward(80)
    redcircle.left(90)
    redcircle.forward(200)
    redcircle.circle(40, 180)
    redcircle.forward(200)
    redcircle.left(90)
    redcircle.end_fill()


draw_housing()
redcircle.penup()
redcircle.forward(40)
redcircle.left(90)
redcircle.forward(50)
turtle_setups()

state_num = 0
redcircle.hideturtle()
orangecircle.hideturtle()
greencircle.hideturtle()

def advance_state_machine():
    global state_num
    if state_num == 0:
        redcircle.hideturtle()
        greencircle.hideturtle()
        orangecircle.hideturtle()
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1:
        redcircle.showturtle()
        orangecircle.hideturtle()

wn.mainloop()