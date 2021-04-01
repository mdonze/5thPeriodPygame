import pygame
import random

#TODO Make the black block move randomly - DONE
#TODO Replace the rectangles with pictures
#TODO Make the space ship shoot

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, fName, width, height, isPlayer):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(fName)
        self.rect = self.image.get_rect()
        self.player = isPlayer
        self.x_vel = random.randrange(-2, 2)
        self.y_vel = random.randrange(-2, 2)

    def moveBlock(self):
        if self.player == False:
            self.rect.x += self.x_vel
            self.rect.y += self.y_vel
        

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block("bigRock.png", 20, 15, False)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)

player = Block("bigRock.png", 20, 15, True)
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    for block in all_sprites_list:
        block.moveBlock()

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)
    
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

