from turtle import *
pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    fd(120)
    lt(50)
    end_fill()
mainloop()

