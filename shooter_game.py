#Створи власний Шутер!
from models_shooter import *

win = font2.render("WIN", True, color)
louse = font2.render("LOUSE", True, color)


mixer.music.load("space.ogg")
mixer.music.set_volume(0.1)
mixer.music.play()
clock = time.Clock()
player = Player("rocket.png", 10, 410 ,15,UFOsize)

background = transform.scale(image.load("galaxy.jpg"),winSize)
# посмотрет тайм и + сделать перемещение других врагов и пули 
game = True
game_pause = False
FPS = 60
ranEnemy = []
for i in range(5):
    enemies.add(Enemy("ufo.png", randint(0,winSize[1]-SPSize[1]), randint(-100,0),3,SPSize,True))
for i in range(5):
    asteroids.add(Enemy("asteroid.png", randint(0,winSize[1]-SPSize[1]), randint(-100,0),1,SPSize,False))

while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not game_pause:
        winows.blit(background,(0,0))

        player.spawn()
        player.update()
        player.fire()
        enemies.draw(winows)
        enemies.update()
        asteroids.draw(winows)
        asteroids.update()
        bullets.draw(winows)
        bullets.update()
        sprite.groupcollide(bullets,asteroids,True,False)
        if sprite.groupcollide(bullets,enemies,True,True):
            count.killed += 1
            enemies.add(Enemy("ufo.png", randint(0,winSize[1]-SPSize[1]), randint(-100,0),3,SPSize,True))
        if count.killed >= 10:
            winows.blit(win, (winSize[0] / 2 , winSize[1] / 2))
            game_pause = True
        elif count.lost >=3 or sprite.spritecollide(player,enemies,False) or sprite.spritecollide(player,asteroids,False):
            winows.blit(louse, (winSize[0] / 2 , winSize[1] / 2))
            game_pause = True
        
        count.show()
        clock.tick(FPS)
        display.update()