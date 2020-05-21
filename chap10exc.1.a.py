import turtle

turtle.setup(300 , 500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def h1():
    tess.foward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

def h5():
    tess.color("red")

def h6():
    tess.color("green")

def h7():
    tess.color("blue")

def h8():
    tess.pensize()

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "r")
wn.onkey(h6, "g")
wn.onkey(h7, "b")


wn.listen()
wn.mainloop()
