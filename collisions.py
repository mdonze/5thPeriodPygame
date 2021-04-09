import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

game_over = False

class Block(pygame.sprite.Sprite):
    def __init__(self, fName, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        big_image = pygame.image.load(fName)
        big_image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(big_image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.xVel = random.randrange(-2, 2)
        self.yVel = random.randrange(-2, 2)

    def change_x(self):
        self.xVel = self.xVel * -1

    def change_y(self):
        self.yVel = self.yVel * -1

    def update(self):
        self.rect.x += self.xVel
        self.rect.y += self.yVel

class Player(pygame.sprite.Sprite):
    def __init__(self, fName, width, height):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        big_ss = pygame.image.load(fName)
        big_ss.set_colorkey(WHITE)
        self.image = pygame.transform.scale(big_ss, (width, height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 350
        self.is_alive = True

    def update(self):
        pass

    def isDead(self):
        self.kill()
        self.is_alive = False
        global game_over 
        game_over = True

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    def update(self):
    # Move the bullet
        self.rect.y -= 3


pygame.init()
score  = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Score: " + str(score), True, RED, BLACK)
textRect = text.get_rect()
textRect.center = (100, 20) 

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

for i in range(50):
    block = Block("asteroid.png", 40, 40)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height - 200)
    block_list.add(block)
    all_sprites_list.add(block)

player = Player("spaceshipC.png", 30, 40)
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 15
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    if not game_over:
        screen.fill(BLACK)
        pos = pygame.mouse.get_pos()
        player.rect.x = pos[0]
        
        all_sprites_list.update()

        for bullet in bullet_list:
            blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
            for block in blocks_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1
                print(score)
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
        
        for block in block_list:
                if pygame.sprite.collide_mask(block, player):
                    player.isDead()
                if block.rect.y > screen_height:
                    block.change_y()
                if block.rect.y < 0:
                    block.change_y()
                if block.rect.x > screen_width:
                    block.rect.x = 0
                if block.rect.x < 0:
                    block.rect.x = screen_width
        
        all_sprites_list.draw(screen)
        text = font.render("Score: " + str(score), True, RED, BLACK)
        screen.blit(text, textRect)
    else:
        screen.fill(RED)
    pygame.display.flip()
    clock.tick(60)

