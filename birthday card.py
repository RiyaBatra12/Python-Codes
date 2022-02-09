import turtle
t=turtle.Turtle()
t.width(7)
s=turtle.Screen()
s.bgcolor("orange")
x=-50
y=0
t.setx(x)
t.sety(y)
t.color("black","pink")
t.begin_fill()
t.hideturtle()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.end_fill()
t.right(90)
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.forward(40)
t.end_fill()
t.left(90)
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(40)
t.left(90)
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(40)
t.right(90)
t.forward(30)
t.end_fill()
t.width(5)
t.right(90)
t.forward(40)
t.right(90)
t.forward(30)
t.right(90)
t.forward(20)
t.left(90)
t.forward(30)
t.width(5)
t.color("black","yellow")
t.begin_fill()
t.left(30)
t.forward(5)
t.right(30)
t.forward(5)
t.right(30)
t.forward(5)
t.right(90)
t.forward(5)
t.right(30)
t.forward(5)
t.right(30)
t.forward(5)
t.right(30)
t.forward(5)
t.end_fill()
t.color("black")
t.begin_fill()
t.left(30)
t.forward(25)
t.end_fill()


t.penup()
x=-310
y=-150
t.setx(x)
t.sety(y)

t.pendown()
t.color("Blue")
t.write("HAPPY BIRTHDAY",font=("comic sans ms",50,"bold"))

t.penup()
x=-150
y=-250
t.setx(x)
t.sety(y)

t.pendown()
t.color("Blue")
t.write("Name",font=("comic sans ms",50,"bold"))











