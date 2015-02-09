import pygame
import math


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

GRAVITY = .04
VELOCITY = 2.5

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
        self.change = [0,0]
        self.gravity = 0
        self.distance = [10,100]
        self.collision1 = [0,0]
        self.collision2 = [0,0]
        self.collision3 = [0,0]


        self.image = pygame.image.load("paper20.png").convert()
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect(center=(168,600))

    def calculate_collision(self):
        self.distance[0] = self.distance[0] * self.change[0]
        self.distance[1] = self.distance[1] * self.change[1]
        self.collision1[0] = self.rect.x + self.distance[0]
        self.collision1[1] = self.rect.y - self.distance[1]
        print "initial distance y = ", self.distance[1]
        print "initial collision y = ", self.collision1[1]
        # set 2 more collision points?

    def update(self):
        if change_pos == True:
            self.rect.x += self.change[0]
            print "collision x = ", self.collision1[0]
            print "x = ", self.rect.x

            if self.change[0] > 0:
                if self.change[0] <= 0:
                    self.change[0] = 0
                self.change[0] -= self.gravity

            elif self.change[0] < 0:
                self.change[0] += self.gravity
                if self.change[0] >= 0:
                    self.change[0] = 0

            self.rect.y -= self.change[1]
            print "collision y = ", self.collision1[1]
            print "y = ", self.rect.y
            print "gravity = ", self.gravity

            if self.rect.y <= self.collision1[1]:
                self.gravity += GRAVITY
                # change to bounce

            if self.change[1] > 0:
                self.change[1] -= self.gravity
                if self.change[1] <= 0:
                    self.change[1] = 0
            elif self.change[1] < 0:
                self.change[1] += self.gravity
                if self.change[1] >= 0:
                    self.change[1] = 0



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
                paper_ball.change[0] += VELOCITY
                print "x = " + str(paper_ball.change[0])
            if event.key == pygame.K_LEFT and change_pos == False:
                paper_ball.change[0] -= VELOCITY
                print "x = " + str(paper_ball.change[0])
            if event.key == pygame.K_UP and change_pos == False:
                paper_ball.change[1] += VELOCITY
                print "y = " + str(paper_ball.change[1])
            if event.key == pygame.K_DOWN and change_pos == False:
                paper_ball.change[1] -= VELOCITY
                print "y = " + str(paper_ball.change[1])
            if event.key == pygame.K_SPACE:
                paper_ball.calculate_collision()
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
