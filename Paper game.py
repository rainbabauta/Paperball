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
size = (333, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Paperball")
background_image = pygame.image.load("room.jpg").convert()

targetx = 140
targety = 100


change_pos = False


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = ""
        self.y = ""
        self.changex = 0
        self.changey = 0
        self.gravity = 0

        self.image = pygame.image.load("paper20.png").convert()
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect(center=(168,600))



    def update(self):
        if change_pos == True:
            print "yep"
            self.rect.x += self.changex

            if self.changex > 0:
                if self.changex <= 0:
                    self.changex = 0
                self.changex -= self.gravity

            elif self.changex < 0:
                self.changex += self.gravity
                if self.changex >= 0:
                    self.changex = 0

            self.rect.y += self.changey

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
paper_ball.x = 139
paper_ball.y = 600

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
                print "shoot"


    # --- Game logic should go here


    # --- Drawing code should go here
    screen.blit(background_image, [0, 0])

    pygame.draw.rect(screen, BLACK, [targetx, targety, 50, 50])

    # Call the update() method for all blocks in the block_list
    all_sprites.update()

    # Update & display ball sprite
    all_sprites.draw(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
