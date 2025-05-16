from random import randint
from pygame import *

lost = 0
class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, rect_x, rect_y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',10,self.rect.centerx,self.rect.top)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update (self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 420)
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('hq2-Photoroom.png',randint(10, 50), randint(80, 420), randint(0, 100))
    monsters.add(monster)

bullets = sprite.Group( )
player = Player('foni-papik-pro-94qf-p-kartinki-ishak-na-prozrachnom-fone-4.png', 10, 350, 400)

window = display.set_mode((700, 500))
display.set_caption('СВО')
background = transform.scale(image.load('EMi5uMjxaAM.png'),(700, 500))
mixer.init()
mixer.music.load('RXDXVIL - Bad Piggies Theme (PHONK Remix).mp3')
mixer.music.play()
game = True
finish = False
font.init()
font1 = font.Font(None, 36)
finish = False

score = 0
while game:
    clock = time.Clock()
    fps = 60
    clock.tick(fps)
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if not finish:
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        sprites_list = sprite.spritecollide(player, monsters, False)

        for s in sprites_list:
            score += 1
        window.blit(background,(0, 0))
        text_lose = font1.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (1, 1))
        player.reset()
        player.update()
        monsters.draw(window)
        monsters.update()
        display.update()
