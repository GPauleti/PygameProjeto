import pygame as pg
import json
from enemy import Enemy
import constants as c

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

#IMAGES

#map
map_image = pg.image.load('levels/level.png').convert_alpha()
#enemies
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

waypoints = [
  (100, 100),
  (400, 200),
  (400, 100),
  (200, 300)
]

#GROUPS
enemy_group = pg.sprite.Group()

enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

#LOOP
run = True
while run:

  clock.tick(c.FPS)

  screen.fill("grey100")
  pg.draw.lines(screen, "grey0", False, waypoints)

  #GROUP UPDATE
  enemy_group.update()

  #GROUP DRAW
  enemy_group.draw(screen)

  #event handler
  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False

  pg.display.flip()

pg.quit()