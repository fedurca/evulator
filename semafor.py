#Python program to draw color filled hexagon in turtle programming
import turtle
 
t = turtle.Turtle()
t.fillcolor('red')
t.penup()
t.setpos(100,100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
#t.left(270)
#t.forward(20)
t.setpos(100,150)
t.pendown()

t.fillcolor('orange')
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

t.penup()
t.setpos(100,100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
#t.left(270)
#t.forward(20)
t.setpos(100,150)
t.pendown()

t.fillcolor('green')
t.begin_fill()
for i in range(6):
  t.forward(150)
  t.right(60)
t.end_fill()
t.forward(45)
t.fillcolor('red')
t.begin_fill()
for i in range(6):
  t.forward(150)
  t.right(60)
t.end_fill()


#calling for the mainloop()
turtle.mainloop()

