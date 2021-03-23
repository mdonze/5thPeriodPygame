import pygame
pygame.init()
# Variables for our game
# colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
# size of the Window size
size = [700, 500]
# variable for the screen
screen = pygame.display.set_mode(size)
# Set the name of Window
pygame.display.set_caption("My Game")
# controls the game loop
playing = True
# Helps Control the FPS(how quickly the screen updates)
clock = pygame.time.Clock()

#----GAME LOOP ----
while playing:
  # check and handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False
  
  # ---- Game Logic (update variables)

  # ---- Drawing
  screen.fill(BLACK)

  # at the end of Drawing
  pygame.display.flip()

  # update the clock
  clock.tick(60)
