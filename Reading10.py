import turtle

# turtle.setup(300 , 500)
# wn = turtle.Screen()
# wn.title("Handling keypresses!")
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()

# def h1():
#     tess.foward(30)
#
# def h2():
#     tess.left(45)
#
# def h3():
#     tess.right(45)
#
# def h4():
#     wn.bye()
#
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")
#
# wn.listen()
# wn.mainloop()



# turtle.setup(400 , 500)
# wn = turtle.Screen()
# wn.title("How to handle mouse clicks on the window!")
# wn.bgcolor("lightpink")
#
# tess = turtle.Turtle()
# tess.color("purple")
# tess.pensize(3)
# tess.shape("circle")
#
# def h1(x, y):
#     wn.title("Got click at coords {0}, {1}".format(x, y))
#     tess.goto(x, y)
#
# wn.onclick(h1)
# wn.mainloop()


# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Handling mouse clicks!")
# wn.bgcolor("lightyellow")
# tess = turtle.Turtle()
# tess.color("purple")
# alex = turtle.Turtle()
# alex.color("blue")
# alex.forward(100)
#
# def handler_for_tess(x, y):
#     wn.titel("tess clicked at {0}, {1}".format(x, y))
#     tess.left(42)
#     tess.forward(30)
#
# def handler_for_alex(x, y):
#     wn.title("Alex clicked at {0}, {1}".format(x, y))
#     alex.right(84)
#     alex.forward(50)
#
# tess.onclick(handler_for_tess)
# alex.onclick(handler_for_alex)
#
# wn.mainloop()



# turtle.setup(400, 500)
# wn = turtle.Screen()
# wn.title("Using a timer")
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("purple")
# tess.pensize(3)
#
# def h1():
#     tess.forward(100)
#     tess.left(56)
#
# wn.ontimer(h1, 2000)
# wn.mainloop()


#wn.mainloop()

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer to get events!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")

def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1,60)

h1()
wn.mainloop()