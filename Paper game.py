import pygame
import math
#test
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("zelda.jpg").convert()
ball_sprite = pygame.image.load("paper20.png").convert()
ball_sprite.set_colorkey(RED)

class Ball():
    def __init__(self):
        self.x = ""
        self.y = ""
        self.changex = 0
        self.changey = 0

    def move(self):
        self.x += self.changex
        self.y += self.changey

paper_ball = Ball()
paper_ball.x = 0
paper_ball.y = 0



# Loop until the user clicks the close button.
done = False


# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:


    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            paper_ball.changex += 1
            paper_ball.changey += 1
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    screen.blit(background_image, [0, 0])

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    
    paper_ball.move()

    screen.blit(ball_sprite, [paper_ball.x, paper_ball.y])

       

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()