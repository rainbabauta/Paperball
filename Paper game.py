import pygame
import math
#test
#Leo rules

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

change_pos = False

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = ""
        self.y = ""
        self.changex = 0
        self.changey = 0
        self.gravity = .025

        self.ball_sprite = pygame.image.load("paper20.png").convert()
        self.ball_sprite.set_colorkey(RED)



    def movex(self):
        if change_pos == True:
            self.x += self.changex

            if self.changex > 0:
                if self.changex <= 0:
                    self.changex = 0
                self.changex -= self.gravity

            elif self.changex < 0:
                self.changex += self.gravity
                if self.changex >= 0:
                    self.changex = 0


    def movey(self):
        if change_pos == True:
            self.y += self.changey

            if self.changey > 0:
                self.changey -= self.gravity
                if self.changey <= 0:
                    self.changey = 0
            elif self.changey < 0:
                self.changey += self.gravity
                if self.changey >= 0:
                    self.changey = 0
                    self.changex = 0




paper_ball = Ball()
paper_ball.x = 200
paper_ball.y = 200

pygame.display.set_caption("Paperball")

all_sprites = pygame.sprite.Group()
all_sprites.add(paper_ball)


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and change_pos == False:
                paper_ball.changex += 1
                print "x = " + str(paper_ball.changex)
            if event.key == pygame.K_LEFT and change_pos == False:
                paper_ball.changex -= 1
                print "x = " + str(paper_ball.changex)
            if event.key == pygame.K_UP and change_pos == False:
                paper_ball.changey -= 1
                print "y = " + str(paper_ball.changey)
            if event.key == pygame.K_DOWN and change_pos == False:
                paper_ball.changey += 1
                print "y = " + str(paper_ball.changey)
            if event.key == pygame.K_SPACE:
                change_pos = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    screen.blit(background_image, [0, 0])

    # Get the current mouse position. This returns the position
    # as a list of two numbers.

    paper_ball.movex()
    paper_ball.movey()



    screen.blit(paper_ball.ball_sprite, [paper_ball.x, paper_ball.y])



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
