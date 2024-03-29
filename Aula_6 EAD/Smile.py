import turtle

t = turtle.Turtle()

t.pencolor("black")
t.pensize(width=10)

t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-40, 120)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, 120)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-70, 70)
t.pendown()
t.setheading(-60)
t.circle(80, 120)

turtle.done()
