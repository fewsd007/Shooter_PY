from pygame import *
back = (0,0,128) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
window.fill(back)

ball_pic = 'ball.png'
player_pic = 'player.png'

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self. rect.x, self. rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed

game = True
finish = False

clock = time.Clock()
FPS = 60

speed_x = 3 
speed_y = 3

ball = GameSprite(ball_pic, 200, 200, 4, 50, 50)
player_1 = Player(player_pic, 20, 200, 6, 200, 50)

while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False

    ball.reset()
    player_1.reset()

    player_1.update_l()

    display.update()
    clock.tick(FPS)

