from pygame import *
back = (0,0,128) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
window.fill(back)

game = True
finish = False

clock = time.Clock()
FPS = 60
while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False

    display.update()
    clock.tick(FPS)

