import pygame
import os

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((600, 600))

hero = pygame.Rect(50, 50, 40, 45)

pressed_right = False
pressed_left = False
pressed_up = False
pressed_down = False

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

stone_wall = pygame.image.load(img_path + "/wall.png")
flag = pygame.image.load(img_path + "/flag_ukr.png")
Wooden_floor = pygame.image.load(img_path + "/floor.png")
geroi = pygame.image.load(img_path + "/hero_ukr.png")
shared_flag= pygame.image.load(img_path + "/flag_ukr_2.png")
bitcoin = pygame.image.load(img_path + "/bitcoin.png")

moneta1 = pygame.Rect(50, 200, 50, 50)
moneta2 = pygame.Rect(350, 200, 50, 50)
moneta3 = pygame.Rect(450, 500, 50, 50)

money_list = [moneta1, moneta2, moneta3]

textures = [
   [1,1,1,1,1,3,3,3,3,1,1,1],
   [1,3,1,3,3,3,1,1,3,5,1,1],
   [1,3,3,3,1,1,1,1,1,1,1,1],
   [1,3,1,1,1,3,3,3,1,1,1,1],
   [1,3,3,3,3,3,1,3,1,1,1,1],
   [1,3,1,1,1,3,3,3,1,1,1,1],
   [1,3,1,1,1,1,1,1,1,1,1,1],
   [1,3,3,3,3,3,3,3,3,2,1,1],
   [1,3,1,1,1,1,1,1,1,1,1,1],
   [1,3,1,1,1,1,1,1,1,1,1,1],
   [1,3,3,3,3,3,3,3,3,3,1,1],
   [1,1,1,1,1,1,1,1,1,1,1,1],
]

rects = [] 
rects_textures = []

bad_rects = []
good_rects = []

x = 0
y = 0

for texture in textures: 
    for i in texture: 
        kvadrat = pygame.Rect(x, y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 1 or i == 5:
            bad_rects.append(kvadrat)
        if i == 2:
            good_rects.append(kvadrat)
        x += 50 
    y += 50   
    x = 0

font = pygame.font.SysFont("Arial", 70)
text = font.render("YOU WIN!", True, (255,0,0))

game = True

while game:

   display.fill((255, 0, 0))
   pygame.draw.rect(display, (0,0,0), hero)

   for i in range(144):
      if rects_textures[i] == 1:
         display.blit(stone_wall, rects[i])
      if rects_textures[i] == 2:
         display.blit(flag, rects[i])
      if rects_textures[i] == 3:
         display.blit(Wooden_floor, rects[i])
      if rects_textures[i] == 5:
         display.blit(shared_flag, rects[i])
   
   display.blit(geroi, hero)

   if hero.y < 0:
      hero.x = 50
      hero.y = 50 

   for moneta in money_list:
      display.blit(bitcoin, moneta)
      if hero.colliderect(moneta):
         money_list.remove(moneta)
         break

   for bad in bad_rects:
      if hero.colliderect(bad):
         hero.x = 50
         hero.y = 50
   
   for good in good_rects:
      if hero.colliderect(good):
         display.fill((0, 0, 0))
         display.blit(text, (140, 150))

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game = False

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_d:
            pressed_right = True
         if event.key == pygame.K_a:
            pressed_left = True
         if event.key == pygame.K_w:
            pressed_up = True
         if event.key == pygame.K_s:
            pressed_down = True
      
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_d:
            pressed_right = False
         if event.key == pygame.K_a:
            pressed_left = False
         if event.key == pygame.K_w:
            pressed_up =  False
         if event.key == pygame.K_s:
            pressed_down = False
   
   if pressed_right == True:
      hero.x += 5
   if pressed_left == True:
      hero.x -= 5
   if pressed_up == True:
      hero.y -= 5
   if pressed_down == True:
      hero.y += 5

   pygame.display.flip()
   clock.tick(60)