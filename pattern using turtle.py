import turtle
t=turtle.Turtle()
s=turtle.Screen()  #for the screen
s.bgcolor("black") #for background color
s.setup(700,600)  #for the height and width of screen the first thing in bracket is width and second is height
t.width(2) #this is for the width of turtle
t.speed(20) #this is for the speed of turtle
t.hideturtle() #to hide turtle
color=['yellow','blue','green','red','pink','orange']
for i in range(100):
    t.pencolor(color[i%6])  #color of the turtle
    t.forward((i*4))
    t.right(150) #marke new desing with new angles
turtle.done
