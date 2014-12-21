import turtle

turtle.hideturtle()
turtle.speed(0)

x,y=turtle.position()

def brush_circle_red(x,y):
    turtle.penup()
    turtle.color("red")
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(50)

def brush_square_red(x,y):
    turtle.begin_fill()
    turtle.color("red")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    turtle.end_fill()

def brush_circle_blue(x,y):
    turtle.penup()
    turtle.color("blue")
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(50)


def brush_square_blue(x,y):
    turtle.begin_fill()
    turtle.color("blue")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    turtle.end_fill()




turtle.onclick(brush_circle_red, btn=1, add=True)
turtle.onscreenclick(brush_circle_red, btn=1, add=True)
turtle.ondrag(brush_circle_red, btn=1, add=True)


turtle.onclick(brush_square_red, btn=3, add=True)
turtle.onscreenclick(brush_square_red, btn=3, add=True)
turtle.ondrag(brush_square_red, btn=3, add=True)




turtle.listen()
turtle.mainloop()
