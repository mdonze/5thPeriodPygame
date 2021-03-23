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

# Variables to keep track of stick guy's position
x_coord = 10
y_coord = 10

# variables for velocity
x_speed = 0
y_speed = 0

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)
    # Legs
    pygame.draw.line(screen, BLACK, [5+x, 17+y],[10+x, 27+y],2)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 2)
    # Body
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)
    # Arms
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)

#----GAME LOOP ----
while playing:
  # check and handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_speed = -3
        elif event.key == pygame.K_RIGHT:
            x_speed = 3
        elif event.key == pygame.K_UP:
            y_speed = -3
        elif event.key == pygame.K_DOWN:
            y_speed = 3
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_speed = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_speed = 0
  # ---- Game Logic (update variables)
  x_coord = x_coord + x_speed
  y_coord = y_coord + y_speed

  # ---- Drawing
  screen.fill(WHITE)
  draw_stick_figure(screen, x_coord, y_coord)

  # at the end of Drawing
  pygame.display.flip()

  # update the clock
  clock.tick(60)
