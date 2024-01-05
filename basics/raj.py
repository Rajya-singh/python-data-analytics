from turtle import *
bgcolor('black')
speed('fast')
color['red','purple','blue','green','yellow','orange',]
for x in range(180):
    pencolor(color[x%2])
    width(x/50+1)
    forward(x)
    left(39)
mainloop()