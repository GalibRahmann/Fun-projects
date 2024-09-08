import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("Black")
t.pencolor("Red")
t.speed(100)
for i in range(250):
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.lt(18)
