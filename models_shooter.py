from pygame import *
from random import randint
import time as tm
winSize = (700,500)
color = (255,255,255)
SPSize = (65,75)
UFOsize = (75,65)
winows = display.set_mode(winSize)
display.set_caption("Shooter")
time.get_ticks()
font.init()
mixer.init()
interval = 0.1111
fireTime = 0
shot = mixer.Sound("fire.ogg")
shot.set_volume(0.01)
font1 = font.Font(None,24)
font2 = font.Font(None, 70)
enemies = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()


class Counter:
    def __init__(self, fontObj, color):
        self.lost = 0
        self.killed = 0
        self.fontObj = fontObj
        self.color = color
    def show(self):
        self.lostObj = self.fontObj.render("Пропущено: " +  str(self.lost), 1, self.color)
        winows.blit(self.lostObj, (0,0))
        self.killedObj = self.fontObj.render("Вбито: " +str(self.killed), 1, self.color )
        winows.blit(self.killedObj, (0,30))

count = Counter(font1,color)

class GameSprite(sprite.Sprite):
    def __init__(self, playerImage, playerX, playerY, playerSpeed,SPSize1):
        super().__init__()
        self.spsize = SPSize1
        self.image= transform.scale(image.load(playerImage), self.spsize)
        self.playerSpeed = playerSpeed
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY
        self.rect.centerx = playerX
        self.rect.top = playerY

    def spawn(self):
        winows.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.playerSpeed
        if self.rect.y <= 0:
            self.kill()

class Player(GameSprite):
    def update(self):
        keys= key.get_pressed()
        if keys[K_a] and self.rect.x > 0 and not keys[K_LEFT]:
            self.rect.x-=self.playerSpeed
        if keys[K_d] and self.rect.x < winSize[0] - SPSize[0] - 5 and not keys[K_RIGHT] :
            self.rect.x+=self.playerSpeed
        if keys[K_LEFT] and self.rect.x > 0 and not keys[K_d]:
            self.rect.x-=self.playerSpeed
        if keys[K_RIGHT] and self.rect.x < winSize[0] - SPSize[0] - 5 and not keys[K_a]:
            self.rect.x+=self.playerSpeed
    def fire(self):
        global fireTime
        keys= key.get_pressed()
        if keys[K_SPACE] and tm.time() > fireTime + interval:
            fireTime = tm.time()
            bullet = Bullet("bullet.png", self.rect.centerx , self.rect.top, 5, (5,10))
            shot.play()
            
            bullets.add(bullet)

class Enemy(GameSprite):
    def __init__(self, playerImage, playerX, playerY, playerSpeed,SPSize1,Destroy):
        super().__init__(playerImage, playerX, playerY, playerSpeed,SPSize1)
        self.Destroy = Destroy
    def update(self):
        self.lostEnemy = 0
        if self.rect.y <= winSize[1] :
            self.rect.y += self.playerSpeed
        if self.rect.y > winSize[1] :
            self.rect.y = 0
            self.rect.x = randint(0,winSize[0]-SPSize[0])
            if self.Destroy:
                count.lost += 1
            