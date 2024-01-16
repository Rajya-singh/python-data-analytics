import pgzrun
import random

WIDTH=400
HEIGHT=400

b1=Rect((10,10),(50,50))
b2=Rect((200,200),(75,100))
music.play('m1')

def draw():
    screen.clear()
    screen.draw.filled_rect(b1,'red')
    screen.draw.filled_rect(b2,'blue')
    screen.draw.text('game',(120,20),
                     color='white',fontsize=50)
def move(box,axis,speed=1):
    if axis =='x':
        if box.x > WIDTH:
            box.x=0
        box.x += speed  #speed left to right
    if axis == 'y':
        if box.y > HEIGHT:
            box.y = 0
        box.y += speed

def update():
    print('rurnning')
    move(b1, 'x', 50)
    move(b2, 'y', 25)
pgzrun.go()
