from pygame import *
back = (0,255,0) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
window.fill(back)

speed_x = 3 
speed_y = 3

ball_pic = 'ball.png'
player_pic = 'player.png'
back_pic = 'фон.jpg'

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,player_speed, width, height,speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def reset(self):
        window.blit(self.image, (self. rect.x, self. rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height - 150: 
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - 150: 
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed

class Ball(GameSprite):
    
    def run(self,roc1,roc2):

        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y

        if self.rect.y >= 450:
            self.speed_y *= -1
        if self.rect.y <= 10:
            self.speed_y *= -1

        if sprite.collide_rect(roc1, self) or sprite.collide_rect(roc2, self):
            self.speed_x *= -1


game = True
finish = False

clock = time.Clock()
FPS = 60


back = GameSprite(back_pic,0,0,0,win_width,win_height,0,0)
ball = Ball(ball_pic, 200, 200, 4, 50, 50,3,3)
player_1 = Player(player_pic, 20, 200, 6, 20, 150,0,0)
player_2 = Player(player_pic, 550, 100, 6, 20, 150,0,0)

while game:
    for e in event.get(): 
        if e.type == QUIT: 
            game = False

    back.reset()
    ball.reset()
    player_1.reset()
    player_2.reset()

    player_1.update_l()
    player_2.update_r()
    ball.run(player_1,player_2)
    
    display.update()
    clock.tick(FPS)

