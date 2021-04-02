import pygame
import random

#TODO Make the black block move randomly - DONE
#TODO Replace the rectangles with  pictures - DONE
#TODO Make the space ship shoot
#TODO Split the player from blocks and make a new class - DONE
#TODO Make a Bullet class

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, fName, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(fName)
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-2, 2)
        self.y_vel = random.randrange(-2, 2)

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

class Player(pygame.sprite.Sprite):
    def __init__(self, fName):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image = pygame.image.load(fName)
        self.rect = self.image.get_rect()
    def moveBlock(self):
        pass

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
    # Move the bullet
        self.rect.y -= 3


pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for i in range(50):
    block = Block("rock2.png", 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player("spaceship.png")
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 40
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    for block in all_sprites_list:
        block.update()

    for bullet in bullet_list:
        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in blocks_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
    
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

