import turtle
t=turtle.Turtle()
s=turtle.Screen()  
s.bgcolor("black") 
s.setup(700,600)  
t.width(2) 
t.speed(20) 
t.hideturtle() 
color=['violet',"indigo",'blue','green',"yellow",'orange','red']
for i in range(100):
    t.pencolor(color[i%7])  
    t.forward((i*4))
    t.right(263) 
turtle.done
